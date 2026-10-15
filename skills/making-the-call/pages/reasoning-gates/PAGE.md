---
name: ssi-reasoning-gates
description: >
  Load before acting on any recommendation, "we should" claim, strategy call or
  rule of thumb about your brand, and before quoting a verdict from any of the
  challenge tools: "is this actually true for us", "what is the case against",
  "what is really holding us back", "would this have worked before", "what
  could kill this", "do deal buyers really repeat worse". Only one of these
  gates reads your brand's own history. The rest score numbers typed into them,
  so they hand back a confident verdict on invented inputs unless every number
  is sourced first.
---

# Reasoning gates: what challenges an answer before it ships

## Open this page when

- Before any recommendation, "you should", kill or scale call, or stated rule about how your
  brand works.
- Before quoting a HELD / REJECT / CRITICAL / DEGRADING verdict from any gate below.
- When someone states a law about the brand ("deal buyers repeat worse") that has never been
  tested against the brand's own past.
- Not for arithmetic or comparability checks. For arithmetic, re-derive each figure yourself
  from the governed metric tools; for comparability, use `check_reasoning` with `metric`
  `comparable_basis`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `reasoning-gates`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`backtest_rule` · `strategy_framework` · `check_reasoning` · `classify_constraint_layer`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
