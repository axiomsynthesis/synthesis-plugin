---
name: ssi-deal-events-in-trends-and-projections
description: >
  Load when a month, week or year-over-year window contains or sits beside a deal
  event such as Prime Day, Prime Big Deal Days, the Amazon Spring Sale, Black Friday
  and Cyber Monday, or your own sale ("what will this month land at", "why is this
  week five times normal", "are we down against last year", "when was Prime Day",
  "did the deal bring in worse customers"). These events move between years, so a
  run rate blends a ten-times day into a meaningless average and a calendar
  year-ago line compares a peak week with an ordinary one. Says how to find the
  real event window, how the projection handles an event, and which reads are
  safe inside one.
---

# Deal events in trends and projections

## Open this page when

- Any month projection, weekly trend, year-over-year read or "is this real" question
  whose window touches a deal event.
- Before writing a date for any deal event into an answer, a chart label or a report.
- Before reading a deal cohort's later behaviour as better or worse than a normal
  cohort.

Whether two windows are comparable at all is covered in ssi-compare-like-with-like.
How fresh the newest days are is covered in ssi-data-maturity-and-settling-windows.
This skill carries the part neither does: the event dates, how to find them, and
what it costs when they are wrong.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `deal-events-in-trends-and-projections`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`monthly_projection` · `amazon_metric` · `brand_facts` · `backtest_rule`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
