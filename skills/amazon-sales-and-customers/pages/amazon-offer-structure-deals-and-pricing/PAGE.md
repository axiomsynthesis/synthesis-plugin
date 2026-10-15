---
name: ssi-amazon-offer-structure-deals-and-pricing
description: >
  Load when your question is about the SHAPE of an Amazon offer rather than one price: a
  single / 2-pack / 3-pack ladder, price per use, whether a list price moved, how deep a deal
  really was, whether a bigger pack covers for a sibling that went out of stock, or what a
  rival's offer looks like ("should we cut the 3-pack", "is our multipack actually cheaper per
  use", "how deep was Prime Day", "did anyone change our price"). Nothing measures pack size
  or list-price history, so this is a hand-built read, and the promotion number will tell you
  a deal never happened.
---

# Amazon offer structure, deals and pricing

## Open this page when

- A pack ladder: pricing, adding, cutting or comparing a single, 2-pack, 3-pack or bundle.
- Price per use, per treatment, per ounce, per serving.
- "Did our price change", "did a deal run", "how deep was the discount".
- Deal or event payback, coupon depth, whether a deal left anything behind.
- Whether a bigger pack picks up demand when the single goes out of stock.
- What a competitor's offer looks like beyond one headline price.

Not this page: whether the Subscribe and Save discount is worth it, whether an
event moved sales against a clean week, which revenue basis to use, or a live
competitor shelf read. Each of those has its own page.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-offer-structure-deals-and-pricing`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `query_series` · `amazon_metric` · `revenue_by_sku` · `ltv_drivers` · `shelf_history` · `price_positioning`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
