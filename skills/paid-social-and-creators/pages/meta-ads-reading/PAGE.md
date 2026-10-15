---
name: ssi-meta-ads-reading
description: >
  Load before answering any Meta, Facebook or Instagram ads question about spend,
  ROAS, CPA, creatives, hook or hold rate, placement, device, age and gender,
  geography, the funnel or ad spend by product, and before adding up raw Meta ad
  rows by hand ("what's our Meta ROAS this month", "why did Facebook spend drop",
  "which creative should I cut", "Reels or Feed", "which states work", "what did
  this product spend on Meta"). Stops the usual Meta misreads: an inflated sum, two
  ad accounts blended into one line, dead fields read as zero, a return quoted where
  Meta records no sales, and marketplace-bound spend judged on pixel purchases.
---

# Reading your Meta ads data

## Open this page when

- "What's our Meta ROAS / CPA / spend this month?" "Why did Facebook spend drop?"
- "Which creative is winning? What should I cut? Is our hook rate good?"
- "Reels or Feed? iPhone or Android? Which states? What did this product spend?"
- Any time you are about to add up raw Meta ad rows by hand, for example from an
  export.

For the marketplace side of Meta spend, meaning the sales that ads sent to Amazon
actually drove, load `ssi-meta-amazon-attribution-scoring`. This skill only tells
you when to hand off. For hook, hold and fatigue diagnosis in depth, load
`ssi-meta-creative-diagnosis`. For audience, placement and per-creative tables, load
`ssi-meta-creative-detail`. For pacing, reach and saturation, load
`ssi-meta-delivery-and-pacing`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-ads-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric` · `data_freshness` · `mer` · `attribution_lenses` · `media_response_model` · `score_creative_metrics` · `benchmark_metric` · `propose_brand_fact` · `log_decision` · `register_prediction`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
