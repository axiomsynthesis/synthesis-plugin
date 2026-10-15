---
name: ssi-meta-budget-advice
description: >
  Load when you want advice on Meta ad spend: "what should we do with our Meta
  budget this week", "should we cut or scale Meta", "where should the money go",
  "why does the account keep losing money when some ads clearly work", or when you
  are reading the advice section of a weekly Meta report. Reads how the account was
  bought over several weeks (streaks, money moved into losing ads, the reclaimable
  share, an ad that really scaled, where total spend should land) instead of one
  week's snapshot, and refuses to invent a pattern that is not there.
---

# Meta budget advice from several weeks of behaviour

## Open this page when

- "What should we do with Meta spend this week?" "Should we cut Meta?" "Where should the budget go?"
- Reading or writing the advice or "short version" block of a weekly Meta report.
- "Why does the account keep losing money even though some ads clearly work?"

Do not load it for creative questions (hook, hold, fatigue) or for scoring one ad's
Amazon return. Those belong to `ssi-meta-creative-diagnosis` and
`ssi-meta-amazon-attribution-scoring`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-budget-advice`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `meta_metric` · `amazon_metric` · `gsheets_metric` · `check_reasoning` · `register_prediction` · `brand_facts` · `brand_context` · `product_ltv_windowed` · `shopify_metric` · `capture_turn` · `log_decision`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
