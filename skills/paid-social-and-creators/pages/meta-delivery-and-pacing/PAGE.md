---
name: ssi-meta-delivery-and-pacing
description: >
  Load before answering anything about how your Meta ads are DELIVERING rather than
  how the creative looks: daily and weekly spend, campaign and ad set pacing, runaway
  or stalled spend, reach and frequency, spend concentration, the
  impressions-to-purchase funnel, and where a campaign stops paying back as daily
  spend rises ("did spend spike", "is this campaign saturating", "how often are people
  seeing us", "why is Meta spend down this week", "is our spend riding on one ad").
  Picks the right delivery read, explains why the two weekly trends disagree about the
  latest week, and stops a stale ad account reading as a spend cut.
---

# Meta delivery and pacing, read correctly

## Open this page when

- Any Meta spend, impressions, clicks, purchases, ROAS, CPA, CPM, CTR or CPC figure
  read by day, week, campaign, ad set, account or month.
- "Did a campaign run away or stall this week?"
- "Are we saturating this campaign?" and "how often is one person seeing us?"
- "Is our spend riding on one ad?"
- Before any direct SQL on a table in the Meta dataset.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-delivery-and-pacing`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric` · `data_freshness` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
