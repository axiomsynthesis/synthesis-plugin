---
name: ssi-brand-search-and-own-name
description: >
  Load for branded search volume, "are more people searching our name", brand awareness,
  "did the TV spots or the influencer push lift searches for us", the halo of outside
  marketing on Amazon search, a branded vs non-branded split on Amazon, ads or Google, or any
  sentence that calls a search your brand's own name. Decides what counts as your name with
  one rule, and measures the trend on a fixed spelling list instead of the week-to-week
  branded flag.
---

# Measure demand for your brand's own name

## Open this page when

- "Are more people searching for our brand?" "Is brand awareness growing?"
- "Did the TV spots / billboard / influencer push / Instagram campaign lift searches for us?"
- "How much of our Amazon search is branded vs non-branded?" (also for ads and Google organic)
- "What share of the clicks on our own name do we win? Who takes the rest?"
- Before any answer or report prints "your own name", "brand recall" or "branded demand".
- When a branded number moves sharply in one week and nobody knows why.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `brand-search-and-own-name`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `search_console_organic` · `register_prediction` · `propose_brand_fact`
`amazon_metric`, with `metric` set to: `search_query_trend` · `search_query_performance` · `search_competitors` · `ppc_branded_split` · `attribution_publishers` · `attribution_trueup`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_search_query_trend` means `amazon_metric` with `metric` set to `search_query_trend`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
