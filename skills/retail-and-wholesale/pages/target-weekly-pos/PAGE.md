---
name: ssi-target-weekly-pos
description: >
  Load for any question about your Target store sales or your weekly Target files: "how did
  Target do last week", "what are we selling per store", "how many stores carry us", "why is
  Target down on last year", "is that item leaving the shelf", "are we out of stock at Target",
  "how much of Target was on promotion", or "why didn't my Target report arrive". Keys weeks by
  position, computes from the workbook rather than the PDF chart, uses each item's own store
  count, treats a return as an exit rather than a sale, reads exits from your door counts, and
  shows availability with its level and its direction.
---

# Target weekly POS files: read them without being fooled

## Open this page when

- Any question about Target store sales or the weekly Target files: "how did Target
  do last week", "what are we selling per store", "how many stores carry us", "is
  that item leaving the shelf", "are we out of stock", "how much was on promotion",
  "why did my Target report not arrive".

Only if the brand emails those weekly exports in: Target store sales have no feed
of their own. Open the general store-sales page alongside this one.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `target-weekly-pos`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`run_sql` · `operator_inputs`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
