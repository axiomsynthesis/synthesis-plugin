---
name: ssi-synthesis-operating-protocol
description: >
  Load on every real question about your business that Synthesis can answer,
  from "what was revenue last month" or "chart sales by week" to "should we
  expand", "why is repeat down" or "what is our biggest risk". Decides how deep
  to go from what you are asking, grounds the read in your brand's verified
  facts before interpreting a number, never shows a flagged or unsourced
  figure, stays on your brand and today's date, and hands off to the deeper
  skills when the question needs them.
---

# How to answer a business question with Synthesis

## Open this page when

- Any question about your connected brand that a Synthesis tool could answer.
- A greeting, or a question about how Synthesis works, does not need it.
  Answer plainly.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `synthesis-operating-protocol`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`deep_synthesis` · `log_question` · `ingest_file` · `find_product` · `brand_facts` · `get_skill` · `metric_timeseries` · `data_freshness` · `capture_turn` · `rate_synthesis_output`
`check_reasoning`, with `metric` set to: `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_comparable_basis` means `check_reasoning` with `metric` set to `comparable_basis`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
