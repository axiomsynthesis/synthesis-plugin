---
name: ssi-amazon-ads-data-reading
description: >
  Load before quoting any Amazon ad spend, attributed sales, ACoS, TACoS or ROAS figure,
  comparing two ad weeks, or reconciling your ad numbers to an agency report or the Amazon
  ad console ("what is my ACoS", "why did ad sales drop this week", "my agency says 48% and
  Synthesis says 40%", "is PPC working", "how much am I spending on Amazon ads"). Makes the
  ad numbers themselves right first: one view of the money, one attribution window per ad
  product, age-matched weeks, and all three ad products carried.
---

# Reading Amazon ad numbers without double counting or mixing windows

## Open this page when

- "What is my ACoS / TACoS / ROAS?", "how much am I spending on Amazon ads?"
- "Ad sales dropped this week", "ACoS jumped", any week-over-week or month-over-month ad read.
- "My agency's report says X and Synthesis says Y", or any tie-out to the Amazon ad console.
- "Is PPC working?", "which ad product is best?", "what does a new customer cost on Amazon?"
- Before any bid, budget, negative-keyword or scheduling recommendation, so it rests on
  clean numbers.
- When an ads tool comes back empty, or you have just connected your ad account.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-ads-data-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`breakeven_roas` · `data_freshness` · `propose_brand_fact` · `register_prediction`
`amazon_metric`, with `metric` set to: `ppc_campaigns` · `ppc_week_over_week` · `ppc_trend` · `ppc_branded_split` · `ppc_purchase_latency` · `ppc_placements` · `ppc_ntb` · `ad_spend_monthly` · `tacos` · `ppc_organic_vs_paid` · `ppc_search_terms` · `ppc_keywords` · `ppc_spend_by_parent` · `ppc_invalid_traffic` · `ppc_day_of_week` · `ppc_hour_of_day` · `ppc_account_changes`
`check_reasoning`, with `metric` set to: `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_campaigns` means `amazon_metric` with `metric` set to `ppc_campaigns`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
