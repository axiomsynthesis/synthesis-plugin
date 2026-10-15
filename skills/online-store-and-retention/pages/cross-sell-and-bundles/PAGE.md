---
name: ssi-cross-sell-and-bundles
description: >
  Load for cross-sell, attach, bundle and upgrade questions: "do buyers of A buy B", "what do
  our buyers buy next", "which product is the front door", "should we bundle these two", "why
  didn't the bundle sell", "how do I get A buyers to buy B", "two cross-sell numbers disagree",
  or any idea for an adjacent product. Names the definition and denominator, reads both
  directions against the base rate, splits same-cart from later buyers, uses a fair window
  when products launched on different dates, then gives the Amazon bundle and ad mechanics and
  how to look past the obvious pairs.
---

# Cross-sell and bundles

## Open this page when

- "Do buyers of A buy B?" "What do our buyers buy next?" "Which product is the front door?"
- "Should we bundle A and B?" "Why did the bundle not sell?"
- "How do I get A buyers to buy B?" "What should we sell them next?"
- Single-pack to multipack upgrade questions.
- "Two cross-sell numbers disagree" or "A to B is 19x stronger than B to A".
- Any adjacent-product or new-pairing idea.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `cross-sell-and-bundles`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `cross_sell` · `sequenced_cross_sell` · `cross_sell_breakdown` · `product_customers` · `subscribe_save_attach_rate` · `amazon_metric` · `shopify_metric` · `find_bridge`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
