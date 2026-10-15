---
name: ssi-tiktok-shop-sales-and-payouts
description: >
  Load for any TikTok Shop question: "how is TikTok Shop doing", "what did we sell on TikTok
  last month", "which products sell on TikTok", "what did TikTok actually pay us", "why is
  the payout so far below sales", "did TikTok raise its fees", returns and refunds, shop
  traffic, conversion or the shop health score, "am I about to run out of stock on TikTok", and "should we put more into TikTok Shop".
  Sets the sales basis, removes free creator samples for the period asked, keeps payout
  apart from sales, splits a payout drop into warehouse fees, shipping and commission, reads
  returns by reason, and never adds ad-platform or creator GMV on top of shop sales.
---

# TikTok Shop sales, payouts, returns and shop health

## Open this page when

- "How is TikTok Shop doing?", "what did we sell on TikTok last month?", AOV, orders, units.
- "Which products sell on TikTok?", "how concentrated is the shop?"
- "What did TikTok pay us?", "why is the payout half of sales?", "did TikTok raise fees?"
- Returns, refunds, "is the product the problem?"
- Shop traffic, visitors, conversion, GMV by video, product card or LIVE, the health score.
- Any time a TikTok ads figure (GMV Max) or a creator-platform figure sits beside shop sales.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `tiktok-shop-sales-and-payouts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`tiktok_metric` · `describe_schema` · `run_sql` · `data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
