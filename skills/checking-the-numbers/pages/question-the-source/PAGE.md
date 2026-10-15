---
name: ssi-question-the-source
description: >
  Load when a tool comes back empty, blank, refused or "not available", when a
  number looks too low or a chart falls off a cliff, when a deep analysis lost
  some of its analysts, or before you write "we have no X" or "there is no data
  on Y". "Why is this zero?" "Did our email really stop?" "Do we have any
  customer research?" Tells four kinds of nothing apart (missing, real zero,
  partial, failed read), proves the source is complete before calling anything
  absent, and reports failures as failures.
---

# Question the source before you call anything missing

## Open this page when

- A tool comes back with zero rows, a blank, an empty list, or "not available".
- A number looks too low, a chart falls off a cliff, or a channel reads zero.
- You are about to write "the brand has no X", "there is no research on Y",
  "this product has no complaints" or "that data is not in the warehouse".
- A deep analysis finished but one or more analysts did not report back, or it
  routed more analysts than it names in its answer.
- The question asks for a metric you are not sure is connected.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `question-the-source`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `warehouse_freshness` · `warehouse_tables` · `warehouse_row_counts` · `data_freshness_sweep` · `warehouse_table_preview` · `search_files` · `search_file_content` · `list_files` · `read_file` · `declare_not_known`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
