---
name: ssi-retail-combined-exec-summary
description: >
  Load when asked for one weekly summary across two or more retailers ("give me Walmart
  and Target on one page", "an exec summary of the retail week for our head of sales",
  "combine the two retail reports", "make this a one-pager for the broker"). Forces one
  page with each retailer side by side in a fixed set of slots, keeps the detail behind
  it organised by topic rather than one retailer's report after the other, assembles
  every figure from each retailer's own reconciled numbers instead of recomputing them,
  and prints the two different week ends and the shelf-dollar basis every time.
---

# The combined retail week: one page, then the detail by topic

## Open this page when

- One weekly summary across two or more retailers: "put both retailers on one
  page", "an exec summary of the retail week", "combine the two retail reports",
  "make this a one-pager for the broker".

Not this page: a single retailer's week, or the store-sales rules themselves.
This page is only the shape of the combined document and where its figures come
from; open the per-retailer pages first and do not restate them.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `retail-combined-exec-summary`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## No tool of its own

This page is judgment rather than a reader. The method names whatever
tools the question needs.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
