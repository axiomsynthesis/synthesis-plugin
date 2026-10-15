---
name: ssi-amazon-weekly-expert-report
description: >
  Load when you ask about your weekly Amazon report: what a section means ("what is 'who took
  the clicks'", "is that click-through rate"), why a number looks wrong or looks the same as
  last week, why a product is flagged for reorder, why the customer number is marked
  provisional, whether this week's report can be trusted or forwarded, or when it arrives.
  Carries the eight sections in order and the parts inside them, the reading rule for each,
  which parts run behind by design, the checks to make before trusting it, and the
  misreadings to avoid.
---

# Your weekly Amazon report

## Open this page when

- "What does 'Who took the clicks' in my Amazon report mean?" / "Is that click-through rate?"
- "This number looks wrong" / "This search number is the same as last week."
- "Why does the report say a product needs reordering?"
- "Why is the customer number marked provisional?"
- "When does the Amazon report come? Can I have this week's now?"
- Reviewing an Amazon weekly before trusting or forwarding it.

Not for: the general weekly revenue report (a different, shorter report, see Traps), or a
one-off Amazon question with no report in view (load the matching reading skill).

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-weekly-expert-report`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `query_series` · `new_vs_repeat` · `amazon_metric` · `ltv_drivers` · `brand_time_to_repeat`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
