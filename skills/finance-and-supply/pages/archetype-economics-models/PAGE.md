---
name: ssi-archetype-economics-models
description: >
  Load before answering a lifetime value, retention, repeat, payback, first-order
  margin or acquisition-cost question where how often people rebuy decides what
  "good" means ("is our repeat rate bad", "why is retention so low", "can we lose
  money on the first order", "should we run a win-back", "should we push
  subscriptions"). Says which single number is the scoreboard for a brand that is
  rebought, one that is bought once and one that is both, which figures to stop
  showing for a once-bought brand, and why a stored label is not proof anything
  was measured.
---

# Pick the purchase model before you pick the number

## Open this page when

- "Is our repeat rate bad?" "Why is retention so low?" "What is a customer
  worth?"
- "Can we lose money on the first order?" "What should payback be?"
- "Should we run a win-back campaign?" "Should we push subscriptions?"
- Before showing a retention curve, a cohort grid or a lifetime value to
  acquisition cost ratio for a brand whose purchase model you have not checked.
- Any report section that quotes a target repeat rate, a payback period or a
  margin floor.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `archetype-economics-models`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_context_frame`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
