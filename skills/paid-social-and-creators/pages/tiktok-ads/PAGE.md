---
name: ssi-tiktok-ads
description: >
  Load before quoting any TikTok advertising figure or writing SQL on the TikTok ads tables
  ("what did we spend on TikTok", "what is our TikTok ROAS", "which TikTok campaign is
  working", "is our TikTok creative burning out", "who are we reaching on TikTok", "did
  TikTok spend fall"). TikTok reports spend in two places that do not overlap, auction ads
  and shop ads (GMV Max), and reading one alone gives a real number that is not your TikTok
  spend. Names what each table covers, which grain exists for which surface, and which
  spans are too thin to carry an answer.
---

# TikTok ads, read correctly

## Open this page when

- Any TikTok spend, ROAS, campaign, creative, audience or ad-account question.
- Before any `run_sql` on the `tiktok_ads` dataset.
- Before saying TikTok is small, has shrunk, or has stopped.
- Not for TikTok **Shop** orders, payouts, returns or shop health on their own: that is a
  different dataset and a different population.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `tiktok-ads`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`tiktok_metric` · `warehouse_freshness` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
