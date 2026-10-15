---
name: ssi-amazon-harvest
description: >
  Load when you want to give Amazon searches that already sell their own exact-match
  keywords, as a list you upload yourself ("harvest my winning search terms", "which
  searches should become exact keywords", "promote converting searches to exact", "make me
  a bulksheet of new keywords", "where should this keyword go and what should I bid").
  Builds one new exact keyword per proven search, placed in an ad group the search already
  sold in, at the starting bid the read computes (what the search actually paid, capped at
  that ad group's break-even), paired with the negative that stops the old place bidding
  against it. This list raises spend; every keyword row is the brand's call.
---

# Harvest winning Amazon searches into exact keywords

## Open this page when

- "Which searches should I harvest?", "promote my winners to exact", "what new keywords
  should I add?"
- "Make me a bulksheet of new exact keywords", "where does this keyword go and at what bid?"
- After `ssi-amazon-ppc-decisions` found proven searches with no exact keyword and you want
  the change list, not the analysis.

For searches that spend and never sell, use `ssi-amazon-block-wasted-searches`. For bids that
are too high, use `ssi-amazon-bid-trim`. For campaigns out of budget, use
`ssi-amazon-budget-release`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-harvest`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `export_xlsx`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
