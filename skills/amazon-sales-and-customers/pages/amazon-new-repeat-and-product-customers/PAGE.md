---
name: ssi-amazon-new-repeat-and-product-customers
description: >
  Load for Amazon questions about new-to-brand customers, returning customers, repeat rate,
  net active customers, "how many customers bought this product", gateway products, or
  whether people rebuy the same product ("are we still acquiring", "do people come back",
  "is this our best entry product", "why does the new product show 70% returning"). Routes
  each question to the one definition that answers it, because several repeat definitions
  and two product-customer counts look alike and read very differently, and the wrong one
  flatters a young product.
---

# Pick the right new, repeat and product-customer definition on Amazon

## Open this page when

- "How many new customers did we get last month?" "Are we still acquiring?"
- "What is our repeat rate?" "Do people come back?"
- "Do people rebuy this product, or do they move on to something else?"
- "How many customers has this product brought in?" "Is it a gateway product?"
- "Is our customer base growing or shrinking?"
- "What does a new customer cost on Amazon?"
- A new product's launch read, where someone quotes a high "returning" share.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-new-repeat-and-product-customers`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`new_to_brand_customers` · `returning_customers` · `total_customers` · `new_vs_repeat` · `gateway_repeat` · `order_repeat` · `product_customers` · `repeat_rate` · `cohort_metrics` · `net_active` · `brand_time_to_repeat` · `amazon_metric` · `query_series` · `cohort_retention_table` · `product_ltv_windowed` · `sequenced_cross_sell`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
