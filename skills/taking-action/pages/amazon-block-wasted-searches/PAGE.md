---
name: ssi-amazon-block-wasted-searches
description: >
  Load when you want to turn wasted Amazon ad searches into a list of negative keywords you
  can upload yourself ("which searches should I block", "give me the negatives to add",
  "make me a bulksheet of negative keywords", "stop paying for searches that never sell",
  "clean up my search terms"). Builds one row per search and per ad group or campaign, by
  Amazon's own ids, as negative exact by default, and refuses to call the list checked when
  it cannot see what you have already blocked.
---

# Block wasted Amazon searches

## Open this page when

- "Which searches should I block?", "give me my negatives", "what is wasting ad money?"
- "Make me a bulksheet I can upload", "turn the waste list into changes"
- After a search-term review in `ssi-amazon-ppc-decisions` found zero-order spend and you
  want the change list, not the analysis.

For bid changes, harvesting winners or judging ACoS, use `ssi-amazon-ppc-decisions`. To
free up budget on campaigns that run out of money, use `ssi-amazon-budget-release`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-block-wasted-searches`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`export_xlsx`
`amazon_metric`, with `metric` set to: `ppc_search_terms`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_search_terms` means `amazon_metric` with `metric` set to `ppc_search_terms`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
