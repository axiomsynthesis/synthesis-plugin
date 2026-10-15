---
name: ssi-brand-context-lenses
description: >
  Load before leaning on your brand's stored archetype, revenue stage, channel
  gravity, seasonality class, market posture or death-mode scores ("what kind of
  brand are we", "what should our repeat rate be", "are we Amazon-dependent",
  "are we seasonal", "which trap are we closest to", "why does Synthesis call
  us a premium consumable"). Says how each label is worked out, which are
  measured, which are an interview answer from months ago, and which are a
  default that reads exactly like a finding.
---

# Read your brand through its lenses, and know which ones are guesses

## Open this page when

- Before quoting or relying on your archetype, stage, channel gravity,
  seasonality, market posture, financial lean or a death-mode score.
- Before quoting a benchmark target (repeat rate, acquisition-cost band,
  lifetime value to acquisition cost, payback months, ad cost of sales) that
  came from the archetype rather than your own numbers.
- When two reads of "how Amazon-dependent are we" disagree.
- For what the archetype changes about the answer (which scoreboard to use),
  load `ssi-archetype-economics-models`.
- For the stored fact list and how to date it, load
  `ssi-ground-in-brand-knowledge`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `brand-context-lenses`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_context_frame` · `market_posture` · `brand_context` · `strategy_framework`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
