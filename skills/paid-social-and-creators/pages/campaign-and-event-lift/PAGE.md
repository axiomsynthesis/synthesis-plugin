---
name: ssi-campaign-and-event-lift
description: >
  Load for "how did the campaign, launch, TV week, promo, billboard, celebrity deal or site
  change do", "sales jumped this week, was it the campaign", "is this a step change", "did the
  SEO change bring sales", or any readout over an arbitrary date window (a six-day flight,
  before / during / after). Confirms the definition, splits the result by product, compares the
  same dates last year, uses break dates and geography as tests, checks the data before
  contradicting anyone, prices the deal against a payback bar, and says what is unknown.
---

# Did a campaign or dated event move sales?

## Open this page when

- "Did the TV / billboard / influencer / celebrity campaign work?"
- "How did the launch / promo / Prime week do?" "Did the site or SEO change bring sales?"
- "Sales jumped this week. Was it the campaign?" "Is this a step change?"
- Any readout over a window no standard tool takes.
- Before a report or deck says a dated event caused anything.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `campaign-and-event-lift`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `query_series` · `shopify_metric` · `meta_metric` · `breakeven_roas` · `describe_schema` · `run_sql` · `register_prediction` · `propose_brand_fact` · `capture_turn`
`amazon_metric`, with `metric` set to: `search_query_trend`
`check_reasoning`, with `metric` set to: `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_search_query_trend` means `amazon_metric` with `metric` set to `search_query_trend`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
