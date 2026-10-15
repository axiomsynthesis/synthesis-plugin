---
name: ssi-synthesis-reasoning-method
description: >
  Load for a strategic, why or should-we question ("should we cut ad spend",
  "why is revenue falling", "what's driving repeat down", "give me a strategy
  to scale this product", "what is our biggest constraint") once the operating
  protocol has routed it to depth, when the deep analysis is done by hand in
  this session instead of by the server's deep run. Gives the order to work
  in: frame the real decision, pull fresh numbers in pairs, pin brand, date
  and source, read the plain direction, find the one fact that limits the
  rest, check like for like, play it forward, argue against it, answer, then
  file it back.
---

# Run a deep strategic analysis yourself, step by step

## Open this page when

- A decision question worked through here, with the ordinary tools: should we,
  where should we, why is, what is driving, what would you do, is it worth it,
  give me a strategy, what is our biggest risk or lever or constraint.
- The session has already turned into an analysis rather than a lookup.

Not this page: a lookup, a chart, a table, "just the number" or "keep it short" —
those get the fast path. Nor a message containing the word "deep", which starts
the server's own deep run instead.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `synthesis-reasoning-method`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_facts` · `search_knowledge` · `query_series` · `metric_timeseries` · `find_product` · `declare_not_known` · `explain_metric_move` · `find_stable_datum` · `data_freshness` · `data_freshness_sweep` · `register_prediction` · `capture_turn` · `resolve_by_senior_datum`
`check_reasoning`, with `metric` set to: `comparable_basis` · `facsimile`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_comparable_basis` means `check_reasoning` with `metric` set to `comparable_basis`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
