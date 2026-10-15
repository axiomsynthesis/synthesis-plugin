---
name: ssi-growi-creator-payouts
description: >
  Load before quoting anything about a Growi creator or affiliate channel: what you paid
  your creators, what a creator earned, who posted, which campaign a creator is enrolled
  in, or the channel's return ("what do our creators cost", "is the creator program
  paying", "who are our top creators", "did the roster post", "what did we pay creators
  last month"). Keeps paid money, earned money and promised retainers apart, stops an
  empty cost table reading as zero cost, and says which tables carry a date and which do not.
---

# Growi creator payouts, read correctly

## Open this page when

- Any creator, affiliate, ambassador or influencer cost, earning, payout or ROI figure.
- Any creator leaderboard, campaign enrollment, roster funnel or "did they post" question.
- Before any `run_sql` on the `growi` dataset.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `growi-creator-payouts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`growi_creator_payouts` · `growi_top_creators` · `growi_campaign_performance` · `growi_roster_health` · `growi_post_compliance` · `growi_creator_channel_trend` · `describe_schema` · `run_sql` · `data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
