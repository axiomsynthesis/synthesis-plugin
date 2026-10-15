---
name: ssi-amazon-search-and-competitors
description: >
  Load before quoting any Amazon search share, keyword, share-of-search, branded versus
  non-branded, competitor product, rival click share or search-gap figure ("who is beating us
  on search", "what is our share of search", "which keywords should we attack", "where are
  we not on the shelf", "what else do shoppers buy with our product"). Says which of Amazon's
  two search reports a number came from, stops the two being subtracted from each other,
  fixes the percent-versus-fraction misread that turns invisible into dominant, and keeps a
  competitor answer and a share answer from silently describing different weeks.
---

# Amazon search share and competitors, read correctly

## Open this page when

- Any Amazon search share, keyword, query volume, click share, purchase share or
  share-of-search figure.
- Any "who are our competitors on Amazon" or "who is taking our clicks" question answered
  from your connected data rather than a live scrape.
- Branded versus non-branded demand, brand recall, or "are people searching for us".
- For paid search terms (what your ads actually paid for) load an Amazon PPC skill instead.
  This skill is the organic and marketplace-wide picture.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-search-and-competitors`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`propose_brand_fact`
`amazon_metric`, with `metric` set to: `search_query_performance` · `search_query_trend` · `keyword_opportunities` · `search_competitors` · `search_term_gaps` · `market_basket`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_search_query_performance` means `amazon_metric` with `metric` set to `search_query_performance`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
