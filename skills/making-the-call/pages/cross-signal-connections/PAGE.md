---
name: ssi-cross-signal-connections
description: >
  Load when you want non-obvious patterns across channels, an "idea of the week", to know
  whether the way your business works has changed, or to test a relationship you believe in
  ("is our model still holding", "find me something we would not have spotted", "does more ad
  spend still buy rank", "does more traffic still buy revenue"). Reports show levels; this
  finds the RATE between two levels that moved while both levels looked fine, proves the
  population behind it did not change, kills the candidates that cannot survive a hunt for a
  duller cause, and caps the week at two or three findings.
---

# Connect two right facts to say what neither says alone

## Open this page when

- "Find something non-obvious", "idea of the week", "what should I be worried about that
  nothing flagged".
- Testing a relationship you already believe: more ad spend buys rank, more traffic buys
  revenue, a price move pays for itself.
- Not for "why did this number go up or down". If the question names a number that already
  moved, explain that move directly. Not for whether one channel's spend lifts another, which
  needs a named spend and a break-even. Not for whether a single series really changed.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `cross-signal-connections`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`query_series` · `data_freshness` · `describe_schema` · `run_sql` · `keyword_rank_tracker` · `measurable_test` · `capture_turn` · `propose_hypothesis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
