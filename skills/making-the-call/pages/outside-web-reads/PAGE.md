---
name: ssi-outside-web-reads
description: >
  Load before reading anything from outside your own data: a web search, a competitor or
  news page, public mentions of a topic, a theme map over review text, or where a product
  ranks on the live Amazon shelf ("what are people saying about this ingredient", "read this
  competitor's page", "where do we rank for our main keyword", "what do the reviews say").
  Two of these spend a shared metered allowance that the weekly shelf snapshot depends on,
  so they are stop-and-ask, never a loop. All of them return third-party text that must be
  cited as outside and unverified, and never mixed into a measured number.
---

# Outside web reads

## Open this page when

- Any web search, page fetch, public-mention read or live-shelf rank check.
- Any question about what the market, the press, Reddit or YouTube is saying.
- Any theme or sentiment read over review text.
- Before putting an outside figure (a competitor price, a claimed market size, a rank) next
  to one of your own numbers in a report.
- For the full live shelf, prices and competitor set, the scraping tools
  (`scrape_amazon_search`, `scrape_amazon_product`, `compare_to_shelf`, `scrape_walmart`,
  `scrape_google_shopping`) belong with competitor-shelf work. Only the rank tracker is here.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `outside-web-reads`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`web_search` · `web_fetch` · `social_listening` · `reddit_mentions` · `keyword_rank_tracker` · `review_themes`
`amazon_metric`, with `metric` set to: `organic_rank`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_organic_rank` means `amazon_metric` with `metric` set to `organic_rank`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
