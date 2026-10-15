---
name: ssi-netsuite-pnl-reading
description: >
  Load for any company-level P&L, gross margin, EBITDA, net income, operating cost,
  year-over-year, channel mix, receivables, supplier spend, working capital or runway
  question from your accounting ledger (NetSuite) or the monthly P&L report ("what did we
  make last month", "is margin improving", "are we growing year on year", "what is our
  EBITDA", "how much runway do we have", "what share of the company is Amazon"). Reads the
  closed month-end books first, labels every other month as an estimate, spots missing
  product cost, refuses a year-over-year without two closed months, and says what the
  ledger cannot answer.
---

# Read your NetSuite P&L without false profit or false growth

## Open this page when

- "What did we make last month?" "What is our gross margin / EBITDA / net income?"
- "Is margin improving?" "Are we growing year on year?" "What is our run-rate?"
- "Where is the operating money going?" "Which retail accounts are growing?"
- "How much do we give back in discounts and refunds?" "Who are our biggest suppliers?"
- "What is our cash / working capital / runway / receivables?"
- "What share of the company is Amazon?" (the whole-company split, not Amazon vs website)
- Any time a P&L figure from the monthly P&L report, a deck or a memo is about to be quoted.

Not for Amazon-only money questions: those go to `ssi-amazon-revenue-basis`. For which
revenue figure covers which scope, see `ssi-metric-definitions-and-citation`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `netsuite-pnl-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`monthly_pnl` · `netsuite_metric` · `channel_revenue_mix` · `product_family_pnl` · `customer_concentration` · `working_capital` · `net_revenue` · `describe_schema` · `run_sql` · `propose_brand_fact` · `register_prediction`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
