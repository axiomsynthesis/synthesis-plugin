#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""UserPromptSubmit — put the automation a message asks for in front of Claude.

WHY (2026-11-03). The rule "check our automations first" was written in the
start-of-chat text and on the brand overview. Ten fresh sessions read it, and
none of the eight that should have run an automation did. A rule a model may
skip is not a route. This check runs on the message itself, before Claude
answers, so the match does not depend on Claude remembering to look.

HOW. The plugin build writes two files beside this one: the server's own
matcher (_automation_match.py, a byte copy) and the ready automations it reads
(_automation_index.json). Same words, same match as get_skill's search. Only a
clear match prints, with what to do with it. A near match prints nothing: one
word in a long message is enough to make one, and an offer of an unrelated job
on "what was revenue yesterday" is worse than none. A plain number or a
definition is left untouched.

RULES. A slash command is left alone: it already names its automation. Text
the app adds inside <system-reminder> tags is not the person's words and is not
matched. FAILS OPEN: any problem prints nothing. No network. STDLIB ONLY.
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FIND_TOOL = "If `get_skill` is not in your tools yet, search your tools for `get_skill` first."
_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)


def _rows() -> list:
    with open(os.path.join(HERE, "_automation_index.json"), encoding="utf-8") as f:
        return json.load(f)


def person_words(prompt: str) -> str:
    return _REMINDER.sub(" ", str(prompt or "")).strip()


def note_for(prompt: str) -> str:
    words = person_words(prompt)
    if not words or words.startswith("/"):
        return ""
    import _automation_match as M  # noqa: E402 — written by the plugin build
    found = M.find(words, _rows(), n=1)
    if not found or found[0]["fit"] != "clear":
        return ""
    m = found[0]
    return (f"Synthesis automation for this message: \"{m['title']}\" (`{m['automation']}`). "
            f"{m['what_to_do']} {FIND_TOOL}")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0
    if not isinstance(payload, dict):
        return 0
    text = note_for(str(payload.get("prompt") or ""))
    if text:
        print(text)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:                              # noqa: BLE001 — fail open, print nothing
        sys.exit(0)
