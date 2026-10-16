---
name: ssi-sales-drop-triage
description: >
  Load when sales look wrong TODAY or this week and someone wants to know if something is
  broken ("we haven't had an order in an hour", "is the site broken", "cost per sale jumped
  this morning", "was it our change or Meta", "today looks terrible", "why did yesterday's
  numbers collapse"). Rules out a broken buy path first, then splits cost per sale into
  cost per visitor and visitors who buy, compares the same hours on earlier days, and sets a
  rollback trigger in advance. For a monthly "why did revenue move", load
  `explain-a-metric-move` instead.
---

# Is something broken, or is it a normal bad hour?

## Open this page when

- No orders for an unusual stretch.
- Cost per sale or conversion looks far off partway through a day.
- Right after a change went live (a page, a price, a discount, an ad) and numbers move.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `sales-drop-triage`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `shopify_metric` · `meta_metric` · `funnel_decomposition`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
