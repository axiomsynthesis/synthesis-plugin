---
name: ssi-product-cost-resolution
description: >
  Load for any margin, contribution, profit-after-ads or unit-economics answer, when you
  have just entered or changed a product cost, when a cost looks wrong or shows $0, or
  when a product looks unusually profitable or unprofitable ("what is my margin on the
  3-pack", "which products make money", "that cost is wrong", "why does this show 100%
  margin", "I just added my costs, are they picked up?"). Checks which cost attached to
  which product on which channel, treats a missing cost as no margin, and runs the bundle,
  pack-size and SKU-name sanity tests.
---

# Product cost resolution and sanity checks

## Open this page when

- "What is my margin on X?", "which products make money?", "profit after ads", "unit
  economics", "contribution", "break-even ACoS" (ACoS is ad spend as a share of ad sales).
- A tool shows $0 product cost, 100% margin, or a margin that jumped or fell overnight.
- You think a cost is wrong, or a cost was just entered or changed.
- Not for retail store margin (Walmart stores, Target), which needs a fully loaded cost and
  the retailer's own price to you.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `product-cost-resolution`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `operator_inputs` · `find_product` · `breakeven_roas` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
