---
name: ssi-amazon-customer-identity-and-counts
description: >
  Load before quoting any Amazon customer count, new vs returning split, orders or revenue
  per customer, cost per new customer, cohort, repeat, LTV or "bought both" figure, or before
  planning to match Amazon buyers to Meta, Google, TikTok or a customer data platform ("how
  many customers did we have last month", "customers dropped 60% but revenue is flat, why",
  "what is our CAC on Amazon", "can we send Amazon buyers to Meta as an audience"). Amazon
  identifies a buyer only by a relay email that arrives late and can be missing for whole
  months, so every customer number starts with an email-coverage check.
---

# Count Amazon customers without the buyer-email traps

## Open this page when

- "How many customers did we have last month?" "How many were new?"
- "Our customers dropped 60% but revenue is flat. Why?"
- "What is orders per customer, revenue per customer, or CAC (what it costs to win one new
  customer) this week?"
- "What is our repeat rate, cohort retention or LTV (lifetime value: what a customer spends
  over time) on Amazon?"
- "How many people bought both of these products?"
- "Can we send Amazon buyers to Meta as a custom audience or a conversion?"
- Any week-over-week or year-over-year comparison that has "customers" in it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-customer-identity-and-counts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`total_customers` · `new_to_brand_customers` · `returning_customers` · `query_series` · `new_vs_repeat` · `amazon_metric` · `data_freshness` · `cross_sell` · `cross_sell_breakdown`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
