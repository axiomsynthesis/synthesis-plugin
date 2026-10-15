---
name: ssi-amazon-traffic-and-conversion
description: >
  Load when your Amazon sessions, page views, conversion rate, buy box or sales velocity
  swing, when sessions surge or drop while conversion moves the other way, or when you ask
  whether a traffic change is real ("sessions tripled this week, is that a data problem",
  "why did conversion collapse", "are we losing the buy box", "people visit but do not
  buy", "is this product speeding up"). Runs checks that can fail before calling a swing a
  data error, splits by product and source, judges conversion against your own baseline,
  and checks buy box and stock first when shoppers click and do not buy.
---

# Read Amazon sessions, conversion and buy box, and check a swing

## Open this page when

- "Sessions tripled / halved this week. Is that real or a data problem?"
- "Conversion collapsed." "Why is our conversion so low / so high?"
- Sessions and conversion moving in opposite directions at the same time.
- "Are we losing the buy box?" "Shoppers visit but do not buy."
- "Is this product speeding up or slowing down?" (sales velocity)
- Load alongside: `ssi-data-maturity-and-settling-windows` (how long the traffic feed keeps
  moving), `ssi-amazon-fba-inventory-and-cover` (stock), `ssi-benchmark-grammar` (grading a
  rate), `ssi-amazon-revenue-basis` (which revenue number to quote).

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-traffic-and-conversion`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `amazon_metric` · `query_series` · `meta_metric` · `capture_turn`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
