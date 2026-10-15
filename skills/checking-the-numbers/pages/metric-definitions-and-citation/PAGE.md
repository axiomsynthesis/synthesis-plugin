---
name: ssi-metric-definitions-and-citation
description: >
  Load before quoting any named KPI (revenue, repeat rate, LTV, new or returning customers,
  cross-sell, AOV, days of cover, CAM, MER, TACoS), when you ask "what does this metric mean",
  "how is this calculated", "what counts as a new customer", or when two answers give
  different numbers for the same label ("last week you said 12%, now you say 5%"). Picks the
  one definition in play, cites it with who is counted, the window and the source, and holds
  the glossary and the formula reference.
---

# Pick and cite the one definition for every named metric

## Open this page when

- "What is my repeat rate / LTV / AOV / TACoS / MER?" or any named KPI in an answer.
- "What does this metric mean?" "How is it calculated?" "What counts as a new customer?"
- "Last time you said X, now you say Y." Two answers, one label, two numbers.
- Building a table, report or chart that shows named KPIs side by side.
- About to reuse a figure from memory, an earlier turn or an old document.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `metric-definitions-and-citation`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`net_revenue` · `gross_revenue` · `net_revenue_dtc` · `total_net_revenue` · `aov` · `units_sold` · `new_to_brand_customers` · `returning_customers` · `total_customers` · `repeat_rate` · `product_ltv_windowed` · `cohort_ltv_table` · `cross_sell_breakdown` · `mer` · `amazon_metric` · `metric_timeseries` · `declare_not_known` · `propose_brand_fact` · `register_prediction`
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
