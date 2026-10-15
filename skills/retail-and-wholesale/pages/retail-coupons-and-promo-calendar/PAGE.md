---
name: ssi-retail-coupons-and-promo-calendar
description: >
  Load for any cash-back app, digital clip coupon or retail offer question: is it
  working, what is the return on spend, what is break-even, how big should the next offer
  be, or is an offer live this week ("is iBotta paying for itself", "what did the Target
  clip coupon do", "should we run the small pack and the big pack offers together", "is
  there an offer on right now", "is our coupon eating our margin"). Prices each offer
  against the incrementality it must reach on fully loaded cost with the platform fee
  included, brackets each offer against clean weeks before and after, keeps solo and
  overlapping offers apart, and decides "live" only from start and end dates.
---

# Retail coupons and the promo calendar

## Open this page when

- Any cash-back app, digital clip coupon or retail offer question: is it working,
  what is the return on the spend, what is break-even, how big should the next one
  be, is an offer live this week, is the coupon eating the margin.
- Two offers running at the same time, or an offer next to a clean week.

Open the store-sales page first: this one depends on the three retail dollars and
does not repeat them.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `retail-coupons-and-promo-calendar`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`operator_inputs` · `gsheets_metric` · `search_files` · `list_files` · `read_file` · `search_file_content` · `ingest_file` · `describe_schema` · `run_sql` · `category_scorecard` · `register_prediction` · `log_decision` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
