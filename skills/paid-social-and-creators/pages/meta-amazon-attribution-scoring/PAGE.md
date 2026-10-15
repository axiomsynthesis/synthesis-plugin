---
name: ssi-meta-amazon-attribution-scoring
description: >
  Load for any Meta ROI, ROAS, cost per order or "which Meta ads should I cut"
  question when your Meta ads send shoppers to an Amazon or other marketplace
  listing, or whenever Meta shows almost no purchases against real spend ("is Meta
  working for Amazon", "Ads Manager says zero purchases but Amazon sales are fine",
  "should I check my pixel", "which ads should I turn off"). Scores those ads on the
  marketplace sales Amazon Attribution credits to them: joins each ad to its
  attribution link, scopes the program, nets the Brand Referral Bonus, and tells a
  tracking gap from plain lag.
---

# Score marketplace-bound Meta ads on marketplace sales

## Open this page when

- "Is Meta working?", "what is our Meta ROAS?", "which Meta ads should I turn off?" for a brand that sells mostly on Amazon.
- Meta Ads Manager shows almost no purchases, yet spend is large and Amazon sales look fine.
- Someone is about to say "check your pixel".
- For hook, hold and fatigue, use `ssi-meta-creative-diagnosis`. This skill replaces only the "what happened after the click" part.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-amazon-attribution-scoring`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `meta_metric` · `gsheets_metric` · `amazon_metric` · `register_prediction` · `log_decision`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
