---
name: ssi-amazon-revenue-basis
description: >
  Load before quoting, charting or checking any Amazon revenue, sales, units, average
  order value, order count, best day or before-and-after figure, or when two screens
  disagree on Amazon revenue ("what did I sell on Amazon this month", "why is this lower
  than Seller Central", "was yesterday my best day", "did the campaign lift sales", "my
  profit tool says less than you do"). Picks order or settlement basis, applies one shared
  revenue definition, strips rows that are not sales, and counts days on your Pacific
  Seller Central clock.
---

# Amazon revenue on the right basis and the right clock

## Open this page when

- "What is my Amazon revenue this month?" or any Amazon revenue, units, orders or average
  order value (AOV) figure.
- "Why is your number lower (or higher) than Seller Central / my accountant / my profit
  tool?"
- "Was that my best day?", "sales jumped yesterday", any day-level or week-level read.
- "Did the campaign / price change / deal lift sales?", any before-and-after read.
- Any fee rate, per-unit profit or settlement figure (with `ssi-amazon-settlement-and-fees`).
- Any time two surfaces disagree on Amazon revenue.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-revenue-basis`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`net_revenue` · `gross_revenue` · `amazon_metric` · `query_series` · `units_sold` · `monthly_projection` · `explain_metric_move` · `data_freshness` · `propose_brand_fact` · `register_prediction`
`check_reasoning`, with `metric` set to: `magnitude_consistency` · `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_magnitude_consistency` means `check_reasoning` with `metric` set to `magnitude_consistency`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
