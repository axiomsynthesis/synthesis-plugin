---
name: ssi-amazon-search-share-sqp
description: >
  Load for any Amazon impression, click or purchase share question, keyword performance,
  search funnel gap, head vs tail terms, or any Amazon demand, visibility or acquisition
  conclusion ("what share of searches do we get for this term", "are we losing the shelf",
  "we get shown but nobody clicks", "should we spend more on ads for this keyword", "sales
  are down, is it the category or us"). Reads Amazon's Search Query Performance data the
  right way: shares are already percentages, there is no daily grain, an absent search is
  not zero share, and a share is only comparable over the same set of searches.
---

# Read Amazon search share

## Open this page when

- "What share of searches do we get for (term)?" "Are we winning on (term)?"
- "Is our search position getting better or worse?" "Is demand for our name growing?"
- "Which keywords should we go after for this product?"
- "We get shown but nobody clicks. Why?" "They click but don't buy."
- "Should we spend more on ads for this term?"
- "Sales are down. Is it the category or is it us?"
- Any answer about Amazon acquisition, new customers, demand or visibility. That answer must
  state search share over the same period first (see "What caps results here").

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-search-share-sqp`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `propose_brand_fact` · `register_prediction` · `log_decision`
`amazon_metric`, with `metric` set to: `search_query_trend` · `search_query_performance` · `keyword_opportunities` · `search_term_gaps` · `ppc_keyword_roi`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_search_query_trend` means `amazon_metric` with `metric` set to `search_query_trend`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
