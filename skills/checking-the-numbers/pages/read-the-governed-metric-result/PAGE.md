---
name: ssi-read-the-governed-metric-result
description: >
  Load the moment a Synthesis tool result lands and before any number from it
  is stated. Use when a result says gated, carries a refusal reason, data
  quality flags or basis labels, comes back empty or as an error, says a feed
  is "not provisioned" or "not connected", or could be cut off, filtered
  wrong, too large to read, or labelled with the wrong coverage ("why does it
  say no data", "is this the full list", "can I trust this number"). Tells you
  what each warning obliges you to say, how to tell "no data" from "data with
  a warning", and how to prove a result is whole before trusting it.
---

# Read a tool result before trusting it

## Open this page when

- A result has `gated: true`, a `refusal_reason`, or any `data_quality_flags`.
- A result carries a basis label: `comparable_basis`, `revenue_basis`,
  `channel_basis`, `customer_settlement`, `provenance_lock`,
  `platform_attribution_scope`, `_data_integrity`, `_source_integrity`.
- A result came back empty, or as an `error`.
- You are about to rely on a list of rows, a filtered read, or a very long
  result.
- A tool says a feed is "not provisioned", "not connected" or "not in this
  warehouse".

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `read-the-governed-metric-result`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`net_revenue` · `query_series` · `amazon_metric` · `data_freshness` · `warehouse_tables` · `tiktok_metric` · `cruva_metric`
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
