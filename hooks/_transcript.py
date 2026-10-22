# Copyright (c) 2026 Axiom / Synthesis Intelligence. Proprietary & confidential. See LICENSE.
"""Read one turn out of Claude Code's session transcript: the question, and the
Synthesis tool calls made to answer it.

Used by the Stop hook (answer memory is on by default since 2026-10-06).

WHAT IS READ, AND WHAT IS NOT
-----------------------------
The question is the last message the person typed. The steps are the calls Claude
made AFTER it to a Synthesis server — the plugin's own, or the claude.ai Synthesis
connector — with the tool name and the inputs Claude gave it, the call's id and
time, and whether it errored. Never the tool's result: the server already has
every result it returned. Never a call to another MCP server, and never a built-in
tool (file reads, shell commands, web fetches). A server counts as ours by the
plugin's exact name prefix (OWN_TOOL_PREFIX), or because the session called a tool
on it that only Synthesis has (DISTINCTIVE_TOOLS).

One more thing is computed, as a single yes/no: whether ANY call in this session,
in any turn or helper agent, read Google data. The answer can
repeat figures from any earlier turn the model can still see, and Google's terms
for that data say it may never be used to improve our product for everyone. The
flag is how the server knows to keep this answer out of that. It errs toward yes:
a Google-named tool on any server counts. And when a file cannot be read, the
answer is None — "could not check" — never False, and the server treats None as
yes. A False from a file nobody read would stamp a Google answer as clean.

THE TRANSCRIPT FORMAT IS NOT A PUBLIC CONTRACT
----------------------------------------------
Claude Code documents the file as internal and liable to change between versions.
So every read here is defensive: an unreadable line is skipped, an unexpected
shape yields no step rather than a wrong one, and nothing here can raise into the
hook. If a future format hides the steps, the capture still carries the question
and the answer, as it did before steps existed.
"""
from __future__ import annotations

import glob
import json
import os
import re

# Claude Code names a plugin's MCP tools mcp__plugin_<plugin>_<server>__<tool>,
# turning any character outside letters, digits, "_" and "-" into "_". Plugin
# "synthesis" (.claude-plugin/plugin.json), server "synthesis" (.mcp.json). A test
# re-derives this from those two files, so renaming either one fails the suite
# instead of silently sending no steps.
OWN_TOOL_PREFIX = "mcp__plugin_synthesis_synthesis__"

# THE OTHER DOOR (2026-10-07): the Synthesis connector from claude.ai. Inside Claude
# Code it is named after the connector, not the plugin — mcp__claude_ai_Synthesis__…
# in a terminal, mcp__<connector id>__… in the desktop app — so no fixed prefix can
# match it, and every answer given through it was invisible to answer memory. Many
# customers, and the founder, answer through it.
#
# So a server is ours when, at any point in the session, Claude called a tool on it
# that only Synthesis has. These names are deliberately unusual: a generic name like
# `read_file` or `web_search` (both of which Synthesis also has) would count another
# vendor's server as ours. A test checks each one is a real Synthesis tool.
DISTINCTIVE_TOOLS = frozenset({
    "brand_context_frame", "brand_brain", "brand_facts", "deep_synthesis",
    "amazon_metric", "check_reasoning", "strategy_framework", "operator_inputs",
    "explain_metric_move", "product_ltv_windowed", "data_freshness_sweep", "capture_turn",
})


def split_tool(name: str) -> tuple[str, str]:
    """("mcp__<server>__", "<tool>") for an MCP tool name, else ("", name)."""
    name = str(name or "")
    if not name.startswith("mcp__") or name.count("__") < 2:
        return "", name
    prefix, bare = name.rsplit("__", 1)
    return prefix + "__", bare


def synthesis_prefixes(tool_names) -> set[str]:
    """The tool-name prefixes that are Synthesis: the plugin's own, plus any server
    on which one of the names called a DISTINCTIVE_TOOLS tool."""
    out = {OWN_TOOL_PREFIX}
    for n in tool_names:
        prefix, bare = split_tool(n)
        if prefix and bare in DISTINCTIVE_TOOLS:
            out.add(prefix)
    return out

MAX_STEPS = 100          # the server keeps at most this many; the rest are counted
STEP_ARGS_CAP = 2000     # chars of one call's inputs, as JSON
QUESTION_CAP = 30000     # chars of the question
_MAX_EXTRA_FILES = 200   # helper-agent transcripts scanned for the Google flag

# A COPY of the server's Google rule. The hook ships
# on its own and cannot import the server, so the lists are repeated here and a
# test fails if the two ever disagree.
GOOGLE_TOOL_PREFIXES = ("ga4_", "google_ads_", "gsheets_", "search_console_")
_GOOGLE_DATASETS = ("ga4", "google_ads", "google_sheets", "gsheets", "search_console")
_GOOGLE_DATASET_RE = re.compile(
    r"(?:^|[^A-Za-z0-9_])[A-Za-z0-9_]*(?:" + "|".join(_GOOGLE_DATASETS) + r")\s*\.",
    re.IGNORECASE)


def _events(path: str, must_contain: tuple[str, ...] = ()):
    """Each JSON object in a JSONL file. Lines that do not parse are skipped;
    ``must_contain`` skips lines cheaply before parsing them. A file that cannot be
    opened or read RAISES: the callers decide what an unread file means, and for
    the Google flag it means "could not check", not "nothing there"."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith("{"):
                continue
            if must_contain and not any(s in line for s in must_contain):
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if isinstance(ev, dict):
                yield ev


def _blocks(ev: dict) -> list:
    content = (ev.get("message") or {}).get("content")
    return [b for b in content if isinstance(b, dict)] if isinstance(content, list) else []


def _typed_prompt(ev: dict) -> str | None:
    """The text of a message the person typed ("" for a pasted image with no words),
    or None for anything else: an assistant line, a tool-result carrier, a
    system-injected (meta) line, or a helper agent's line."""
    msg = ev.get("message") or {}
    if not (ev.get("type") == "user" or msg.get("role") == "user"):
        return None
    if ev.get("isMeta") or ev.get("isSidechain") or "toolUseResult" in ev:
        return None
    content = msg.get("content")
    if isinstance(content, str):
        return content if content.strip() else None
    if isinstance(content, list):
        blocks = [b for b in content if isinstance(b, dict)]
        if any(b.get("type") == "tool_result" for b in blocks):
            return None
        parts = [str(b.get("text") or "") for b in blocks if b.get("type") == "text"]
        text = "\n".join(p for p in parts if p)
        if text.strip():
            return text
        # An image with no words is still the person starting a new turn.
        return "" if any(b.get("type") == "image" for b in blocks) else None
    return None


def _call_reads_google(name: str, args: object) -> bool:
    """Any MCP call whose tool is Google-named, or whose raw SQL reads a Google
    dataset. Any server, not just ours: over-counting here only withholds an
    answer, under-counting would let Google data through."""
    if not name.startswith("mcp__"):
        return False
    bare = name.rsplit("__", 1)[-1]
    if bare.startswith(GOOGLE_TOOL_PREFIXES):
        return True
    return isinstance(args, dict) and bool(_GOOGLE_DATASET_RE.search(str(args.get("sql") or "")))


def _session_files(transcript_path: str) -> list[str]:
    """The main transcript plus any helper-agent transcripts Claude Code keeps
    beside it (<session>/subagents/..., <session>/workflows/...)."""
    base = os.path.splitext(transcript_path)[0]
    extra = sorted(glob.glob(os.path.join(glob.escape(base), "**", "*.jsonl"), recursive=True))
    return [transcript_path] + extra[:_MAX_EXTRA_FILES]


def read_turn(transcript_path: str) -> tuple[str, list[dict], int, bool | None]:
    """(question, steps, steps_seen, session_read_google) for the turn that just ended.

    ``steps_seen`` is how many of our calls the turn made; ``steps`` holds at most
    MAX_STEPS of them. ``session_read_google`` is True, False, or None when the
    session could not be read — and None must never be reported as False. Never
    raises."""
    # A FILE, not merely a path that exists: a directory here would widen the
    # helper-agent scan below to every transcript under it.
    if not transcript_path or not os.path.isfile(transcript_path):
        return "", [], 0, None
    try:
        question, steps, seen = _read_steps(transcript_path)
    except Exception:                               # noqa: BLE001 — never break the hook
        return "", [], 0, None
    try:
        read_google: bool | None = _session_read_google(transcript_path)
    except Exception:                               # noqa: BLE001 — unread is not clean
        read_google = None
    return question, steps, seen, read_google


def _read_steps(transcript_path: str) -> tuple[str, list[dict], int]:
    events = list(_events(transcript_path))

    # The turn starts at the last message the person typed. If no line reads as one
    # — a format change, or a session made only of injected lines — there is no way
    # to tell this turn's calls from earlier ones, so none are sent. Sending every
    # call in the file as this answer's steps would be a confident wrong record.
    start, question = -1, ""
    for i, ev in enumerate(events):
        text = _typed_prompt(ev)
        if text is not None:
            start, question = i, text
    if start < 0:
        return "", [], 0

    # Which servers are Synthesis is learned from the WHOLE session, not just this
    # turn: a connector recognised by an earlier turn's brand_context_frame call is
    # still ours when this turn only called one of its ordinary tools.
    ours = synthesis_prefixes(
        str(b.get("name") or "") for ev in events if not ev.get("isSidechain")
        for b in _blocks(ev) if b.get("type") == "tool_use")

    calls: list[dict] = []
    errored: dict[str, bool] = {}
    for ev in events[start + 1:]:
        if ev.get("isSidechain"):
            continue
        for b in _blocks(ev):
            prefix, bare = split_tool(str(b.get("name") or "")) if b.get("type") == "tool_use" else ("", "")
            if prefix and prefix in ours:
                args = b.get("input")
                try:
                    args_json = json.dumps(args if args is not None else {}, sort_keys=True,
                                           default=str)
                except (TypeError, ValueError):
                    args_json = "{}"
                calls.append({
                    "tool": bare,
                    # Inputs over the cap go as their parsed prefix's text, marked cut,
                    # rather than as a dict the server would read as the whole input.
                    "args": args if len(args_json) <= STEP_ARGS_CAP else
                            {"_cut": True, "_chars": len(args_json),
                             "_prefix": args_json[:STEP_ARGS_CAP]},
                    "id": str(b.get("id") or ""),
                    "ts": str(ev.get("timestamp") or ""),
                })
            elif b.get("type") == "tool_result" and b.get("tool_use_id"):
                errored[str(b["tool_use_id"])] = bool(b.get("is_error"))
    for c in calls:
        c["is_error"] = errored.get(c["id"])

    return question[:QUESTION_CAP], calls[:MAX_STEPS], len(calls)


def _session_read_google(transcript_path: str) -> bool:
    """True when any call this session — this turn, an earlier one, or a helper
    agent's — read Google data. Reads every call's FULL inputs, so a long query
    cannot hide its Google table past the step cap. Raises if any file of the
    session cannot be read; the caller turns that into None."""
    for path in _session_files(transcript_path):
        for ev in _events(path, must_contain=("mcp__",)):
            for b in _blocks(ev):
                if b.get("type") == "tool_use" and _call_reads_google(
                        str(b.get("name") or ""), b.get("input")):
                    return True
    return False


# ── The answer-memory pass (2026-10-21) ──────────────────────────────────────
# Each signed-in Synthesis result carries PASS_FIELD, a pass signed by the server
# that names the person and brand the call was signed in as. capture_turn.py sends
# the newest one with the answer, and that is how the session's secret gets tied to
# them (the server's mcp_capture_key, "The pass"). It used to ride INTO each call
# through a PreToolUse hook, which Anthropic's plugin directory holds for review.
#
# Read only as a TOP-LEVEL key of a result from a Synthesis tool. Text a Synthesis
# tool merely passed along (a fetched web page, another vendor's output) sits inside
# a JSON string, where its quotes are escaped, so it can never read as that key.
PASS_FIELD = "answer_memory_pass"
PASS_PREFIX = "syncap_pass."
_PASS_RE = re.compile(r'(?<!\\)"' + PASS_FIELD + r'"\s*:\s*"(' + re.escape(PASS_PREFIX)
                      + r'[A-Za-z0-9_\-.]{20,2000})"')


def _result_texts(block: dict) -> list[str]:
    content = block.get("content")
    if isinstance(content, str):
        return [content]
    if isinstance(content, list):
        return [str(c.get("text") or "") for c in content
                if isinstance(c, dict) and c.get("type") == "text"]
    return []


def _pass_in(text: str) -> str:
    try:
        parsed = json.loads(text)
    except ValueError:
        parsed = None
    if isinstance(parsed, dict):
        value = parsed.get(PASS_FIELD)
        return value if isinstance(value, str) and value.startswith(PASS_PREFIX) else ""
    m = _PASS_RE.search(text)        # a result that is not one JSON object as a whole
    return m.group(1) if m else ""


def latest_pass(transcript_path: str) -> str:
    """The newest answer-memory pass in this session's Synthesis results, or ""."""
    if not transcript_path or not os.path.isfile(transcript_path):
        return ""
    try:
        events = [ev for ev in _events(transcript_path) if not ev.get("isSidechain")]
    except Exception:                                # noqa: BLE001 — never break the hook
        return ""
    ours = synthesis_prefixes(str(b.get("name") or "") for ev in events
                              for b in _blocks(ev) if b.get("type") == "tool_use")
    our_calls = {str(b.get("id") or "") for ev in events for b in _blocks(ev)
                 if b.get("type") == "tool_use"
                 and split_tool(str(b.get("name") or ""))[0] in ours}
    found = ""
    for ev in events:
        for b in _blocks(ev):
            if (b.get("type") == "tool_result" and not b.get("is_error")
                    and str(b.get("tool_use_id") or "") in our_calls):
                for text in _result_texts(b):
                    value = _pass_in(text)
                    if value:
                        found = value
    return found
