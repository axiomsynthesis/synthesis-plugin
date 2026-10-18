---
name: ssi-customer-and-product-mix
description: >
  Load before answering who the customers are and what actually sells: value segments,
  which states the money comes from, which products carry the window, who to win back,
  how to lift order value, and which products to keep or cut ("where is our revenue
  concentrated", "which customers are worth chasing", "should we kill this SKU", "how do
  we raise AOV", "where do our buyers live", "who is our customer"). Three of these seven
  tools measure nothing: they arrange numbers you type in, and one returns a fixed list of
  rules of thumb that reads exactly like a measurement.
---

# Customer and product mix, read correctly

## Open this page when

- Customer value segments, "who are our best customers", "how much of the base is lapsed".
- Revenue or customers by state or region.
- "Which products carry the month", SKU concentration, Pareto reads, "top 3 = X%".
- Win-back, reactivation, lapsed-customer offers.
- Average order value levers, bundles, volume tiers, free-shipping thresholds.
- SKU rationalisation: keep, fix or cut a product.
- Customer personas: "who is our customer", "build me personas", ad or copy briefs that need
  the buyer's own words.
- For Amazon new-vs-repeat or repeat rate, load ssi-amazon-new-repeat-and-product-customers
  instead.
- Before any product-level read, also load ssi-product-identity-resolution: these tools key on
  ASIN and none of them knows about product ranges.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `customer-and-product-mix`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`rfm_segments` · `geo_performance` · `top_products` · `winback_tiers` · `aov_levers` · `score_sku_rationalization`
`amazon_metric`, with `metric` set to: `customer_personas`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_customer_personas` means `amazon_metric` with `metric` set to `customer_personas`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
