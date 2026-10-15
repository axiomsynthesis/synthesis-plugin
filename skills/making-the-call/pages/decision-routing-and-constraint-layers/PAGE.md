---
name: ssi-decision-routing-and-constraint-layers
description: >
  Load before deciding how much effort a question deserves, before running a deep
  synthesis on a decision, before calling a decision reversible or one-way, before
  ranking findings by which layer of the business they sit in, before quoting a risk-zone
  alert, and before scoring a pre-mortem ("is this a big decision", "can we undo this",
  "which problem do we fix first", "how exposed are we to Amazon", "what could kill this
  plan"). Four of these five tools only arrange numbers you typed in; the fifth reads your
  data but its zone names promise more than it measures.
---

# Routing a decision, and ranking findings by layer

## Open this page when

- Before running a deep synthesis (`deep_synthesis`, step `start`). It takes minutes, and is
  meant to be used when the stakes check says a question deserves it.
- Before calling a decision "reversible" or "one-way".
- Before ranking a list of findings, or saying one problem outranks another.
- Before quoting any alert level from the four risk zones.
- Before scoring a pre-mortem or a set of failure modes.
- When you are about to say "this question needs the deep treatment". That is the stakes
  check's call, and it is made from words in the question, not from its real importance.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `decision-routing-and-constraint-layers`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`rank_by_constraint_layer`
`strategy_framework`, with `framework` set to: `decision_weight` · `decision_type` · `death_mode_risk_zones` · `premortem_score`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`decision_weight` means `strategy_framework` with `framework` set to `decision_weight`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
