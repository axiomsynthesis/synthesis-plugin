---
name: ssi-amazon-pause-losers
description: >
  Load when you want to stop ads that keep losing money ("which campaigns should I pause",
  "what ad groups are losing money", "which keywords should I turn off", "kill the losers",
  "which Meta ads should I pause", "make me a file to pause these"). Finds Amazon
  campaigns, ad groups, keywords and product targets that lose money against their OWN ad
  group's break-even over two fully credited windows, plus Meta campaigns, ad sets and ads,
  all by id. Prefers a bid cut or a budget cap where the evidence supports one, treats every
  pause as the brand's call, and stops rather than guess a Meta parent or trust a pixel that
  cannot see marketplace sales.
---

# Pause the ads that keep losing money

## Open this page when

- "Which campaigns, ad groups or keywords should I pause?", "what is losing money?"
- "Which Meta ads or ad sets should I turn off?"
- "Make me a bulksheet or import file to pause these."

For keywords that sell but cost too much per click, use `ssi-amazon-bid-trim`. For searches
that spend and never sell, use `ssi-amazon-block-wasted-searches`. For budgets, use
`ssi-amazon-budget-release`. For whether a pause is easy to walk back, use
`ssi-reversibility-and-decision-doors`. The shared columns are in `ssi-change-list-standard`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-pause-losers`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric` · `export_xlsx`
`amazon_metric`, with `metric` set to: `ppc_keyword_bids` · `ppc_campaigns` · `ppc_account_changes`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_keyword_bids` means `amazon_metric` with `metric` set to `ppc_keyword_bids`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
