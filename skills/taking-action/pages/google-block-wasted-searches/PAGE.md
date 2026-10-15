---
name: ssi-google-block-wasted-searches
description: >
  Load when you want to turn wasted Google Ads searches into negative keywords you add
  yourself ("which Google searches should I block", "give me negatives for Google Ads",
  "stop paying Google for searches that never convert", "make me a Google Ads Editor file of
  negatives", "clean up my Google search terms"). Builds one row per search and per campaign
  or ad group it ran in, with the account, campaign and ad group ids and the names Google Ads
  Editor matches on, leaves out places already blocked, and stops plainly when the search-term
  data is not there to check.
---

# Block wasted Google searches

## Open this page when

- "Which Google searches should I block?", "give me my Google negatives", "what search
  terms are wasting Google money?"
- "Make me something I can paste into Google Ads Editor."
- After a Google Ads review in `ssi-google-ads-and-web-analytics` found zero-conversion
  search spend and you want the change list, not the analysis.

For Amazon searches use `ssi-amazon-block-wasted-searches`. For how the change list is laid
out, the risk tiers and the undo cells, see `ssi-change-list-standard`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `google-block-wasted-searches`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`google_ads_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
