---
name: ssi-paid-media-and-acquisition-economics
description: >
  Load for paid media across more than one channel and for what a new customer costs: "is paid
  working", "what is my CAC", "what is our MER", "how much does Meta over-report", "can we
  afford to scale", "what is the most we can pay per order", "where should the next dollar go",
  "are we past diminishing returns", "what is our LTV to CAC", "how long is payback".
  Triangulates platform, blended and incremental reads, picks the CAC denominator from your own
  data, and grades only against a goal you set.
---

# Paid media across channels, and the cost of a new customer

## Open this page when

- Paid media across more than one channel: "is paid working", "where should the
  next dollar go", "can we afford to scale", "are we past diminishing returns".
- What a new customer costs: cost of acquisition, marketing efficiency ratio,
  lifetime value against acquisition cost, payback, the most you can pay per order.
- How far a platform over-reports its own results.

Not this page: a single-channel creative or ad read. Those have their own pages.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `paid-media-and-acquisition-economics`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `meta_metric` · `google_ads_metric` · `tiktok_metric` · `amazon_metric` · `mer` · `total_net_revenue` · `new_customers_dtc` · `new_to_brand_customers` · `breakeven_roas` · `first_order_contribution_margin` · `product_ltv_windowed` · `cohort_ltv_table` · `shopify_metric` · `attribution_lenses` · `google_trends` · `check_reasoning` · `media_response_model` · `diminishing_returns` · `run_scenario` · `allocate_budget` · `quality_adjusted_cac` · `log_decision` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
