---
name: ssi-dtc-and-creator-leftovers
description: >
  Load when you ask how many customers came back to your website, what share of web revenue
  is repeat, how long people take to order again, what your subscription revenue or
  run-rate is on Skio, where site traffic comes from or which page people land on, what
  Google Ads search terms, keywords, Performance Max or paid landing pages are doing, whether
  Google Ads is getting better week to week, or when you want to sort creators or
  influencers into tiers by size. Each of these reads like a finished number and is not one.
---

# Website repeat, Skio subscriptions, Google and creator tiers

## Open this page when

- "How many customers came back to the website last month?"
- "What share of web revenue is repeat?" or "how long until someone orders again?"
- "What is our subscription revenue?" or any monthly recurring figure from Skio.
- "Where is site traffic coming from?" or "which page do people land on?"
- Any Google Ads question about search terms, keywords, Performance Max, paid landing pages
  or whether ads are getting better or worse week to week.
- Before tiering influencers or creators by size.
- For Shopify revenue, orders and AOV, cohort LTV and retention, or creator payouts and
  programme cost, use the skills built for those; this one covers the leftovers.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `dtc-and-creator-leftovers`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`returning_customers_dtc` · `shopify_metric` · `skio_metric` · `ga4_metric` · `google_ads_metric` · `tier_creators`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
