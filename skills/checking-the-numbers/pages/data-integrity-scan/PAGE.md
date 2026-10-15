---
name: ssi-data-integrity-scan
description: >
  Load after pulling data and again on the draft, before any conclusion, and
  whenever two metrics disagree ("orders are down but customers are up", "why
  does this not match my dashboard?", "is this drop real?"). Walks every number
  along the path it travels, from the day it lands to the advice built on it,
  and stops at each point where a wrong answer is known to slip through: data
  still landing, a partial product set, unlike periods, totals that do not tie,
  a baseline reset, a cause read off a chart, advice aimed at the wrong
  problem, and findings that never reached the draft.
---

# Data integrity scan

## Open this page when

- Right after the pulls, before any judgment is formed.
- Again on the finished draft, before it goes to the reader.
- Whenever two metrics seem to disagree ("orders are down but customers are up").
- Whenever a number looks too good, too bad, or too round.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `data-integrity-scan`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `warehouse_freshness` · `data_freshness_sweep` · `find_product` · `check_reasoning` · `query_series` · `strategy_framework` · `declare_not_known`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
