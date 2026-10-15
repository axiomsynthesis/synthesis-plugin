---
name: ssi-walmart-marketplace-reading
description: >
  Load for questions about your own Walmart Marketplace seller account on walmart.com: "how is
  Walmart doing", "what did we sell on Walmart last month", "which SKUs sell on Walmart", "why
  is Walmart so weak", "are our Walmart listings live", "what is our Walmart cancel rate", and
  before writing SQL against your `walmart` dataset. Keeps the seller ledger apart from Walmart
  store sales and from the public walmart.com shelf, states the one revenue basis that never
  ties to a bank deposit, and stops a channel you paused being reported as a broken pipeline.
---

# Read your Walmart Marketplace seller ledger

## Open this page when

- Any "how is Walmart doing" question where Walmart means **your own seller account** on
  walmart.com: revenue, orders, units, average order value, SKU mix, cancel rate, listing
  health.
- Before writing SQL against `walmart`.
- Whenever a Walmart figure is about to sit next to an Amazon, Shopify or accounting figure,
  because the basis is different.

Not this skill: Walmart **store** selling, where Walmart buys from you and sells in its own
stores. That is **ssi-walmart-retail-weekly-files** and **ssi-retail-store-sales-and-money**.
The public walmart.com shelf, where you check rivals' positions and prices, is
**ssi-competitor-shelf-and-price-checks**.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `walmart-marketplace-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`walmart_metric` · `shelf_history` · `scrape_walmart` · `run_sql` · `describe_schema`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
