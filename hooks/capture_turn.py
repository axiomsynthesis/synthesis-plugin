#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""Stop hook — close the compounding loop automatically, once per turn.

WHY THIS EXISTS, AND WHY IT CAN ONLY EXIST HERE
-----------------------------------------------
On claude.ai the model's PROSE never reaches our server. MCP hands us tool calls
and our own results, nothing else. So `capture_turn` is VOLUNTARY: the model has
to decide to call it, and it fires on about 1.6% of turns. The ledger that is
supposed to compound across sessions is, in practice, barely written to.

In Claude Code we own the harness. The Stop hook is handed
`last_assistant_message` — the actual final text of the turn — so the capture can
be made deterministic instead of hoped for. That is the single thing the CLI can
do that the hosted connector cannot, and it is the reason this file exists.

WHAT IT DOES NOT DO
-------------------
It never blocks the turn. Every failure path exits 0. A capture that fails is a
lost fact; a capture that hangs is a broken product.

It does not fail SILENTLY, which is the harder rule. The sibling session-start
hook sat quiet for weeks because "no credential" and "nothing to say" produced
identical output. Here, anything that stops a capture is written to
`~/.synthesis/capture.log` with a reason, so "the loop is on" is a checkable
claim rather than an assumption.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pinned_url import DEFAULT_URL, resolve_url  # noqa: E402  (shared with session_start)
from _transcript import read_turn  # noqa: E402
from _capture_secret import load as _load_secret, switched_off  # noqa: E402

# Tells the server this call came from the recorder, so it keeps the steps. A model
# calling capture_turn itself sends no steps and is recorded as its own kind.
SOURCE = "cli_stop_hook"

STATE_DIR = os.path.expanduser("~/.synthesis")
LOG_PATH = os.path.join(STATE_DIR, "capture.log")

# capture_turn's own description says "INSTANT (returns in <1s)". Measured live
# on 2026-09-04 it took 0.77s, 3.70s and 10.38s on three consecutive calls with
# the same payload — the cold one being the 10s. Sizing a 6s timeout on that
# description is what made the first live capture fail.
#
# So the wait does not happen on the turn at all. The parent hands the request
# to a detached child and exits in milliseconds; the child waits generously and
# logs if it fails. Nobody's turn should end 10 seconds late so a fact can be
# filed, and a capture that is dropped because the server was warming up is a
# fact lost for no reason.
TIMEOUT_S = 60.0        # the DETACHED sender's budget, never the turn's
INLINE_TIMEOUT_S = 8.0  # when the send must happen ON the turn, this caps the wait.
                        # Sits inside the 10s hooks.json timeout; measured capture_turn
                        # latency was 0.77-10.4s, so a slow one is still lost -- logged,
                        # not silent, and better than holding the turn open indefinitely.
SYNC_ENV = "SSI_CAPTURE_SYNC"   # tests set this to skip the fork and assert directly

# Below this, a turn is an acknowledgement, not a finding. Capturing "Done." on
# every turn fills the ledger with noise and makes the real facts harder to find.
MIN_ANSWER_CHARS = 240


def _log(reason: str) -> None:
    """One line per skipped or failed capture. The only defence against this
    hook going quiet the way the session-start hook did."""
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            fh.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {reason}\n")
    except OSError:
        pass


ENABLE_ENV = "SSI_CAPTURE_ENABLED"


def _truthy(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in ("1", "true", "yes", "on")


def _enabled() -> bool:
    """ON BY DEFAULT (founder decision 2026-10-06). It was opt-in from 2026-09-08.

    Opt-in sounded careful and measured as dead: setting it meant typing two
    environment variables, one of them the access key, and in the 30 days to
    2026-10-06 the plugin saved no answers at all, on any brand. The brand's memory
    learned only from what Claude looked up, never from what it concluded.

    What makes ON defensible is the narrowing in main(): an answer leaves the
    machine only when that turn made a Synthesis call. A chat about anything else
    never reaches us. It is still off when the customer says so (switched_off: the
    kill switch, or SSI_CAPTURE_ENABLED set to a no), and a brand can be switched
    off on our side.
    """
    return not switched_off()


def _disabled() -> bool:
    """Kill switch. REQUIRED by the split-test harness.

    This hook talks to the server over plain HTTP, so it bypasses the CLI's
    --disallowedTools entirely. During an eval the arms deny capture_turn as an
    MCP tool precisely so 35 questions x 2 arms of scratch reasoning never enter
    the brand's permanent memory — and without this switch, the hook would walk
    straight past that and write it all anyway.
    """
    return _truthy("SSI_CAPTURE_DISABLED")


def _log_once(reason: str) -> None:
    """Like _log, but not on every turn: an opted-out install would otherwise
    write the same line every time Claude stops. One line, until it changes."""
    try:
        with open(LOG_PATH, encoding="utf-8") as fh:
            last = fh.read().rstrip("\n").rsplit("\n", 1)[-1]
        if last.endswith(reason):
            return
    except OSError:
        pass
    _log(reason)


def _token(session_id: str = "") -> tuple[str, str]:
    """(token, source). This session's answer-memory secret, else SSI_MCP_TOKEN.

    The secret (_capture_secret.py) is what nearly every customer has: it is made
    on this machine and registered through their /mcp sign-in, and the server lets
    it save an answer and nothing else. SSI_MCP_TOKEN is the older path for
    someone who exported their access key.

    This used to fall back to Claude Code's own credential store
    (~/.claude/.credentials.json) and pick our entry out by serverUrl. It was
    the sharpest edge in the package: that file holds the OAuth tokens for
    EVERY MCP server the customer has connected, it is undocumented internal
    storage that can change shape without notice, and "this plugin reads the
    credential store" is the sentence that stops a security review. It is gone,
    and must stay gone.
    """
    secret = _load_secret(session_id) if session_id else ""
    if secret:
        return secret, "capture_key"
    env = os.getenv("SSI_MCP_TOKEN", "").strip()
    return (env, "env") if env else ("", "none")


def _already_captured(session_id: str, digest: str) -> bool:
    """A Stop hook can fire more than once for one logical turn. Capturing the
    same answer twice writes the same facts twice."""
    marker = os.path.join(STATE_DIR, f"last-{session_id[:40]}")
    try:
        with open(marker, encoding="utf-8") as fh:
            if fh.read().strip() == digest:
                return True
    except OSError:
        pass
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        with open(marker, "w", encoding="utf-8") as fh:
            fh.write(digest)
    except OSError:
        pass
    return False


def _arguments(question: str, answer: str, turn: dict | None = None) -> dict:
    """What capture_turn receives. ``turn`` carries the recorder's extras: this
    turn's Synthesis calls, how many there were, Claude Code's session id, and
    whether any call this session read Google data (see _transcript)."""
    args = {"question": question, "answer": answer}
    if turn:
        args.update({"source": SOURCE,
                     "session_id": turn.get("session_id", ""),
                     "steps": turn.get("steps", []),
                     "steps_seen": turn.get("steps_seen", 0),
                     # True, False, or None ("could not check"). Never coerced:
                     # bool(None) would report an unread session as Google-free.
                     "session_read_google": (turn.get("session_read_google")
                                             if isinstance(turn.get("session_read_google"), bool)
                                             else None)})
    return args


def _call(url: str, token: str, question: str, answer: str,
          budget_s: float = TIMEOUT_S, turn: dict | None = None) -> tuple[bool, str]:
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": "capture_turn",
                   "arguments": _arguments(question, answer, turn)},
    }).encode()
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream",
                 "Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=budget_s) as resp:
            payload = json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return False, f"http {e.code}"
    except (urllib.error.URLError, OSError, ValueError, TimeoutError) as e:
        # The class name alone is not a diagnosis. URLError covers DNS failure,
        # a refused connection and a blocked proxy tunnel alike, and a hook runs
        # in whatever environment the host gives it -- which is not necessarily
        # the shell's. Record the reason and whether a proxy was visible, or the
        # next person debugging this learns only that something went wrong.
        proxy = "set" if (os.getenv("HTTPS_PROXY") or os.getenv("https_proxy")) else "unset"
        return False, f"{e.__class__.__name__}: {str(e)[:90]} [proxy {proxy}]"
    if isinstance(payload, dict) and payload.get("error"):
        return False, f"rpc {str(payload['error'])[:80]}"
    return True, "ok"


def main() -> int:
    if _disabled():
        return 0                                    # eval harness — stay out of the ledger
    # The pin is checked BEFORE the on/off switch. A refused SSI_MCP_URL is
    # evidence that something on this machine is trying to redirect the token,
    # and it is exactly as much evidence on an install that switched memory off —
    # review found that ordering them the other way made a redirect attempt
    # on such an install look identical to a healthy quiet session.
    url, refusal = resolve_url()
    if refusal:
        _log_once(f"REFUSED: {refusal}. Nothing was sent.")
        return 0
    if not _enabled():
        _log_once("skip: answer memory is switched off on this machine "
                  f"(SSI_CAPTURE_DISABLED, or {ENABLE_ENV} set to no). Nothing is sent.")
        return 0

    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        _log("skip: unreadable hook payload")
        return 0

    answer = (payload.get("last_assistant_message") or "").strip()
    if not answer:
        _log("skip: no last_assistant_message on this Stop event")
        return 0
    if len(answer) < MIN_ANSWER_CHARS:
        return 0                                    # an acknowledgement, not a finding

    # THE PROMISE: an answer leaves this machine only when its own turn used
    # Synthesis. Read before anything else, so a turn that did not use us costs
    # no credential lookup and sends nothing at all.
    question, steps, seen, read_google = read_turn(str(payload.get("transcript_path") or ""))
    if not steps and not seen:
        _log_once("skip: this answer did not use Synthesis, so nothing was sent")
        return 0

    raw_session = str(payload.get("session_id") or "")
    token, source = _token(raw_session)
    if not token:
        _log("SKIPPED: no credential — this session has no answer-memory key (the "
             "plugin adds one on the first Synthesis call) and SSI_MCP_TOKEN is not "
             "set. The compounding loop is NOT running.")
        return 0

    session_id = raw_session or "anon"
    digest = hashlib.sha256(answer.encode("utf-8")).hexdigest()[:32]
    if _already_captured(session_id, digest):
        return 0

    turn = {"session_id": raw_session,
            "steps": steps, "steps_seen": seen, "session_read_google": read_google}

    if _must_send_inline():
        ok, why = _call(url, token, question, answer, INLINE_TIMEOUT_S, turn=turn)
        if not ok:
            _log(f"FAILED via {source}: {why} ({len(answer)} chars not captured)")
        return 0

    _send_detached(url, token, question, answer, source, turn)
    return 0


def _must_send_inline() -> bool:
    """True when detaching would outlive the network path the child needs.

    Diagnosed 2026-09-04. Inside a `claude -p` session HTTPS_PROXY is not the
    shell's -- Claude Code provisions its OWN egress proxy on a different
    loopback port for its child processes. A detached sender therefore inherits
    a proxy address whose lifetime is the PARENT's: the moment the headless run
    exits, the proxy goes with it and the orphan gets ECONNREFUSED. Every
    capture in a `-p` session was lost this way, while the identical hook run
    from a shell succeeded in 0.067s.

    A loopback proxy is the tell. Nothing on 127.0.0.1 outlives the process tree
    that published it, so where one is configured the send happens on the turn,
    inside the hook's own timeout, and the parent is still there to carry it.

    Most machines have no proxy at all, and there the send detaches as designed
    and no turn waits on the ledger. This is the sandboxed / proxied case
    specifically, not the normal one.
    """
    if os.getenv(SYNC_ENV, "").strip().lower() in ("1", "true", "yes", "on"):
        return True
    proxy = (os.getenv("HTTPS_PROXY") or os.getenv("https_proxy") or "").strip()
    return ("127.0.0.1" in proxy) or ("localhost" in proxy) or ("::1" in proxy)


def _send_detached(url: str, token: str, question: str, answer: str, source: str,
                   turn: dict | None = None) -> None:
    """Hand the request to a child that outlives this hook, and return at once.

    The turn must not wait on the ledger. If the handoff itself fails, that is
    logged — a capture nobody attempted has to be visible, or this hook goes
    quiet exactly the way the session-start one did.
    """
    import subprocess
    import tempfile
    try:
        fd, path = tempfile.mkstemp(prefix="ssi-capture-", suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump({"url": url, "token": token, "question": question,
                       "answer": answer, "source": source, "turn": turn}, fh)
    except OSError as e:
        _log(f"FAILED: could not stage the capture ({e.__class__.__name__})")
        return
    try:
        kwargs = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL,
                  "stdin": subprocess.DEVNULL}
        if hasattr(os, "setsid"):
            kwargs["start_new_session"] = True      # POSIX: survive the hook exiting
        elif hasattr(subprocess, "DETACHED_PROCESS"):
            kwargs["creationflags"] = subprocess.DETACHED_PROCESS
        subprocess.Popen([sys.executable, os.path.abspath(__file__), "--send", path], **kwargs)
    except OSError as e:
        _log(f"FAILED: could not start the sender ({e.__class__.__name__})")
        try:
            os.unlink(path)
        except OSError:
            pass


def _send_from_file(path: str) -> int:
    """The detached child. Waits as long as it needs to, then cleans up."""
    try:
        with open(path, encoding="utf-8") as fh:
            job = json.load(fh)
    except (OSError, ValueError):
        return 0
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass
    ok, why = _call(job["url"], job["token"], job.get("question", ""), job["answer"],
                    turn=job.get("turn"))
    if not ok:
        _log(f"FAILED via {job.get('source', '?')}: {why} "
             f"({len(job['answer'])} chars not captured)")
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3 and sys.argv[1] == "--send":
            sys.exit(_send_from_file(sys.argv[2]))
        sys.exit(main())
    except Exception:                               # noqa: BLE001 — never block a turn
        _log("FAILED: unhandled exception in capture hook")
        sys.exit(0)
