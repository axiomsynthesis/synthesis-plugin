---
name: ssi-shopify-summary-tables
description: >
  Load before reading any prebuilt Shopify summary: channel mix, subscription mix, order
  tags, new vs returning orders, the per-customer lifetime table, revenue concentration,
  winback candidates, country revenue, weekly revenue, seasonality, AOV levers or the product
  catalogue, or before writing SQL against a `fact_shopify_*` table. Situations: "how much of
  our website revenue is subscription", "who should we win back", "what share of revenue comes
  from our top customers", "which country buys most", "is this week normal for the season",
  "why does this table only have ten rows". These are snapshots rebuilt on a cadence, so they
  carry a build date and can go stale silently.
---

# The prebuilt Shopify summary tables

## Open this page when

- Any Shopify channel mix, subscription share, order tag, winback, customer concentration,
  country revenue, weekly revenue, seasonality or AOV-lever question.
- Before any `run_sql` on a `fact_shopify_*` table or on the `products` table.
- Before saying a small store "has no" signal. A table holding ten rows is a real but tiny
  holding, not an absence.
- For the raw orders, the revenue definition and the giveaway rule, load
  `ssi-shopify-orders-and-revenue`. This skill assumes those definitions.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `shopify-summary-tables`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`shopify_metric` · `describe_schema` · `run_sql` · `data_freshness_sweep`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
