---
name: ssi-inventory-and-supply-planning
description: >
  Load when the question is HOW MUCH to order and WHEN to place the order: "how many units do
  I reorder", "what is my reorder point", "how much safety stock", "what cover should this
  product be held at", "are we going to make Q4", "is Amazon going to cap our storage", or
  "should we keep this product". The stock tools give a run-out date (counting sales and stock on its way) and a quantity to reach
  a target days of cover, with no lead time, minimum order or case pack; this turns them into
  an order, and says plainly which numbers are measured and which are
  playbook anchors nobody has tested on your business.
---

# How much to order, and when to place the order

## Open this page when

- "How many units do I order?", "what is my reorder point?", "how much safety stock?"
- "What cover should this product be held at?" Targets differ by the product's role.
- "Are we going to make Q4?", any pre-build, container or sea-freight timing question.
- "Is Amazon going to cap our storage?" The inventory score and its levers.
- "Should we keep this product?" Range trimming.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `inventory-and-supply-planning`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `query_series` · `operator_inputs` · `score_sku_rationalization`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
