---
name: ssi-amazon-ppc-diagnostics
description: >
  Load before diagnosing WHERE your Amazon ad money goes and why a PPC number moved:
  placement splits, keyword and match-type detail, branded versus non-branded, day-of-week
  pattern, paid versus organic share, halo onto other products, parent-product spend,
  portfolio and ad-group rollups, budget cap-outs, invalid traffic, Sponsored Brands
  creatives, the weekly trend and what changed in the account ("is top of search worth it",
  "are we paying for bot clicks", "why did ACoS jump last week", "which portfolio eats the
  budget"). Says which numbers are measured, which are a subtraction, which cover one ad
  product only, and which read as a confident zero when the data is simply absent.
---

# Amazon PPC diagnostics: where the money went, and what the number is not

## Open this page when

- "Where is our ad spend going?" by placement, keyword, weekday, portfolio, ad group,
  parent product or Sponsored Brands creative.
- "Is top of search worth its premium?" / "Should we shift budget by day?" / "Are we paying
  for bot clicks?" / "Are ads incremental or just buying sales we would have had?"
- "Why did ACoS jump last week?": before blaming performance, check what changed in the
  account and whether the week is mature.
- Any weekly PPC trend chart or report section over ad data.
- For search-term waste, harvest and negatives, load `ssi-amazon-ppc-decisions`.
- For the settled money and fee side, load `ssi-amazon-settlement-and-fees`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-ppc-diagnostics`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
