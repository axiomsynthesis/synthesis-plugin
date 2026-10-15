# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""Which automation, if any, this session is running right now.

An automation answers in its own short shape (a headline, one table, one move),
so its Synthesis calls should come back with the data and its warnings only, not
the general notes an open question gets. The server cannot see the person's
prompt, so the plugin tells it: mark_automation.py notes the automation when the
person starts one, and register_capture.py adds AUTOMATION_ARG to every Synthesis
call until the person sends anything else.

What counts as starting one, from the prompt the person sent:
  * a slash command whose file in this plugin's commands folder is an automation
    page (it carries AUTOMATION_MARK), or /go;
  * the gallery's copied instructions pasted in (they begin with AUTOMATION_MARK).
Any other prompt clears the mark. A mark older than MAX_AGE is ignored.

STDLIB ONLY, and every reader fails to "no automation": a missed mark costs a
longer answer, never a broken tool call.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time

AUTOMATION_ARG = "_synthesis_automation"
# The first words of every automation's instructions (catalog.build_instructions).
AUTOMATION_MARK = "Run the Synthesis automation"
GO_COMMAND = "go"
MAX_AGE = 2 * 60 * 60
_ID_RE = re.compile(r'Run the Synthesis automation "[^"]*" \(id: ([a-z0-9-]+)')
_CMD_RE = re.compile(r"^\s*/(?:[a-z0-9_-]+:)?([a-z0-9_-]+)\b")


def _state_dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".synthesis", "automation")


def _path(session_id: str) -> str:
    # Hashed so a session id can never be a path, whatever it contains.
    return os.path.join(_state_dir(), hashlib.sha256(session_id.encode("utf-8")).hexdigest()[:32])


def _commands_dir() -> str:
    root = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root, "commands")


def _command_automation(name: str) -> str:
    """The automation a slash command runs, or "" when it is not one of ours or
    not an automation (/setup, /deep)."""
    if name == GO_COMMAND:
        return GO_COMMAND
    if not re.fullmatch(r"[a-z0-9_-]{1,40}", name):
        return ""
    try:
        with open(os.path.join(_commands_dir(), f"{name}.md"), encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    if AUTOMATION_MARK not in text:
        return ""
    m = _ID_RE.search(text)
    return m.group(1) if m else name


def automation_in_prompt(prompt: str) -> str:
    """The automation this prompt starts, or ""."""
    if not isinstance(prompt, str) or not prompt.strip():
        return ""
    m = _CMD_RE.match(prompt)
    if m:
        return _command_automation(m.group(1))
    if prompt.lstrip().startswith(AUTOMATION_MARK):
        m = _ID_RE.search(prompt)
        return m.group(1) if m else "pasted"
    return ""


def mark(session_id: str, automation: str) -> None:
    """Record the running automation, or clear the record when automation is ""."""
    if not session_id:
        return
    path = _path(session_id)
    if not automation:
        try:
            os.remove(path)
        except OSError:
            pass
        return
    os.makedirs(_state_dir(), mode=0o700, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"automation": automation, "at": time.time()}, f)
    os.replace(tmp, path)


def running(session_id: str) -> str:
    """The automation this session is running, or ""."""
    if not session_id:
        return ""
    try:
        with open(_path(session_id), encoding="utf-8") as f:
            rec = json.load(f)
    except (OSError, ValueError):
        return ""
    if not isinstance(rec, dict) or time.time() - float(rec.get("at") or 0) > MAX_AGE:
        return ""
    name = str(rec.get("automation") or "")
    return name if re.fullmatch(r"[a-z0-9_-]{1,80}", name) else ""
