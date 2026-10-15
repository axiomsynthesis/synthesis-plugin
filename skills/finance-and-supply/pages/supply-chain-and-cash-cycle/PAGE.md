---
name: ssi-supply-chain-and-cash-cycle
description: >
  Load before scoring or ranking a supplier, choosing between Amazon fulfilment and a
  third-party warehouse, or quoting a cash conversion cycle ("is this supplier any good",
  "rank my suppliers", "should we move to a 3PL", "how long is our cash tied up", "is 95
  days bad"). All four of these tools are arithmetic on numbers you type in. None of them
  reads your data, none of them can fail, and every one returns a confident tier or colour
  band even when every input was a guess. This says where each number must come from first.
---

# Suppliers, fulfilment and the cash cycle

## Open this page when

- Any supplier question: score one, rank several, decide who to move volume to.
- Any fulfilment question: Amazon's own warehouses versus a third-party warehouse, or both.
- Any cash conversion cycle, cash-tied-up, days-of-inventory or payment-terms question.
- Before putting any of these tiers or bands in a report or a written answer.
- For stock cover and reorder timing, load ssi-amazon-fba-inventory-and-cover instead; this
  skill only consumes a days-of-stock figure, it does not produce one.
- For the supplier-cost side of margin, load ssi-product-cost-resolution.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `supply-chain-and-cash-cycle`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`operator_inputs` · `working_capital` · `score_supplier` · `tier_suppliers` · `decide_fulfillment` · `ccc_health`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
