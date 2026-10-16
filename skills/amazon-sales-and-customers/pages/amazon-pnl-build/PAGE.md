---
name: ssi-amazon-pnl-build
description: >
  Load when you want an Amazon P&L with Amazon's fees, ad spend and product cost for recent
  months, a "what are we actually keeping per product" view, or a weekly profit ("what did we
  make last week, Monday to Sunday"), or when you are reading the weekly P&L email and want to
  know why a figure is missing. Checks how far back every line reaches before promising a
  window, builds monthly from settlement, reads the weekly from your Profit page's own figures,
  and keeps a product with no cost entered from showing a fake margin.
---

# Build an Amazon P&L, monthly or weekly

## Open this page when

- "Build me a P&L with fees, ads and product cost for the last few months."
- "What are we actually keeping per product?" / "Which products pay?"
- "What did we make last week, Monday to Sunday?"
- "Can we do a 12-month loaded P&L?" (usually not yet; see step 1)
- "Why does the weekly P&L show a dash where profit should be?"

Not for: a single margin or product-cost question, or a fee-rate or payout question on its own.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-pnl-build`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `render_report` · `operator_inputs` · `warehouse_freshness` · `run_sql` · `describe_schema`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
