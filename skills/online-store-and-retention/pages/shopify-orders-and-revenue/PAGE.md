---
name: ssi-shopify-orders-and-revenue
description: >
  Load before quoting any Shopify or website revenue, order count, average order value,
  discount, refund or product figure, and before writing SQL on Shopify order tables.
  Situations: "what did the website sell last month", "why is your Shopify number different
  from Shopify Admin", "what is our DTC AOV", "how many web orders did we get", "how much did
  we give away in samples", "did the sale month really grow". Gives the one revenue definition,
  says which tools include refunds and which do not, removes giveaways by the money rule, and
  lists the checks that catch a quietly wrong number.
---

# Shopify orders and revenue, read correctly

## Open this page when

- Any Shopify or direct-to-consumer (DTC, your own website) revenue, orders, average order
  value (AOV), discount, refund, product or customer figure.
- "Why is your Shopify number different from Shopify Admin, or from my accountant?"
- Before any `run_sql` on `orders_clean`, `orders` or `order_line_items`.
- Before any Shopify lifetime value or cohort read (load the cohort and retention skill too).
- For sessions, traffic source or conversion rate, load `ssi-shopify-traffic-and-conversion`
  instead. For the prebuilt monthly, weekly and customer summary tables, load
  `ssi-shopify-summary-tables`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `shopify-orders-and-revenue`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`net_revenue_dtc` · `aov_dtc` · `shopify_metric` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
