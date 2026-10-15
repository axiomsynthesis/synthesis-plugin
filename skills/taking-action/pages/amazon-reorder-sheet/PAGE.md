---
name: ssi-amazon-reorder-sheet
description: >
  Load when you want a reorder list you can send to a supplier, not just a stock warning:
  "what should I reorder and how much", "build me a PO sheet", "which products do I need to
  order this week", "give me reorder quantities for 90 days of cover", "when is the last day I
  can order before we run out on Amazon". Turns the restock plan into a per-product order
  sheet with ASIN and SKU, net of stock Amazon is already moving between its own warehouses,
  adjusted for your lead time, minimum order and case pack, with the places the quantity can
  be wrong said out loud.
---

# Build an Amazon reorder sheet

## Open this page when

- "What do I need to reorder?", "build a PO", "reorder sheet", "how much should I order".
- A stock warning (LOW or CRITICAL cover) and the next question is what to order.
- Planning a buy ahead of a known sales event, where you need cover through it.

For whether stock is really low, or how to read reserved and inbound stock, the inventory
reading skill (`ssi-amazon-fba-inventory-and-cover`) goes deeper. This one turns the answer into
an order.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-reorder-sheet`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`operator_inputs` · `amazon_metric` · `export_xlsx`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
