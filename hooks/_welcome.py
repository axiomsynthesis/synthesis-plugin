# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""The one-time welcome: what a person sees the first time Claude opens with Synthesis.

WHY (2026-10-19). Claude Code has no "just installed" moment, from the store or from
the one-line install. The earliest the plugin can reach someone is the first session
start after install, and before this nobody was told /start existed. The founder asked
that the first open tell them how to use it, what to look at first, which commands to
type and which automations to open.

TWO HALVES, BECAUSE THEY REACH DIFFERENT READERS.
- SCREEN is shown on screen before the person types (the hook's `systemMessage`,
  measured in the terminal 2026-10-19: it prints under "SessionStart:startup says").
  It works with no sign-in and no network, so it is only the first two steps.
- GUIDE goes into the model's context. Claude opens its first reply with it, and fills
  in the brand's biggest problem once it can read the brand.

ONCE PER COMPUTER. A marker file in ~/.synthesis says it was shown. Someone who used
Synthesis before this shipped already has ~/.synthesis/keys (written on their first
Synthesis call), so an upgrade does not greet a customer of three months as new.

Every shortcut named here must exist (tests/test_plugin_welcome.py).
Rule 1 of session_start.py applies: any failure means no welcome, never an error.
"""
from __future__ import annotations

import os

SHORTCUTS = ("start", "health", "whyprofit", "stockout", "fees", "reorder", "adloss", "winback")

SCREEN = (
    "Welcome to Synthesis. Your brand's real numbers now live inside Claude.\n"
    "1. Sign in: type /mcp, press Enter twice, and sign in with your Synthesis key.\n"
    "2. Type /start and say what you do. It picks your shortcuts and runs the first one.\n"
    "Or just ask: \"What needs my attention this week?\""
)

GUIDE = (
    "FIRST TIME WITH SYNTHESIS. This person just installed Synthesis and this is their "
    "first chat with it. Whatever they ask first, open your reply with this short "
    "welcome, then answer them. If Synthesis is not signed in yet, the sign-in line "
    "comes before it. Plain words, one line each, about 12 lines, in this order:\n"
    "1. What it is: their brand's real sales, ads, customer and profit numbers, read "
    "inside Claude.\n"
    "2. How to use it: ask in plain words, like they would ask an analyst. Type / to "
    "see every shortcut.\n"
    "3. Look at first: \"What needs my attention this week?\" If Synthesis is signed in, "
    "call `brand_brain` with action `what_matters` and name the top item with its "
    "dollars a month. If not, say it will work once they sign in.\n"
    "4. Commands to try first: /start picks the shortcuts for their job; /health shows "
    "which data needs attention; /whyprofit explains why profit moved; /stockout warns "
    "before a product runs out; /fees finds Amazon fees that went up for no reason; "
    "/deep and a question gives a fully checked deep answer.\n"
    "5. Automations worth opening: /reorder drafts a reorder plan; /adloss finds ads "
    "that lose money after costs; /winback builds a win-back list and email. /go on its "
    "own lists every other automation.\n"
    "6. Close the welcome with: type /start any time to see this again.\n"
    "Show this welcome once, in your first reply only."
)


def _dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".synthesis")


def _marker() -> str:
    return os.path.join(_dir(), "welcomed")


def due() -> bool:
    """True only on the first session on this computer. Never raises."""
    try:
        if os.path.exists(_marker()):
            return False
        if os.path.exists(os.path.join(_dir(), "keys")):
            mark_shown()            # used Synthesis before this shipped
            return False
        return True
    except Exception:               # noqa: BLE001 — rule 1
        return False


def mark_shown() -> None:
    """Record that the welcome was shown. A failure only means it shows again."""
    try:
        os.makedirs(_dir(), mode=0o700, exist_ok=True)
        with open(_marker(), "w", encoding="utf-8") as fh:
            fh.write("1\n")
    except Exception:               # noqa: BLE001 — rule 1
        pass
