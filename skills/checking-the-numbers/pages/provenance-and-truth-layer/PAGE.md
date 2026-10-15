---
name: ssi-provenance-and-truth-layer
description: >
  Load before stating, charting or comparing any number, or before saying how
  sure you are of a claim. "What was revenue last month?" "How confident are
  you?" "Chart it." "Is that right?" "Where did that number come from?" Makes
  every figure trace to a tool result pulled this session, carry its tier
  (measured, calculated, modeled, judgment or opinion) and a full citation, and
  never be invented, including chart points and percentages.
---

# Know how you know each number, and author none

## Open this page when

- Before any answer that states a number, a percentage, a trend or a chart.
- "How are sales doing?" "What's our repeat rate?" "Plot it by week."
  "Are we sure about that?" "How confident are you?"
- Before comparing two figures, or reusing a figure from an earlier answer.
- Before any claim that "the category usually does X" or "brands like us see Y".
- When you are asked where a number came from.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `provenance-and-truth-layer`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`query_series` · `metric_timeseries` · `total_net_revenue` · `declare_not_known` · `score_truth_tpfe` · `emit_chart` · `get_calibration_for_claim` · `track_record`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
