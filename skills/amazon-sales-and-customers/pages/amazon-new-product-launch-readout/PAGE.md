---
name: ssi-amazon-new-product-launch-readout
description: >
  Load when you ask how a new Amazon product or listing is doing ("how is the launch going",
  "how is the new one selling", "is the new pack working"), when a product you do not
  recognise appears in a table, or when someone says a product "went live today". Gives the
  six fields a launch readout must carry, separates the day the listing opened from the day
  it first sold, and names the tools whose normal answer is wrong on a product this young.
---

# Read how a new Amazon product launch is going

## Open this page when

- "How is the launch going?" "How is the new one doing?"
- A product id or name appears that you do not recognise.
- Someone says a listing "went live today", or dates a launch from its first sale.
- You are writing the new-product paragraph of a weekly update.
- A product is young enough that stock cover, repeat rate, LTV or conversion would be read
  from a window longer than the product has existed.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-new-product-launch-readout`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `describe_schema` · `run_sql` · `query_series` · `amazon_metric` · `data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
