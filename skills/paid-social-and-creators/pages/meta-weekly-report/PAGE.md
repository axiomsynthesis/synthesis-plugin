---
name: ssi-meta-weekly-report
description: >
  Load when you ask about your weekly Meta ads report: what a section means, why a
  number looks wrong, whether this week's report can be trusted, how it was built, or
  when it arrives ("what does the hook section mean", "why is the return blank", "why
  did spend double this week", "the report says narrative unavailable", "when does the
  Meta report come", "can you send me this week's report now"). Covers the one
  standard report shape, the conversion basis (pixel or marketplace attribution)
  picked from your data, the section order for each basis, the checks to run before
  trusting it, and the traps that make a section read wrong.
---

# Your weekly Meta ads report

## Open this page when

- "What does the hook section of my Meta report mean?" / "Why is the return blank?"
- "This week's Meta report looks wrong" / "Why did spend double?"
- "The report says narrative unavailable."
- "When does the Meta report come?" / "Can you send me this week's Meta report now?"
- Checking a Meta weekly before trusting it, or rebuilding one of its figures.

Not for: the general weekly revenue report (a different report, see Traps), or a
one-off Meta question with no report in view (load `ssi-meta-ads-reading`).

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-weekly-report`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `warehouse_freshness` · `meta_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
