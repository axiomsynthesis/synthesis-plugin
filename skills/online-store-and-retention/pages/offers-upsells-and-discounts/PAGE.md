---
name: ssi-offers-upsells-and-discounts
description: >
  Load when setting or changing what a website order contains or costs: pack sizes and pack
  prices, free shipping lines, an add-on box, an after-payment upsell, free gifts with
  bigger packs, or discount codes ("should we add a 6-pack", "what should the add-on cost",
  "is free shipping worth it", "set up a post-purchase upsell", "our codes are everywhere",
  "should the code have a minimum", "change the welcome offer"). Works out what each order
  keeps first, prices every option against that and the shipping tiers, and closes discount
  leaks without breaking a promise already made to a customer.
---

# Offers, upsells and codes that make money per order

## Open this page when

- Before adding or repricing a pack, an add-on or a gift.
- Before switching on an after-payment offer.
- When codes show up on many orders, or a code's terms are about to change.
- When cost per sale is above what an order keeps and someone proposes a discount to fix it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `offers-upsells-and-discounts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`shopify_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
