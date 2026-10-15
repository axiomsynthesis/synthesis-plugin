---
name: ssi-amazon-budget-release
description: >
  Load when an Amazon ad campaign keeps running out of daily budget and you want to know
  whether to raise it, and by how much ("which campaigns are budget capped", "should I
  raise my budgets", "my campaigns run out of money by lunchtime", "give me a bulksheet of
  budget changes"). Builds a list of budget raises, by campaign id, only for campaigns
  that are both capping and profitable against break-even, and says plainly that the size
  of each raise is a judgement.
---

# Release budget on capped Amazon campaigns

## Open this page when

- "Which campaigns are budget capped?", "should I raise my budgets?"
- "My ads stop by the afternoon", "where would more budget earn its keep?"
- "Make me the bulksheet to raise these budgets."

To stop paying for searches that never sell, use `ssi-amazon-block-wasted-searches`. For
bid changes and judging ACoS by search, use `ssi-amazon-ppc-decisions`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-budget-release`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`export_xlsx`
`amazon_metric`, with `metric` set to: `ppc_budget_utilisation` · `ppc_campaigns` · `ppc_keyword_roi`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_budget_utilisation` means `amazon_metric` with `metric` set to `ppc_budget_utilisation`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
