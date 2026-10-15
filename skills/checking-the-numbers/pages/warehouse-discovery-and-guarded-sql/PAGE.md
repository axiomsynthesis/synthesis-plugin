---
name: ssi-warehouse-discovery-and-guarded-sql
description: >
  Load when no metric tool answers the question, when you want a figure pulled
  "straight from the data", when checking whether data is fresh or complete
  ("is this up to date?", "why is this empty?", "did this stop syncing?"), when
  a query tool answers "not available on this connection", or before writing
  SQL for your own connected warehouse. Picks a checked tool first, finds what
  data really exists, keeps hand-written SQL from quietly returning nothing or
  counting a row twice, and treats every hand-pulled figure as unverified until
  it ties to a checked tool.
---

# Find the right data and write SQL that cannot fool you

## Open this page when

- "Can you pull X straight from the data?" and no metric tool covers X.
- "Is this data up to date?" "Why is this empty?" "Did this stop syncing?"
- A tool answers "not available on this connection".
- Before writing SQL for your own warehouse, and before trusting any figure that
  came from one.
- When a checked tool and a hand-pulled figure disagree.
- When you are about to write "we have no data on X".

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `warehouse-discovery-and-guarded-sql`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `query_series` · `gateway_repeat` · `product_ltv_windowed` · `net_revenue` · `net_revenue_dtc` · `meta_metric` · `warehouse_tables` · `warehouse_row_counts` · `warehouse_freshness` · `warehouse_table_preview` · `data_freshness` · `data_freshness_sweep` · `walmart_metric` · `declare_not_known`
`check_reasoning`, with `metric` set to: `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_comparable_basis` means `check_reasoning` with `metric` set to `comparable_basis`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
