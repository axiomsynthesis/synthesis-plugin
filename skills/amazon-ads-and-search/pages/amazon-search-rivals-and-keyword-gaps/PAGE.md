---
name: ssi-amazon-search-rivals-and-keyword-gaps
description: >
  Load when you ask who is winning a search term on Amazon, which competitors take your
  clicks, which searches you do not show up on, or which keyword opportunities to pursue
  ("who is beating us on this search", "who are our real competitors on Amazon", "where do
  we not show up at all", "should we bid on a competitor's name"). Names the rival products
  on your own searches, splits "never shown" from "shown and not clicked", keeps rival
  brand-name searches out of the main list, and ranks what is winnable.
---

# Who takes the clicks, and where you do not show up

## Open this page when

- "Who is beating us on this search?" or "who are our real competitors on Amazon?"
- "Which searches are we missing?" or "where do we not show up at all?"
- "Which keywords should we go after for this product?"
- "Should we bid on a competitor's name?"
- Someone is about to read a low share on a rival's own brand name as a broken listing.

For your own share of a search over time, and for branded against non-branded demand, use
`ssi-amazon-search-share-sqp` first. This skill adds the one thing that report cannot: the
names of the other sellers.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-search-rivals-and-keyword-gaps`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`compare_to_shelf` · `propose_brand_fact` · `log_decision` · `register_prediction`
`amazon_metric`, with `metric` set to: `search_competitors` · `search_term_gaps` · `keyword_opportunities` · `search_query_performance` · `ppc_keyword_roi`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_search_competitors` means `amazon_metric` with `metric` set to `search_competitors`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
