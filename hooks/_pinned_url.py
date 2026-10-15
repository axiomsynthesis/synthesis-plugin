# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""The one place a hook decides where it is allowed to send a customer's token.

Both hooks used to read SSI_MCP_URL straight from the environment. The token
followed it: whatever host that variable named received a Bearer credential
and, for the Stop hook, the customer's question and Claude's full answer.
Anything that can set an environment variable on the customer's machine — a
poisoned .envrc, a CI config, a dotfile — could therefore redirect both to a
host of its choosing, and the hook would log "ok".

So the host is PINNED. An override is honoured only when it still points at
our own domain, or at loopback for local development and tests. Anything else
is refused before a socket is opened, and the refusal is returned so the hook
can log it by name — a redirect that fails quietly is indistinguishable from
one that succeeded.

Shared by both hooks on purpose: a second copy of this rule would not receive
the next fix.
"""
from __future__ import annotations

import os
from urllib.parse import urlsplit

DEFAULT_URL = "https://synthesisintelligence.ai/mcp"

# Hosts a hook may talk to. Exact match or a subdomain of the first; loopback
# is for `python3 hook.py` against a local server and for the test suite.
PINNED_HOSTS = ("synthesisintelligence.ai",)
LOOPBACK_HOSTS = ("127.0.0.1", "localhost", "::1")


def _host_allowed(host: str) -> bool:
    h = (host or "").strip().lower().rstrip(".")
    if h in LOOPBACK_HOSTS:
        return True
    return any(h == p or h.endswith("." + p) for p in PINNED_HOSTS)


def resolve_url() -> tuple[str, str]:
    """(url, refusal). `refusal` is empty when `url` may be used.

    A refused override does NOT fall back to the default: if something on the
    machine is trying to redirect the token, silently sending it to us instead
    hides the attempt. The caller logs the refusal and sends nothing.
    """
    raw = (os.getenv("SSI_MCP_URL") or "").strip()
    if not raw:
        return DEFAULT_URL, ""
    parts = urlsplit(raw)
    if parts.scheme not in ("https", "http"):
        return "", f"SSI_MCP_URL scheme {parts.scheme!r} is not http(s)"
    if parts.scheme == "http" and parts.hostname not in LOOPBACK_HOSTS:
        return "", f"SSI_MCP_URL {raw!r} is plain http to a non-loopback host"
    if not _host_allowed(parts.hostname or ""):
        return "", (f"SSI_MCP_URL host {parts.hostname!r} is not "
                    f"{PINNED_HOSTS[0]} or loopback — refusing to send the token there")
    return raw, ""
