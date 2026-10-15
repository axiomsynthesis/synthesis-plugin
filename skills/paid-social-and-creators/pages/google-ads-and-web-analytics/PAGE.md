---
name: ssi-google-ads-and-web-analytics
description: >
  Load before quoting any Google Ads cost, keyword, search-term, Performance Max or impression
  share figure, any organic search or SEO figure from Search Console, any site sessions or
  on-site behaviour figure from GA4, or Amazon ad invalid traffic and "what did the ad click
  actually sell" ("what did we spend on Google", "which search terms bring traffic", "did our
  rankings drop", "how many sessions did the site get", "is our paid traffic real"). Says how
  short each history really is, which numbers must never be added together, and how to read
  each report without mistaking a floor for a total.
---

# Google Ads, GA4, Search Console and Amazon ad quality

## Open this page when

- Any Google Ads spend, cost, click, keyword, campaign or return figure.
- Any organic search, SEO, ranking or search-term question.
- Any site sessions, users, channel-mix or on-site behaviour question.
- Amazon ad invalid traffic, or which products an ad click actually sold.
- Before any `run_sql` against the `google_ads`, `ga4`, `search_console` or `amazon_ads`
  datasets.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `google-ads-and-web-analytics`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`google_ads_metric` · `search_console_organic` · `ga4_metric` · `amazon_metric` · `describe_schema` · `run_sql` · `data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
