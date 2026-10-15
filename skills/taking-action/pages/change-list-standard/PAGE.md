---
name: ssi-change-list-standard
description: >
  Load whenever a finding is about to become a list of changes for the brand to make itself:
  "give me the negatives to add", "which ads should I pause", "make me the bulk file",
  "turn this into something I can upload", "what exactly do I change in the ad console",
  "tag these customers", "what should I cut". Defines the one change-list shape every
  action skill hands over: the columns, the summary above the table, the four risk tiers,
  how to write the undo and the "proves it wrong" cells, and the rules that keep a list
  honest (ids or nothing, never lower an evidence bar, could-not-check is not
  nothing-to-change). Every other action skill points here.
---

# The change list: one standard shape

## Open this page when

- Any time a finding is turning into "here is what to change": negatives to add, bids to trim,
  ads or ad sets to pause, budgets to move, customers to tag, a purchase order to adjust.
- Before producing any upload file for Amazon Ads, Seller Central, Google Ads, Meta or Shopify.
- When a brand asks "what exactly do I do with this?" after an analysis.

The platform skills (search terms, bids, budgets, pausing, customer tags) tell you what to
change and why. This skill tells you how to write it down so the brand can check it, apply it,
reverse it, and know later whether it was right.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `change-list-standard`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`export_xlsx`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
