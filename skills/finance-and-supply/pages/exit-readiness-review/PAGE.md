---
name: ssi-exit-readiness-review
description: >
  Load when you ask whether the business is ready to sell or raise, what a buyer or banker
  would say about it, how it scores against an exit or acquisition checklist, what to fix
  before going to market, or what the company might be worth ("are we ready to sell", "what
  would a buyer think", "score us against the exit checklist", "what multiple would we
  get", "what should we fix before a process"). Also load before running the valuation and
  exit-readiness tool, which refuses without four key inputs and fills the rest with invented numbers that look measured. Walks a
  banker's six-area readiness checklist, routes each line to the tool that can measure it,
  and says plainly which lines cannot be measured from your data at all.
---

# Exit readiness: measure what you can, name what you cannot

## Open this page when

- "Are we ready to sell?" "What would a buyer think?" "Is this a fundable story?"
- "Score us against the exit checklist." "What do we need to fix before a process?"
- "What's the business worth?" "What multiple would we get?"
- Any request to run `valuation_and_exit_readiness`, before the call is made.
- Diligence prep, a banker conversation, a board deck about a sale or raise.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `exit-readiness-review`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## No tool of its own

This page is judgment rather than a reader. The method names whatever
tools the question needs.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
