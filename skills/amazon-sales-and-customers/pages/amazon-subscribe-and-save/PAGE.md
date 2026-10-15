---
name: ssi-amazon-subscribe-and-save
description: >
  Load for any Amazon Subscribe and Save question: active subscribers, attach rate, S&S
  revenue or forecast, never-repeated ("fake") signups, the retention ladder, subscriber vs
  non-subscriber value, or S&S offer design ("how many subscribers do we have", "is S&S
  growing", "are our subscriptions real", "should we raise the S&S discount", "why did S&S
  revenue fall off a cliff last week"). Checks subscriber counts against Amazon's own monthly
  program figure, reads only settled weeks, judges repeat only on mature subscribers, and keeps
  attach rate on orders, never revenue.
---

# Amazon Subscribe and Save, read without double counting

## Open this page when

- Any count of Subscribe and Save (S&S) subscribers or subscriptions, weekly or monthly.
- S&S attach rate (the share of orders placed as S&S), for one product or the brand.
- S&S revenue, Amazon's S&S forecast, or S&S in a weekly or brand report section.
- "Fake" subscriptions: people who took the S&S discount once and never got a second delivery.
- The S&S retention ladder or cohorts, or subscriber vs non-subscriber value.
- Offer design: discount level, bundles, "subscribe to both".

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-subscribe-and-save`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `subscribe_save_attach_rate` · `query_series` · `sns_cohorts` · `subscription_economics` · `repeat_rate` · `cohort_ltv_table`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
