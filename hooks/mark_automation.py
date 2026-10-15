#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""UserPromptSubmit — note whether the person just started a Synthesis automation.

Starting one (/fees, /go win-back list, or the gallery's instructions pasted in)
marks this session; any other prompt clears the mark. register_capture.py reads
the mark and tags each Synthesis call of the run, so the server answers it with
data and warnings only (see _automation.py).

PRINTS NOTHING, ever: whatever a UserPromptSubmit hook prints is added to the
conversation. FAILS OPEN: any problem leaves the session unmarked and the prompt
goes ahead untouched. STDLIB ONLY.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _automation import automation_in_prompt, mark  # noqa: E402


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0
    if not isinstance(payload, dict):
        return 0
    session_id = str(payload.get("session_id") or "")
    mark(session_id, automation_in_prompt(str(payload.get("prompt") or "")))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:                              # noqa: BLE001 — fail open, print nothing
        sys.exit(0)
