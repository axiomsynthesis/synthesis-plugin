#!/usr/bin/env python3
# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""UserPromptSubmit — tell the person once when Synthesis was updated while this
chat was open.

WHY (2026-10-13). A chat keeps the plugin copy it started with. With auto-update
on, a newer copy lands on disk while an old chat keeps running the old one, so a
command added since then answers "no such command" in that chat. One outside
brand hit exactly that and could not tell why.

HOW. The folder this hook runs from IS the version this chat loaded (see
_update_check.installed). Claude Code records the version now installed in
~/.claude/plugins/installed_plugins.json. When the two differ, and the recorded
copy is really on disk, this chat is behind: print NOTICE once for the session.

RULES. Prints only NOTICE, a fixed string, and at most once per session.
FAILS OPEN: any problem means no notice and the prompt goes ahead untouched.
No network. STDLIB ONLY.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _update_check import MARKETPLACE, PLUGIN, installed  # noqa: E402

NOTICE = (
    "Synthesis was updated while this chat was open, and this chat is still using "
    "the older copy. Tell the person this once, as one line at the start of your "
    "answer, word for word, then answer normally and never repeat it: "
    "\"Synthesis was updated while this chat was open. Open a new chat to use the "
    "newest version.\""
)
PLUGIN_KEY = f"{PLUGIN}@{MARKETPLACE}"


def _record_path() -> str:
    base = (os.getenv("CLAUDE_CONFIG_DIR") or "").strip() or os.path.join(
        os.path.expanduser("~"), ".claude")
    return os.path.join(base, "plugins", "installed_plugins.json")


def on_record() -> str | None:
    """The version Claude Code says is installed now, if its folder exists."""
    with open(_record_path(), encoding="utf-8") as f:
        data = json.load(f)
    plugins = data.get("plugins", data) if isinstance(data, dict) else {}
    entries = plugins.get(PLUGIN_KEY) if isinstance(plugins, dict) else None
    if isinstance(entries, dict):
        entries = [entries]
    for e in entries or []:
        if not isinstance(e, dict):
            continue
        version, path = str(e.get("version") or ""), str(e.get("installPath") or "")
        if version and path and os.path.isdir(path):
            return version
    return None


def _stamp(session_id: str) -> str:
    d = os.path.join(os.path.expanduser("~"), ".synthesis", "updated_notice")
    return os.path.join(d, hashlib.sha256(session_id.encode("utf-8")).hexdigest()[:32])


def notice_for(session_id: str) -> str:
    if not session_id:
        return ""
    running = installed()
    if not running:
        return ""
    now = on_record()
    if not now or now == running:
        return ""
    stamp = _stamp(session_id)
    if os.path.exists(stamp):
        return ""
    os.makedirs(os.path.dirname(stamp), mode=0o700, exist_ok=True)
    with open(stamp, "w", encoding="utf-8") as f:
        f.write(now)
    return NOTICE


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return 0
    if not isinstance(payload, dict):
        return 0
    text = notice_for(str(payload.get("session_id") or ""))
    if text:
        print(text)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:                              # noqa: BLE001 — fail open, print nothing
        sys.exit(0)
