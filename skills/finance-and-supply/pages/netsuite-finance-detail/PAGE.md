---
name: ssi-netsuite-finance-detail
description: >
  Load before quoting any accounting-ledger (NetSuite) figure below the top line: supplier
  spend, operating cost by category, discounts and refunds given back, revenue by product
  family, receivables ageing, refund rate, the gross-to-net bridge, GAAP or adjusted EBITDA
  ("what do we spend with our suppliers", "where does our operating cost go", "how much are
  we discounting", "what is our EBITDA", "who owes us money"). Says which of these figures is
  safe to quote as dollars, which is only safe as a shape, and which profit figure reads too
  high in the ledger by design.
---

# NetSuite finance detail, read correctly

## Open this page when

- Any question about supplier spend, operating cost lines, discounts or refunds given back,
  receivables, revenue by product family, or EBITDA.
- Before writing SQL against your `netsuite` dataset's `fact_netsuite_*` tables.
- Before setting an accounting-ledger figure beside an Amazon, Shopify or ads figure.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `netsuite-finance-detail`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`netsuite_metric` · `monthly_pnl` · `describe_schema` · `run_sql` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
