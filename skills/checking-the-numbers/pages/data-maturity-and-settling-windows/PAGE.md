---
name: ssi-data-maturity-and-settling-windows
description: >
  Load before any week-over-week, month-over-month, year-over-year, "latest week",
  "this month so far" or recent-period comparison, or before quoting a fresh figure
  from any source ("why did sales drop this week", "what happened yesterday", "how
  is this month tracking", "is this our lowest month", "did the campaign work"
  asked a few days after it ended). Covers Amazon orders, ads, off-Amazon
  attribution, traffic, search reports, Subscribe and Save, settlement and stock,
  plus the online store, Meta and the accounting system: each source's settling
  clock, what restates after it looks final, what is lost for good if missed, and
  how to compare two periods fairly.
---

# Know which numbers are still moving before comparing periods

## Open this page when

- "Why did sales drop this week?" "How are we doing vs last week / last month / last year?"
- "What happened yesterday?" "How is this month tracking?"
- "Is this the lowest month yet?" "Did the campaign work?" asked a few days after it ended.
- Any report or answer that leans on the most recent week, month or day.
- A number that looks the same as last week's, or a period that looks short or empty.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `data-maturity-and-settling-windows`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `warehouse_freshness` · `data_freshness_sweep` · `mtd_comparison` · `yoy_comparison` · `query_series` · `monthly_projection` · `amazon_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
