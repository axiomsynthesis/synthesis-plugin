---
name: ssi-amazon-settlement-and-fees
description: >
  Load for Amazon fee rates, net proceeds, settlement tie-out, per-product contribution,
  storage fees, reimbursements, fee anomalies or any settlement-basis figure ("what are my
  Amazon fees", "why did my fee rate jump this month", "what does each product really
  make", "does this tie to the bank", "is Amazon overcharging me"). Drops the part-settled
  month from fee trends, books money to the order month, keeps reserve lines, ad bills and
  fulfilment for other channels out of fee math, reads storage from one posted month, and
  knows a settlement month Amazon has deleted is gone for good.
---

# Amazon settlement, fees and per-product contribution

## Open this page when

- "What are my Amazon fees?", "what is my fee rate?", "why did fees jump this month?"
- "What does Amazon actually pay me?", net proceeds, cash, "does this tie to the bank?"
- "What does each product really make after fees and product cost?"
- Storage fees, reimbursements, "is Amazon overcharging me?", fee anomalies.
- Any figure a tool labels settlement basis.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-settlement-and-fees`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `monthly_pnl` · `propose_brand_fact` · `register_prediction`
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
