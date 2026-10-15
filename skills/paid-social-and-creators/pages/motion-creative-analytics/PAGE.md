---
name: ssi-motion-creative-analytics
description: >
  Load before answering anything about ad creative from Motion, if your brand has
  Motion connected: which hook worked, which format holds attention, what a video
  actually says, what competitors are running, or what Motion's AI tags mean ("which
  creative is winning", "what are our best hooks", "what is the competition running",
  "read me the transcript"). Says which Motion table holds what, which tables are
  one-day snapshots with no history, why summaries and transcripts cover only part of
  the catalogue, and why Motion's revenue and return numbers are Meta pixel figures
  that must never be added to your real revenue.
---

# Motion creative analytics, read correctly

## Open this page when

- Any question about ad creative quality, hooks, formats, tags, transcripts or competitor ads.
- Before any `run_sql` against a `motion` table.
- Before quoting a return on ad spend, purchase count or purchase value that came from Motion.
- For Meta spend, campaign structure or the governed Meta numbers, use `meta_metric` and
  `ssi-meta-creative-diagnosis` instead. Motion is the creative layer, not the spend ledger.

If your brand does not have Motion connected, the `motion` dataset will not exist. Say so
and use the Meta creative metrics instead.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `motion-creative-analytics`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`describe_schema` · `warehouse_table_preview` · `run_sql` · `warehouse_tables` · `data_freshness` · `score_creative_metrics` · `build_creative_matrix` · `meta_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
