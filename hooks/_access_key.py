"""The optional Synthesis access key, as the customer gave it to Claude Code.

It is declared as a `sensitive` userConfig option in plugin.json, so Claude
Code asks for it, keeps it in the system's secure credential store, and hands
it to hook processes as CLAUDE_PLUGIN_OPTION_ACCESS_KEY. The hooks read it from
there and nowhere else. They used to read the key from the shell
environment, which Anthropic's directory review flags as "reading a value from
the user's machine" (finding, 2026-11). Most customers never set it: they sign
in through /mcp and the hooks work without it.
"""
from __future__ import annotations

import os

ENV = "CLAUDE_PLUGIN_OPTION_ACCESS_KEY"


def access_key() -> str:
    return (os.getenv(ENV) or "").strip()
