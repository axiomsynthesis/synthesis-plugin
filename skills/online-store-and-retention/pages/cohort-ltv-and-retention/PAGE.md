---
name: ssi-cohort-ltv-and-retention
description: >
  Load for any LTV, cohort, retention curve, payback, "what is a customer worth", young-product
  repeat or cohort grid question on Amazon, Shopify, Recharge or Skio ("what is our 90-day LTV",
  "are newer customers worse than older ones", "which product brings in the best customers",
  "does the new product retain", "why did LTV drop", "how long until a customer pays back").
  Compares only windows both cohorts have closed, picks the right LTV reader per channel, knows
  which readers leave an unfinished window blank, and splits an LTV drop into order value,
  orders per customer and entry-product mix.
---

# Read LTV, retention and cohorts at matched maturity

## Open this page when

- "What is a customer worth?" "What is our LTV?" "What is our 90-day / 12-month LTV?"
- "Are newer customers worse than older ones?" "Is retention getting worse?"
- "Which product brings in the most valuable customers?" "Which front door is best?"
- "Does the new product retain?" "Why is its repeat so low?"
- "How long until a customer pays back?" "What is LTV to CAC?"
- "Why did LTV drop?" "Project this cohort to a year."
- Reading any cohort grid, retention heatmap or survival table.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `cohort-ltv-and-retention`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`product_ltv_windowed` · `product_ltv` · `cam_by_sku` · `cohort_ltv_table` · `cohort_retention_table` · `brand_ltv` · `ltv_driver_dimensions` · `ltv_drivers` · `shopify_metric` · `recharge_metric` · `skio_metric` · `sns_cohorts` · `subscribe_save_attach_rate` · `query_series` · `first_order_contribution_margin` · `amazon_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
