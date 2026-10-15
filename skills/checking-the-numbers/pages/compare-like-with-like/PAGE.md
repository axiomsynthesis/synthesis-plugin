---
name: ssi-compare-like-with-like
description: >
  Load before ranking products or cohorts, saying "X beats Y", quoting a ratio,
  share, month-to-date, projection or year-over-year change, or deciding that two
  numbers conflict ("is product A doing better than product B", "which cohort
  retains best", "are we up on last year", "how are we tracking this month",
  "why does one tool say one number and another tool a different one"). Checks
  that two figures share the same window, sample size, maturity, definition and
  population before they are compared, picks the right period tool, and tells a
  real conflict from two different measures.
---

# Compare like with like

## Open this page when

- "Is product A doing better than product B?" "Which cohort retains best?"
- "How are we tracking this month?" "Will we hit the month?" "Are we up on last year?"
- "Our share went up, is that real?" "Did the new product take over?"
- "Why does this tool say one number and that tool say another?"
- Any answer about to say "X beats Y", "consistent with", "Nx stronger", a
  percentage change, or "the data conflicts".
- Any figure recalled from notes, an uploaded file or a past answer that is about
  to be set next to a fresh pull.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `compare-like-with-like`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`check_reasoning` · `mtd_comparison` · `monthly_projection` · `yoy_comparison` · `metric_timeseries` · `query_series` · `gateway_repeat` · `repeat_rate` · `product_ltv_windowed` · `cross_sell` · `sequenced_cross_sell` · `cross_sell_breakdown` · `benchmark_metric` · `record_contradiction`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
