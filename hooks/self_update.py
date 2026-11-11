"""Run the Synthesis plugin update in the background.

Started by _update_check.self_update() as its own process. It runs each
`claude plugin ...` step as a plain argument list, no shell, one after another,
and keeps going if one fails, the same as the old `a ; b ; c` it replaces.
Anthropic's directory review asks that anything a plugin runs ships as a file
inside the plugin, not as a command line built on the fly (finding, 2026-11).
"""
from __future__ import annotations

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _update_check import _UPDATE_ARGS  # noqa: E402


def main(argv: list[str]) -> int:
    if len(argv) != 2 or not argv[1]:
        return 2
    cli = argv[1]
    for args in _UPDATE_ARGS:
        try:
            subprocess.run([cli, *args], stdin=subprocess.DEVNULL, check=False)
        except OSError as exc:
            print(f"self_update: {' '.join(args)} failed: {exc}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
