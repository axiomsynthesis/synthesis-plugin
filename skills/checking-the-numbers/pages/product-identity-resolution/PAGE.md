---
name: ssi-product-identity-resolution
description: >
  Load whenever you ask about a product, a pack size, a bundle, a range or family, or an
  item code, or want products grouped ("how is the 9-pack doing", "compare the single and
  the 2-pack", "what does this range earn", "what is B0... ?"). Works out which product the
  words mean before any number is pulled, keeps every figure at product or family scope,
  and stops a whole-brand figure from being printed under a product's name.
---

# Resolve which product a name means, and keep numbers at product scope

## Open this page when

- A question names a product: "How is the 9-pack doing?" "Is the new formula working?"
- A question names a pack size or a bundle: "the 2-pack", "the duo set", "the 21-count".
- A question groups products: "What does the range earn?" "Roll it up by family."
- A question or a draft carries a bare item code.
- Before writing any per-product table, deck line or report section.
- A number looks too big for the product it is printed under.

**Exception.** When you ask for deep synthesis (any wording with the word "deep"), do not
resolve the product first. The deep analysis is the first and only call, and it resolves
the product itself.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `product-identity-resolution`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `query_series` · `gateway_repeat` · `product_ltv_windowed` · `revenue_by_sku` · `product_customers` · `cross_sell` · `sequenced_cross_sell` · `product_family_pnl` · `meta_metric` · `amazon_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
