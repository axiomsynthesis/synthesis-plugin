#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""PreToolUse — tie this session's answer-memory secret to the customer's own sign-in.

Runs before each MCP tool call (the matcher is every MCP server, because the claude.ai
Synthesis connector has no fixed name), does nothing unless the call goes to Synthesis,
and then adds one argument to it: the FINGERPRINT of this session's secret
(_capture_secret.py). The call is signed in through /mcp, so the
server learns which person and brand the fingerprint belongs to, and strips the
argument before any tool sees it. Later, capture_turn.py can save an answer with the
secret, which only this machine holds.

It also adds AUTOMATION_ARG while the person is running a Synthesis automation
(_automation.py), so the server answers that call with data and warnings only. That
tag does not depend on answer memory: switching memory off leaves it on.

THREE RULES, the same as the other hooks:

1. FAIL OPEN. Anything unexpected prints nothing and exits 0, and the tool call goes
   ahead exactly as Claude made it. Losing a fingerprint costs one saved answer;
   breaking a tool call costs the answer itself.
2. NEVER DECIDE PERMISSION. The output carries updatedInput and nothing else. Setting
   a permission decision here would approve every Synthesis call on the customer's
   behalf, which is theirs to decide.
3. STDLIB ONLY.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _capture_secret import (  # noqa: E402
    HASH_ARG, fingerprint, learn_server, learned_servers, load_or_create, switched_off,
)
from _transcript import DISTINCTIVE_TOOLS, OWN_TOOL_PREFIX, split_tool  # noqa: E402
from _automation import AUTOMATION_ARG, running  # noqa: E402


def _is_synthesis(name: str, session_id: str) -> bool:
    """True for the plugin's own tools, and for any tool on a server this session has
    shown to be Synthesis: the claude.ai connector, which Claude Code names after the
    connector (2026-10-07). A Synthesis-only tool name teaches the server; after that
    its ordinary tools count too. Another vendor's `read_file` never does."""
    if name.startswith(OWN_TOOL_PREFIX):
        return True
    prefix, bare = split_tool(name)
    if not prefix:
        return False
    if bare in DISTINCTIVE_TOOLS:
        learn_server(session_id, prefix)
        return True
    return prefix in learned_servers(session_id)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0
    if not isinstance(payload, dict):
        return 0
    name = str(payload.get("tool_name") or "")
    args = payload.get("tool_input")
    session_id = str(payload.get("session_id") or "")
    if not name.startswith("mcp__") or not isinstance(args, dict) or not session_id:
        return 0
    if not _is_synthesis(name, session_id):
        return 0
    updated = dict(args)
    if not switched_off():
        secret = load_or_create(session_id)
        if secret:
            updated[HASH_ARG] = fingerprint(secret)
    automation = running(session_id)
    if automation:
        updated[AUTOMATION_ARG] = automation
    if updated == args:
        return 0
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "updatedInput": updated}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:                              # noqa: BLE001 — rule 1, last line
        sys.exit(0)
