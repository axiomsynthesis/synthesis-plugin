---
name: ssi-cross-channel-halo-and-incrementality
description: >
  Load when you ask whether Meta, TikTok, creator, influencer or any outside spend lifts
  Amazon sales, retail sales or branded search: "does TikTok sell our product on Amazon", "is
  Meta driving Amazon", "is the extra Meta money paying", "our Amazon visits tripled but
  revenue did not", or any halo, incrementality or cross-channel correlation question. Frames
  the break-even in orders per $1K first, then runs a marginal before-and-after read, a
  controlled estimate with a range, natural experiments with a timing check and placebos, and
  names the pause test that would settle it.
---

# Does outside spend sell on Amazon or another channel?

## Open this page when

- "Does TikTok (or GMV Max, or creators) sell our product on Amazon?"
- "Is Meta driving Amazon sales? Is the extra Meta money paying?"
- "Did the TV / billboard / influencer campaign lift Amazon, retail or brand searches?" (For a
  dated campaign readout, `ssi-campaign-and-event-lift` leads; this skill supplies the
  controlled estimate when spend is visible.)
- "Our Amazon visits tripled but revenue did not. Is the outside traffic worth it?"
- Any request for incrementality, halo, lift or a cross-channel correlation.

Load with it: `ssi-amazon-offsite-attribution` (reading Amazon Attribution itself: no cost
side, 14-day window, true-up), `ssi-brand-search-and-own-name` (brand-search counts),
`ssi-amazon-revenue-basis` (which Amazon revenue and which clock), and
`ssi-challenge-and-premortem` and `ssi-reversibility-and-decision-doors` before a scale or
pause call.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `cross-channel-halo-and-incrementality`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `amazon_metric` · `meta_metric` · `tiktok_metric` · `query_series` · `breakeven_roas` · `describe_schema` · `run_sql` · `measurable_test` · `attribution_lenses` · `capture_turn` · `log_decision`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
