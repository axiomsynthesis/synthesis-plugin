---
name: ssi-amazon-offsite-attribution
description: >
  Load when asked what Instagram, Meta, TikTok, Google, email, creators or affiliates sold
  on Amazon, whether to renew an influencer or affiliate, why off-Amazon traffic "stopped
  converting", how much of the Amazon business comes from outside Amazon, or how to score
  outside marketing against Amazon sales ("is my Instagram traffic selling on Amazon",
  "should we renew this creator", "what's the return on the Meta money we send to
  Amazon"). Reads Amazon Attribution (clicks, page views, carts, orders and sales for
  traffic that started off Amazon), knows it has no cost side, a 14-day window and a
  true-up period, and says where product names live and how to bring spend in from
  another source.
---

# Read what off-Amazon traffic sold on Amazon

## Open this page when

- "Is my Instagram / Meta / TikTok / Google traffic actually selling on Amazon?"
- "Should we renew this influencer / affiliate / creator?" "Which partners are worth it?"
- "Off-Amazon conversion dropped. Is the channel getting worse?"
- "How much of my Amazon business comes from outside Amazon?"
- "What is the return on the money we send to Amazon from Meta or Google?"
- An unexplained swing in Amazon sessions or conversion that might have an outside cause.
- For how long any number keeps moving after the period closes, see
  `ssi-data-maturity-and-settling-windows`. This skill carries only the attribution rules.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-offsite-attribution`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `meta_metric` · `google_ads_metric` · `tiktok_metric` · `attribution_lenses` · `capture_turn`
`amazon_metric`, with `metric` set to: `attribution_publishers` · `attribution_sources` · `offamazon_share` · `attribution_trueup`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_attribution_publishers` means `amazon_metric` with `metric` set to `attribution_publishers`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
