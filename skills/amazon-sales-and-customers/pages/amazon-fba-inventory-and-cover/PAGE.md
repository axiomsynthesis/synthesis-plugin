---
name: ssi-amazon-fba-inventory-and-cover
description: >
  Load for any Amazon stock, FBA inventory, inbound shipment, stock moving between Amazon
  warehouses, days of cover, weeks of supply, stockout risk, reorder, restock, excess or dead
  stock question, or a report's inventory section ("am I about to run out", "how many days of
  stock do I have", "when does it run out with Black Friday", "what if we run a lightning
  deal", "what should I reorder", "what is inbound", "why does this say LOW").
  Reads Amazon's live stock in nine buckets without double counting, and keeps a failed pull
  from reading as zero stock.
---

# Amazon FBA stock and days of cover, without false reorders

## Open this page when

- "Am I about to run out of anything on Amazon?", "what is at risk of stocking out?"
- "How many days (or weeks) of stock do I have?", any days-of-cover or weeks-of-supply read.
- "When does this run out?", with Prime Day, Black Friday / Cyber Monday, a Deal of the Day,
  a Lightning Deal, a launch or an influencer push ahead.
- "What should I reorder, and how much?", "when do I need to place the order?"
- "What is inbound?", "where is shipment X?", "how much is moving between warehouses?"
- "What is sitting in Amazon too long?", excess, overstock, dead stock, storage cost.
- "Why does the report say LOW / CRITICAL?", or the inventory section of any weekly report.
- Before diagnosing any Amazon sales drop: a stockout looks exactly like lost demand.

For how much to order once you know the stockout date (safety stock, reorder point, cover
targets by product role), load the inventory and supply planning skill next.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-fba-inventory-and-cover`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `record_amazon_deal` · `operator_inputs` · `query_series` · `data_freshness` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
