---
name: ssi-amazon-profit-tools
description: >
  Load for Amazon profit, net, contribution after product cost, daily or weekly profit
  estimates, new versus repeat customer economics, break-even ACoS or ROAS, or plan versus
  actual ("what did Amazon actually make last month", "are we profitable after ads", "what
  is our break-even ACoS", "how hard can we bid", "are we on plan this month"). Picks the one
  read that ends at net (the Profit page's own figure), defaults to the last settled month,
  refuses a net when costs or ads are missing, and reads the estimate lines as estimates.
---

# Amazon profit: which read ends where

## Open this page when

- "What did Amazon actually make last month?", "what's our net after ads?"
- "Are we profitable on Amazon?", "what is our contribution margin?"
- "Profit by day or week", "did the price change hurt profit?"
- "What does a new customer cost us versus a repeat one?"
- "What is our break-even ACoS / ROAS?", "how hard can we bid?"
- "Are we hitting our target this month?"
- Before putting any Amazon profit, margin or net figure in an answer or report.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-profit-tools`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`business_profit` · `amazon_metric` · `breakeven_roas` · `first_order_contribution_margin` · `operator_inputs` · `monthly_pnl` · `propose_brand_fact` · `log_decision` · `register_prediction`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
