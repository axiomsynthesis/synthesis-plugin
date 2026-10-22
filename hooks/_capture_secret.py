# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""The answer-memory secret: one per Claude Code session, kept on this machine.

Most customers sign in through /mcp, and that sign-in lives inside Claude Code where
no hook can read it. So the Stop hook had nothing to send an answer with, and for
30 days it sent none (measured 2026-10-06). This is the fix, in three steps:

  1. a random secret per session, written here, readable by this user only;
  2. each signed-in Synthesis result carries a pass from the server naming this person
     and brand (_transcript.latest_pass);
  3. capture_turn.py, only on a turn that used Synthesis, sends the answer with the
     secret itself as its bearer and the pass beside it, to our pinned host and nowhere
     else. The server ties the secret's fingerprint to whoever the pass names.

The secret never enters a tool call, the model's context or the transcript. The
server side, and why the key can only ever save an answer, lives with the server.

Stdlib only, and nothing at module scope may raise (see session_start.py, rule 1).
"""
from __future__ import annotations

import hashlib
import os
import secrets
import time

PREFIX = "syncap_"
# Must equal the server's own name for this argument. A test reads both.
HASH_ARG = "_synthesis_memory_id"
MAX_AGE_S = 14 * 86400           # a secret file older than this is removed


def _truthy(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in ("1", "true", "yes", "on")


def switched_off() -> bool:
    """True when this machine has answer memory off.

    ON by default (founder decision 2026-10-06). Off when SSI_CAPTURE_DISABLED is set
    (the kill switch the eval harness uses) or SSI_CAPTURE_ENABLED is set to a no.
    A brand can also be switched off on our side; that is checked by the server.
    """
    if _truthy("SSI_CAPTURE_DISABLED"):
        return True
    return os.getenv("SSI_CAPTURE_ENABLED", "").strip().lower() in ("0", "false", "no", "off")


def _key_dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".synthesis", "keys")


def _path(session_id: str) -> str:
    # Hashed so a session id can never be a path, whatever it contains.
    return os.path.join(_key_dir(), hashlib.sha256(session_id.encode("utf-8")).hexdigest()[:32])


def load(session_id: str) -> str:
    """This session's secret, or "" when there is none."""
    if not session_id:
        return ""
    try:
        with open(_path(session_id), encoding="utf-8") as fh:
            value = fh.read().strip()
    except OSError:
        return ""
    return value if value.startswith(PREFIX) else ""


def load_or_create(session_id: str) -> str:
    """This session's secret, made now if it does not exist yet. "" on any failure."""
    existing = load(session_id)
    if existing or not session_id:
        return existing
    try:
        os.makedirs(_key_dir(), mode=0o700, exist_ok=True)
        secret = PREFIX + secrets.token_urlsafe(32)
        # O_EXCL: two Synthesis calls in parallel must not each write a different one.
        fd = os.open(_path(session_id), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return load(session_id)
    except OSError:
        return ""
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(secret)
    except OSError:
        return ""
    _prune()
    return secret


def fingerprint(secret: str) -> str:
    return hashlib.sha256(secret.encode("utf-8")).hexdigest()


def _prune() -> None:
    cutoff = time.time() - MAX_AGE_S
    try:
        names = os.listdir(_key_dir())
    except OSError:
        return
    for name in names:
        p = os.path.join(_key_dir(), name)
        try:
            if os.path.getmtime(p) < cutoff:
                os.unlink(p)
        except OSError:
            pass
