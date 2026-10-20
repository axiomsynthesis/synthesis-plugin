#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""Put the brand's current state in front of the agent before it is asked anything.

Without this, a session opens blind: it does not know which data is stale, what
moved this week, or what the standing caveats are, so it either asks or assumes.
Both are worse than being told.

THREE RULES, AND THE FIRST ONE OUTRANKS THE FEATURE.

1. FAIL OPEN, ALWAYS. This runs on a customer's machine, in front of their
   terminal, before they have typed anything. A hook that hangs or crashes gets
   the plugin uninstalled that day and never reinstalled. Every failure path
   here prints nothing and exits 0: no token, no network, a slow server, a
   malformed reply, an unexpected exception. Silence is a correct outcome.

2. NEVER PRINT THE CREDENTIAL. Not in an error, not in a debug line. The token
   is read, used, and never rendered.

3. STDLIB ONLY. A customer's machine has whatever Python it has. A hook that
   needs `pip install` is a hook that does not run.

Rule 1 covers IMPORT TIME too, which is easy to forget: the try/except around
main() cannot catch anything that raises while the module is still loading. No
module-level expression here may fail on hostile input.

Output goes to stdout and becomes session context. Keep it short — this is
spent from the same budget as the actual work.
"""
from __future__ import annotations

import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pinned_url import resolve_url  # noqa: E402  (shared with capture_turn)

DEFAULT_TIMEOUT_S = 4.5   # brand_context_frame measures ~2.6s live; 3.0 left
                          # no headroom for jitter, so the one call worth
                          # making was one slow round-trip from being cut

# Deliberately tight. The operator is waiting on their prompt; a session that
# takes five seconds to open is a session they resent opening.
#
# PARSED DEFENSIVELY, AND THE REASON IS RULE 1 (2026-09-03, from review). This
# was `float(os.getenv(...))` at module level, so an empty or non-numeric
# SSI_HOOK_TIMEOUT_S raised at IMPORT — before main(), before the try/except in
# __main__ — and the hook printed a traceback and exited 1. That is the exact
# failure this file exists to prevent, in the file itself, and the tests missed
# it because they only ever set valid values.
#
# Nothing at module scope may raise. Bounds too: 0 or a negative would make the
# request misbehave, and a large one would hold the session open, which is the
# thing a tight timeout is for.
# COUPLED TO hooks.json (2026-09-03, from review). The runner kills this process
# at its own timeout, and a killed process never reaches the fail-open exit — so
# session start shows a hook timeout instead of the silence this file promises.
#
# The first version capped each REQUEST at 15s and made two of them serially, so
# against a stalled server it ran 30s under a 10s runner budget. Measured, not
# reasoned: it took exactly 30s.
#
# The bound that matters is the TOTAL, and it has to sit clearly inside the
# runner's. If you change either number, change both.
HOOK_RUNNER_TIMEOUT_S = 10.0        # must match "timeout" in hooks.json
MAX_TOTAL_S = 6.0                   # every call together, with headroom to spare

MIN_TIMEOUT_S, MAX_TIMEOUT_S = 0.5, MAX_TOTAL_S


def _timeout() -> float:
    try:
        v = float(os.getenv("SSI_HOOK_TIMEOUT_S", "") or DEFAULT_TIMEOUT_S)
    except (TypeError, ValueError):
        return DEFAULT_TIMEOUT_S
    if v != v or v in (float("inf"), float("-inf")):   # NaN / inf
        return DEFAULT_TIMEOUT_S
    return max(MIN_TIMEOUT_S, min(MAX_TIMEOUT_S, v))


TIMEOUT_S = _timeout()

# Read-only, no model calls behind it.
#
# ORDER IS THE WHOLE DESIGN (2026-09-03). The budget is spent in sequence, so
# the first entry is the one that always gets paid and the last is the one that
# gets dropped. This list used to open with data_freshness, which is the SLOWEST
# tool on the server -- measured today it does not return inside 70s, against a
# per-call cap of a few seconds inside a total of six. It could never contribute
# anything, and it spent the budget the useful call needed.
#
# Measured on an idle server, same machine, same token:
#
#   data_freshness first          3 of 6 runs produced output, 4.4-6.7s each
#   brand_context_frame only      8 of 8 runs produced output, ~1.0s each
#
# So the old order dropped the brand context about half the time and charged
# every session 4-7 seconds of startup for the privilege. Under load it is far
# worse: while two eval arms were hammering the server the fixed hook itself
# fell to 3 of 8, which is worth knowing on its own -- the server degrades
# enough under concurrency to break a several-second client budget.
TOOLS = ("brand_context_frame",)

# Printed when there is no env key. Static on purpose: this text becomes model
# context, so nothing variable may reach it.
NO_TOKEN_NUDGE = (
    "Synthesis is connected through the `synthesis` MCP server. Before you "
    "answer the first question about this business, call its "
    "`brand_context_frame` tool once so you start from the brand's current "
    "state: what is stale, what moved, and the standing caveats. If that result "
    "carries `claude_code_tip`, end your first answer with it as one line, word "
    "for word, and never repeat it later in the session."
)

# data_freshness is DELIBERATELY NOT LISTED. A call that cannot finish inside
# the budget must not be made at all: reordering it to last was not enough,
# because it still consumed every second left over and left the useful call no
# slack for ordinary jitter.
#
# Put it back once the freshness fix in this branch is deployed (its interactive
# path returns inside 25s) -- and re-measure before trusting it, rather than
# assuming the deploy did what it was meant to.


def _call(url: str, token: str, tool: str, budget_s: float) -> dict | None:
    """One tools/call within `budget_s`. None on any failure — the caller must not care why."""
    if budget_s <= 0:
        return None
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": tool, "arguments": {}},
    }).encode()
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=budget_s) as resp:
            payload = json.loads(resp.read().decode("utf-8", "replace"))
    except (urllib.error.URLError, OSError, ValueError, TimeoutError):
        return None
    except Exception:                      # noqa: BLE001 — rule 1 outranks tidiness
        return None
    if not isinstance(payload, dict):
        return None
    result = payload.get("result")
    return result if isinstance(result, dict) else None


def _text_of(result: dict) -> str:
    """MCP returns content blocks; we want the text of the first one."""
    for block in (result.get("content") or []):
        if isinstance(block, dict) and block.get("type") == "text":
            return str(block.get("text") or "")
    return ""


def _summarise(raw: str, limit: int = 600) -> str:
    """Compact a tool result. Prefers a verdict-ish field over a wall of rows."""
    try:
        data = json.loads(raw)
    except ValueError:
        return raw.strip()[:limit]
    if not isinstance(data, dict):
        return str(data)[:limit]
    keep = {}
    for k in ("summary", "verdict", "stale", "stale_tables", "freshest",
              "category_archetype", "revenue_stage", "channel_gravity",
              "value", "data_quality_flags", "claude_code_tip"):
        if data.get(k) not in (None, [], {}, ""):
            keep[k] = data[k]
    if not keep:
        keep = {k: v for k, v in list(data.items())[:6]}
    out = json.dumps(keep, default=str)
    return out[:limit]


# Printed in every session, before anything that can fail. A customer who also
# added the Synthesis connector to their Claude account gets BOTH in Claude Code
# (the desktop app surfaces account connectors), and the model picked the
# account connector's tools over the plugin's (seen 2026-10-07). The numbers are
# identical, but only the plugin's own connection carries the plugin's hooks,
# so customers should never have to name the plugin to get it. Static text: it
# becomes model context, so nothing variable may reach it.
PREFER_PLUGIN = (
    "Synthesis tools: this session may hold more than one Synthesis connection, "
    "for example a Synthesis connector added to the person's Claude account. For "
    "every Synthesis question, use this plugin's own tools, whose names start "
    "with `mcp__plugin_synthesis_synthesis__`. Use another Synthesis connection "
    "only if those tools are missing or ask for sign-in. "
    # 2026-10-14: in a chat opened right after install, the plugin's server is
    # often still connecting, and Claude told a customer their automation was
    # not there. Wait first; the loading line is the customer's cue to retry.
    "Right after install, or at the start of a chat, this plugin's `synthesis` "
    "server may still be connecting. If its tools are not in your list yet, search "
    "your tools for `synthesis` first; that search waits for a server that is "
    "still connecting. Never say an automation or command does not exist because "
    "the tools are not there yet. If they are still missing and no sign-in is "
    "asked for, tell the person in one line: \"Synthesis is still loading in this "
    "chat. Wait a minute, then open a new chat and try again.\" "
    # 2026-10-09: most customers install from the desktop app and have no
    # terminal session; /mcp works in the desktop chat box too. And a customer
    # with NO other connection must still be told, or their first session just
    # fails quietly — so this no longer hangs off the fallback.
    "If this plugin's `synthesis` server is not signed in, start your first "
    "reply by telling the person how, in one line: type `/mcp`, press Enter "
    "twice, and sign in with their Synthesis key. If they do not see Synthesis "
    "there, they fully quit Claude (Cmd+Q), open it again and do the same."
    # 2026-10-07: the /plugin menu path to auto-update confused people, so the
    # setup page now says "ask Claude to turn on auto-update". This is how.
    # The install itself writes the extraKnownMarketplaces entry (measured), so
    # setting autoUpdate on it is the whole switch.
    " Keeping Synthesis updated: if the person asks to turn on auto-update for "
    "Synthesis, edit ~/.claude/settings.json, keep every other setting as it is, "
    "and set \"autoUpdate\": true on the \"axiom-synthesis\" entry under "
    "\"extraKnownMarketplaces\"; if that entry is missing, add it with \"source\": "
    "{\"source\": \"url\", \"url\": \"https://synthesisintelligence.ai/cli/marketplace.json\"}. "
    "If they ask to update now, run `claude plugin marketplace update "
    "axiom-synthesis && claude plugin update synthesis@axiom-synthesis && claude "
    "plugin update synthesis-design@axiom-synthesis`. Either way, tell them to "
    "restart Claude Code."
)


VOICE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "answer_voice.txt")


def _print_voice() -> None:
    """The house voice, printed into every session before anything else.

    Static text shipped with the plugin (a byte copy of the server's
    house-voice file, kept identical by a test). The server's
    own copy of these rules sits past the part of its instructions Claude Code
    keeps, so without this the plugin's answers never saw them. No network, so
    it runs whether or not a key is set. A missing file prints nothing (rule 1).
    """
    try:
        with open(VOICE_FILE, encoding="utf-8") as fh:
            text = fh.read().strip()
    except OSError:
        return
    if text:
        print(text)
        print()


# The update check (2026-10-07) runs BESIDE the brand call, not after it, so it
# adds nothing to the wall-clock budget above. It gets this long from the START
# of the hook; a check still running then is abandoned (the thread is a daemon)
# and the session opens without a notice. So the hook's worst case stays
# max(MAX_TOTAL_S, UPDATE_JOIN_S), never their sum.
UPDATE_JOIN_S = 2.0


def _start_update_check() -> tuple[threading.Thread, list, float]:
    """Start the check in the background. Its only possible output is the fixed
    NOTICE string in _update_check.py; the server's reply never reaches stdout."""
    box: list = []

    def run() -> None:
        try:
            import _update_check            # lazy: an import error here is rule 1 too
            line = _update_check.notice()
            # One of the two fixed strings, or nothing.
            if line in (_update_check.NOTICE, _update_check.SELF_UPDATING):
                box.append(line)
        except Exception:                   # noqa: BLE001 — rule 1
            pass

    t = threading.Thread(target=run, name="synthesis-update-check", daemon=True)
    started = time.monotonic()
    t.start()
    return t, box, started + UPDATE_JOIN_S


def _print_update_notice(check: tuple[threading.Thread, list, float] | None) -> None:
    if check is None:
        return
    t, box, join_by = check
    t.join(max(0.0, join_by - time.monotonic()))
    if box:
        try:
            print("\n" + box[0])
        except UnicodeEncodeError:
            # A stdout that cannot encode the arrows (Windows cp1252) still
            # gets the line, with ASCII stand-ins.
            print("\n" + box[0].replace("→", ">").replace("—", "-"))


def main() -> int:
    # Before the update check starts: it writes into ~/.synthesis too, and the
    # welcome reads that folder to tell a returning customer from a new one.
    try:
        import _welcome                     # lazy: an import error here is rule 1 too
        welcome = _welcome if _welcome.due() else None
    except Exception:                       # noqa: BLE001 — rule 1
        welcome = None
    try:
        check = _start_update_check()
    except Exception:                       # noqa: BLE001 — never at the cost of the session
        check = None
    if welcome is None:
        _session_context(check)
        return 0
    # First session on this computer. The welcome needs the JSON form of hook
    # output (plain stdout never reaches the screen), so the usual context is
    # collected and carried as additionalContext beside it.
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _session_context(check)
    print(json.dumps({
        "systemMessage": welcome.SCREEN,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": buf.getvalue() + "\n" + welcome.GUIDE,
        },
    }))
    sys.stdout.flush()
    welcome.mark_shown()
    return 0


def _session_context(check) -> None:
    _print_voice()
    print(PREFER_PLUGIN)
    print()
    _brand_state()
    _print_update_notice(check)


def _brand_state() -> int:
    token = os.getenv("SSI_MCP_TOKEN", "").strip()
    if not token:
        # Most customers never set the env key: the install page signs them in
        # through /mcp, and that sign-in lives in Claude Code, not here. Saying
        # nothing left every one of them starting blind (measured live
        # 2026-10-02). So hand the job to the model, which DOES hold the
        # sign-in: a fixed line, no network, nothing about the user echoed.
        print(NO_TOKEN_NUDGE)
        return 0
    url, refusal = resolve_url()
    if refusal:
        # The token must not follow a redirected URL. This hook's stdout is
        # the MODEL's context, and the refusal quotes the env var — echoing an
        # attacker-controlled string into the session is worse than silence.
        # Start the session without the frame; the Stop hook logs the same
        # refusal by name to ~/.synthesis/capture.log on the next turn.
        return 0

    # One wall-clock budget for the whole hook, spent down as we go. Two calls
    # that each honour a per-call timeout still add up past the runner's limit.
    deadline = time.monotonic() + MAX_TOTAL_S

    parts: list[str] = []
    for tool in TOOLS:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break                                  # out of budget — ship what we have
        result = _call(url, token, tool, min(TIMEOUT_S, remaining))
        if not result:
            continue
        text = _summarise(_text_of(result))
        if text:
            parts.append(f"- {tool}: {text}")

    if not parts:
        return 0                                   # nothing to say — say nothing

    print("Synthesis — this brand right now (fetched at session start):")
    print("\n".join(parts))
    print("Treat these as the starting state. Re-pull anything you are about "
          "to act on rather than trusting this snapshot. If it carries "
          "`claude_code_tip`, end your first answer with it as one line, word for word.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:                              # noqa: BLE001 — rule 1, last line
        sys.exit(0)
