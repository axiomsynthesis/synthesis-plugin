---
name: ssi-operating-state-tools-retired
description: >
  Load before calling or quoting any of the six state-diagnosis tools
  (diagnose_operating_state, diagnose_state_gated, diagnose_state_map, check_state_transition,
  run_state_formula, apply_growth_investment_override), or whenever a result comes back
  carrying a named state and an ordered list of moves ("what state is my brand in", "what
  should I do given my state", "is this upgrade confirmed", "does the growth override apply
  to us"). The named states and their prescribed moves are no longer how Synthesis describes
  a brand, so they should not go into an answer or a report. This says what each tool
  actually computes, which numbers inside it are still usable, and what to say instead.
---

# The state-diagnosis tools: keep the numbers, leave the names

## Open this page when

- Before calling any of the six tools named above.
- When a result hands you a state label and an ordered response and you are about to put
  either into an answer, a report or a written conclusion.
- For the thing you actually want, how a metric is trending and how to say it, load
  ssi-synthesis-operating-protocol. That is the live ladder.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `operating-state-tools-retired`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`diagnose_operating_state` · `diagnose_state_map` · `run_state_formula` · `diagnose_state_gated` · `apply_growth_investment_override`
`check_reasoning`, with `metric` set to: `state_transition`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_state_transition` means `check_reasoning` with `metric` set to `state_transition`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
