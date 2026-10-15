---
name: ssi-nielsen-category-scorecard
description: >
  Load for any retail category share, retailer cut, %ACV (share of stores stocking), competitor
  share, velocity or retail trend question from your Nielsen data or the category scorecard
  tool: "where do we sit in the category", "what's our share", "who is passing us", "why is
  Target down", "should we push for more stores", "is distribution leaking", "is the new item
  selling", "is the decline speeding up". Pins the latest delivery, never adds nested windows or
  overlapping markets, keeps shares in points with three decimals, gives opposite advice to the
  two kinds of losing retailer, and makes every label match its number's scope.
---

# Read your Nielsen category scorecard

## Open this page when

- Any retail category share, retailer cut, share of stores stocking, competitor
  share, velocity or retail trend question from a Nielsen delivery.
- "Where do we sit in the category", "what is our share", "who is passing us",
  "should we push for more stores", "is distribution leaking".

Only if a Nielsen delivery is loaded for the brand. If none is, the scorecard
returns nothing, and that means no Nielsen feed rather than no retail sales.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `nielsen-category-scorecard`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`category_scorecard` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
