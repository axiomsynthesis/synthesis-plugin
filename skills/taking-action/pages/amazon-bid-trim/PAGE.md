---
name: ssi-amazon-bid-trim
description: >
  Load when you want a list of Amazon keyword bids to bring down, ready to upload yourself
  ("which bids are too high", "trim my keyword bids", "what should each bid be", "make me a
  bulksheet of bid changes", "which keywords are losing money per click", "cut bids to
  break-even"). Builds one row per Sponsored Products keyword or product target, by Amazon's
  own ids, where the bid sits above what a click can cost before the order it brings loses
  money, judged on that keyword's own ad group break-even and never an account average. Only
  ever suggests a cut, keeps a 20-click evidence floor, and warns when placement or dynamic
  bidding means a lower base bid may not lower the real cost.
---

# Trim Amazon keyword bids to break-even

## Open this page when

- "Which of my bids are too high?", "trim my bids", "what should this keyword bid be?"
- "Make me a bulksheet of bid changes", "turn the bid read into changes I can upload"
- After `ssi-amazon-ppc-decisions` found keywords above break-even and you want the change
  list, not the analysis.

For searches that spend and never sell, use `ssi-amazon-block-wasted-searches`. For giving a
winning search its own exact keyword (which raises spend), use `ssi-amazon-harvest`. For
campaigns that run out of budget, use `ssi-amazon-budget-release`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-bid-trim`. The `doctrine` field of the result is this page's
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
