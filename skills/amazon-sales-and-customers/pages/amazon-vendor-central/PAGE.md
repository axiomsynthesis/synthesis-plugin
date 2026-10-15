---
name: ssi-amazon-vendor-central
description: >
  Load for any Amazon Vendor Central (1P) question: a brand that sells to Amazon wholesale
  on purchase orders, where Amazon owns the stock and sets the price ("what did Amazon buy
  from us", "what is our fill rate", "which POs are open", "how much of our stock does Amazon
  hold", "what is Amazon forecasting", "why is Amazon asking for margin support"). Keeps
  wholesale revenue apart from seller sales and from shoppers' spend.
---

# Amazon Vendor Central on the right basis

## Open this page when

- Any vendor, 1P, Vendor Central, purchase order, fill rate or "Amazon bought" question.
- Stock that Amazon owns, Amazon's demand forecast, or Amazon's margin on a product.
- A brand that is both a seller and a vendor, before adding any two Amazon figures.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-vendor-central`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
