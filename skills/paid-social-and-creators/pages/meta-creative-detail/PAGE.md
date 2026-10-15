---
name: ssi-meta-creative-detail
description: >
  Load before answering any Meta (Facebook and Instagram) question about which AD,
  surface, state, country, age group, gender or device is working ("which creative
  wins on Reels", "which states waste our spend", "who are we reaching", "is this ad
  fatiguing", "which video hooks"), and before writing SQL on a Meta breakdown or
  creative table. Two sets of tables carry these numbers at different grains: the
  per-creative daily tables run to yesterday, while the account-level audience
  tables hold one lifetime row per segment that cannot be trended or windowed. Says
  which table answers which question and the ways a Meta breakdown number comes out
  wrong.
---

# Meta creative detail, read correctly

## Open this page when

- Any per-ad or per-creative Meta read: surface, geography, funnel actions, video,
  fatigue.
- Any Meta audience question: age, gender, placement, device, region, country.
- Before any `run_sql` on a Meta breakdown or creative table.
- For account or campaign level Meta spend, ROAS, CPA and MER, use
  `ssi-meta-ads-reading` or `ssi-meta-delivery-and-pacing` instead. This skill is the
  layer beneath them.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-creative-detail`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
