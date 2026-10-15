---
name: ssi-retail-store-sales-and-money
description: >
  Load for any read of your weekly store sales at a retailer (Walmart stores, Target or
  any account where the retailer buys from you and sells on its own shelf): "how did
  Walmart do this week", "why is retail down 20% on last year", "which items should we
  grow, fix or exit", "is this pack under its hurdle", "how big is the prize if we win
  the doors back", "what does Walmart actually pay us", "what is our retail margin", "are
  markdowns eating us". Reads store sales against recent weeks first with the store count
  beside them, splits every change into stores, selling rate and price, and never calls
  shelf dollars your revenue or the retailer's margin yours.
---

# Retail store sales, and the three retail dollars

## Open this page when

- Any read of weekly store sales at a retailer that buys from you and sells on its
  own shelf: "how did the account do this week", "why is retail down on last year",
  "which items should we grow, fix or exit", "is this pack under its hurdle".
- What the retailer actually pays you, the retail margin, markdowns, the prize from
  winning doors back.

Not this page: selling as a third-party seller on the retailer's website. That is
a different business and must never be blended with store selling.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `retail-store-sales-and-money`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`describe_schema` · `run_sql` · `operator_inputs` · `search_files` · `read_file`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
