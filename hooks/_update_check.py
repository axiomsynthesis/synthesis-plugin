# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""Tell the person, once per session, when a newer Synthesis plugin is served.

WHY (2026-10-07). Claude Code does not auto-update a third-party marketplace
unless the person turns it on, so most installed copies never move past the day
they were installed. Nothing on their screen says so.

HOW THE INSTALLED COPY KNOWS ITS OWN VERSION. Our plugins declare no version on
purpose (the packaging step refuses one), so Claude Code names each one by
the first 12 characters of the sha256 the catalog pins for its zip, and unpacks
it into a folder with exactly that name:

    <plugins>/cache/axiom-synthesis/synthesis/<sha256[:12]>/hooks/session_start.py

So the folder this file sits in already IS the installed version. A zip cannot
carry its own digest, so nothing is baked in at build time.

ONLY THE SYNTHESIS PLUGIN IS COMPARED. The design plugin's install state cannot
be read reliably from here (an uninstall can leave its old folders behind, and
a notice to update a plugin someone removed is worse than none). It changes
rarely, and the command in the notice updates both.

THE SAME RULES AS THE HOOK THAT IMPORTS THIS, AND THEY OUTRANK THE FEATURE.

1. Never slow or break a session. One small GET with a short timeout, at most
   once every CACHE_TTL_S per installed version. A failure stamp is written
   BEFORE the fetch, so a check that fails, or hangs until the hook abandons
   it, backs off for FAILED_TTL_S instead of costing every session. Any error
   at all means no notice.
2. Nothing the server sends reaches the model. The reply is parsed only for
   64-character hex digests, and the only thing that can ever be printed is
   NOTICE, a fixed string in this file.
3. No token. The catalog is public; nothing about the person is sent.
4. Not an installed copy (a developer running the hook from the repo, a layout
   we do not recognise): no check, no notice.
5. The cache is keyed by the INSTALLED version. When the person updates, the
   old answer no longer applies and one fresh check runs, so they are never
   told to install the version they already have.
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.request
from urllib.parse import urlsplit

from _pinned_url import LOOPBACK_HOSTS, _host_allowed

CATALOG_URL = "https://synthesisintelligence.ai/cli/marketplace.json"
CATALOG_URL_ENV = "SSI_PLUGIN_CATALOG_URL"   # tests point this at a local server
MARKETPLACE = "axiom-synthesis"
PLUGIN = "synthesis"

FETCH_TIMEOUT_S = 1.5
CACHE_TTL_S = 12 * 3600
FAILED_TTL_S = 3600
MAX_CATALOG_BYTES = 256 * 1024
CACHE_FILE = "update_check.json"

_VERSION = re.compile(r"^[0-9a-f]{12}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

NOTICE = (
    "Synthesis plugin update: tell the person this once, as one line at the end "
    "of your first answer, word for word, and never repeat it: "
    "\"A Synthesis update is ready. Say 'update Synthesis' and I'll install it, "
    "or say 'turn on auto-update for Synthesis' so updates arrive on their own.\" "
    "If they ask, follow the Keeping Synthesis updated instructions above."
)


def _plugin_root() -> str:
    raw = (os.getenv("CLAUDE_PLUGIN_ROOT") or "").strip()
    if raw:
        return os.path.normpath(raw)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def installed() -> str | None:
    """The installed 12-char version, or None when this is not an installed
    copy in Claude Code's cache layout."""
    root = _plugin_root()
    version = os.path.basename(root)
    plugin_dir = os.path.dirname(root)
    market_dir = os.path.dirname(plugin_dir)
    if (not _VERSION.match(version) or os.path.basename(plugin_dir) != PLUGIN
            or os.path.basename(market_dir) != MARKETPLACE):
        return None
    return version


def _catalog_url() -> str | None:
    raw = (os.getenv(CATALOG_URL_ENV) or "").strip()
    if not raw:
        return CATALOG_URL
    parts = urlsplit(raw)
    if parts.scheme == "https" and _host_allowed(parts.hostname or ""):
        return raw
    if parts.scheme == "http" and (parts.hostname or "") in LOOPBACK_HOSTS:
        return raw
    return None


def _served_from(raw: bytes) -> str:
    """The synthesis plugin's served sha256[:12], or '' — hex digests only."""
    doc = json.loads(raw.decode("utf-8", "replace"))
    for p in doc.get("plugins") or []:
        if not isinstance(p, dict) or p.get("name") != PLUGIN:
            continue
        src = p.get("source")
        pin = str(src.get("sha256") or "").lower() if isinstance(src, dict) else ""
        if _SHA256.match(pin):
            return pin[:12]
    return ""


def _cache_path() -> str:
    return os.path.join(os.path.expanduser("~"), ".synthesis", CACHE_FILE)


def _read_cache(now: float, have: str) -> str | None:
    """The served version from a fresh-enough cache written for THIS installed
    version ('' for a remembered failure), or None to fetch again."""
    try:
        with open(_cache_path(), encoding="utf-8") as fh:
            c = json.load(fh)
        at = float(c["checked_at"])
        served = c["served"]
        for_version = c["installed"]
    except Exception:                       # noqa: BLE001 — missing or corrupt: refetch
        return None
    if for_version != have or not isinstance(served, str) or at > now:
        return None
    if served and not _VERSION.match(served):
        return None
    ttl = CACHE_TTL_S if served else FAILED_TTL_S
    if now - at >= ttl:
        return None
    return served


def _write_cache(now: float, have: str, served: str) -> None:
    try:
        path = _cache_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = f"{path}.{os.getpid()}.tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump({"checked_at": now, "installed": have, "served": served}, fh)
            os.replace(tmp, path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
    except Exception:                       # noqa: BLE001 — a cache we cannot write is a refetch later
        pass


def served(have: str, now: float | None = None) -> str:
    """The served 12-char version; '' when unknown for any reason."""
    now = time.time() if now is None else now
    cached = _read_cache(now, have)
    if cached is not None:
        return cached
    # Stamp the failure FIRST. If this fetch hangs past the hook's join, the
    # process exits with the stamp in place, and the next sessions back off.
    _write_cache(now, have, "")
    url = _catalog_url()
    if not url:
        return ""
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT_S) as resp:
            result = _served_from(resp.read(MAX_CATALOG_BYTES + 1)[:MAX_CATALOG_BYTES])
    except Exception:                       # noqa: BLE001 — rule 1
        return ""
    if result:
        _write_cache(now, have, result)
    return result


def notice() -> str:
    """The line to print: SELF_UPDATING when this hook just started the update
    itself, NOTICE when a newer version is served and it could not, else ''."""
    have = installed()
    if not have:
        return ""
    serve = served(have)
    if not serve or serve == have:
        return ""
    if self_update(serve):
        return SELF_UPDATING
    return NOTICE


# ---------------------------------------------------------------------------
# Updating ourselves when the person asked for it and Claude Code will not
# ---------------------------------------------------------------------------
# WHY (2026-10-18). The founder turned auto-update on (autoUpdate true on our
# marketplace, in settings.json and in Claude Code's own known_marketplaces.json)
# and his copy still sat 12 days behind. The desktop app starts the Claude Code
# inside it with DISABLE_AUTOUPDATER=1, because the app updates Claude Code
# itself, and that switch also stops Claude Code updating marketplaces. So for
# anyone using Synthesis in the desktop app, "turn on auto-update" did nothing.
#
# So the hook does what Claude Code would have done, ONLY when all of these hold:
#   * the person turned auto-update on for our marketplace (their own choice),
#   * Claude Code's own updater is switched off in this process
#     (DISABLE_AUTOUPDATER), so this never races Claude Code doing it itself,
#   * a newer version is served, and this hook has not already tried it,
#   * a `claude` command can be found to run the update with.
# It runs Claude Code's own update commands, detached, so the session never
# waits on it. Nothing the server sends is passed to the command: the commands
# and the marketplace name are fixed strings in this file.
SELF_UPDATING = (
    "Synthesis update: tell the person this once, as one line at the end of your "
    "first answer, word for word, and never repeat it: \"Synthesis is installing "
    "its latest update in the background. Open a new chat in a minute to use it.\""
)
SELF_UPDATE_FILE = "self_update.json"
SELF_UPDATE_RETRY_S = 6 * 3600
_UPDATE_ARGS = (("plugin", "marketplace", "update", MARKETPLACE),
                ("plugin", "update", f"{PLUGIN}@{MARKETPLACE}"),
                ("plugin", "update", f"synthesis-design@{MARKETPLACE}"))


def _claude_dir() -> str:
    return (os.getenv("CLAUDE_CONFIG_DIR") or "").strip() or os.path.join(
        os.path.expanduser("~"), ".claude")


def auto_update_opted_in() -> bool:
    """True when the person turned auto-update on for OUR marketplace, read where
    they set it (settings.json) or where Claude Code copies it."""
    places = ((os.path.join(_claude_dir(), "settings.json"), ("extraKnownMarketplaces", MARKETPLACE)),
              (os.path.join(_claude_dir(), "plugins", "known_marketplaces.json"), (MARKETPLACE,)))
    for path, keys in places:
        try:
            with open(path, encoding="utf-8") as fh:
                node = json.load(fh)
            for k in keys:
                node = node.get(k) if isinstance(node, dict) else None
            if isinstance(node, dict) and node.get("autoUpdate") is True:
                return True
        except Exception:                   # noqa: BLE001 — unreadable: not opted in
            continue
    return False


def claude_updater_off() -> bool:
    return (os.getenv("DISABLE_AUTOUPDATER") or "").strip().lower() not in ("", "0", "false", "no")


def claude_cli() -> str | None:
    """A `claude` command to run the update with: the one on PATH, the standard
    install, or (macOS) the newest copy the desktop app keeps for itself."""
    import glob
    import shutil
    found = shutil.which("claude")
    if found:
        return found
    home = os.path.expanduser("~")
    local = os.path.join(home, ".local", "bin", "claude")
    if os.path.isfile(local) and os.access(local, os.X_OK):
        return local
    bundled = glob.glob(os.path.join(home, "Library", "Application Support", "Claude",
                                     "claude-code", "*", "*", "claude.app", "Contents",
                                     "MacOS", "claude"))
    bundled = [p for p in bundled if os.access(p, os.X_OK)]
    return max(bundled, key=os.path.getmtime) if bundled else None


def _self_update_path() -> str:
    return os.path.join(os.path.expanduser("~"), ".synthesis", SELF_UPDATE_FILE)


def _already_tried(serve: str, now: float) -> bool:
    try:
        with open(_self_update_path(), encoding="utf-8") as fh:
            c = json.load(fh)
        return c.get("served") == serve and now - float(c.get("started_at", 0)) < SELF_UPDATE_RETRY_S
    except Exception:                       # noqa: BLE001 — never tried, or unreadable
        return False


def self_update(serve: str, now: float | None = None) -> bool:
    """Start the update in the background. True only when it was started now."""
    now = time.time() if now is None else now
    if not (auto_update_opted_in() and claude_updater_off()) or _already_tried(serve, now):
        return False
    cli = claude_cli()
    if not cli:
        return False
    import shlex
    import subprocess
    script = " ; ".join(" ".join(shlex.quote(a) for a in (cli,) + args) for args in _UPDATE_ARGS)
    try:
        path = _self_update_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Stamped BEFORE starting, so a crash here cannot loop a retry every session.
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"served": serve, "started_at": now, "cli": cli}, fh)
        log = open(os.path.join(os.path.dirname(path), "self_update.log"), "a", encoding="utf-8")
        subprocess.Popen(["/bin/sh", "-c", script], stdin=subprocess.DEVNULL, stdout=log,
                         stderr=log, start_new_session=True, close_fds=True)
        return True
    except Exception:                       # noqa: BLE001 — rule 1: fall back to the notice
        return False
