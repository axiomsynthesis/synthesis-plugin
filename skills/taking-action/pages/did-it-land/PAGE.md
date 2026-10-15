---
name: ssi-did-it-land
description: >
  Load after the brand has applied a change list and wants to know whether it took effect
  ("did my negatives land", "did the bid cuts go through", "check the upload worked",
  "are those keywords paused now", "did the new exact keywords get created", "what changed
  in my ad account this week", "did someone else change my campaigns"). Confirms each row
  of the list by its own id against the account's daily configuration photo, says plainly
  which rows cannot be confirmed yet and why, and lists changes made outside the list.
---

# Did it land

## Open this page when

- "Did my upload work?", "did the negatives land?", "are the bid cuts live?"
- "Are those keywords paused now?", "did the new exact keywords get created?"
- "What changed in my ad account this week?", "did someone change my campaigns?"
- The day after any change list from `ssi-amazon-block-wasted-searches`,
  `ssi-amazon-bid-trim`, `ssi-amazon-harvest`, `ssi-amazon-budget-release` or
  `ssi-amazon-pause-losers` was applied.

Whether the change *worked* (saved money without losing sales) is a later question, on the
list's `proves_it_wrong` date. Answer it with the skill that built the list. This skill only
answers "is the account now in the state the list described?"

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `did-it-land`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`google_ads_metric` · `meta_metric` · `data_freshness`
`amazon_metric`, with `metric` set to: `ppc_account_changes`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_account_changes` means `amazon_metric` with `metric` set to `ppc_account_changes`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
