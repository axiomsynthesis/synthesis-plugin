---
name: ssi-brand-assets-and-recurring-outputs
description: >
  Load before producing the weekly report as a file, a creative or listing brief, a brand
  kit drafted off your website, a brand-voice score, or before quoting anything from the
  object map ("send me this week's report", "write me a brief for our best seller", "pull
  our brand colours off the site", "what objects does Synthesis track for us"). These five
  tools produce documents and curated text, not measurements. Two of them stamp a file
  "passed" when half the check never ran, and one silently caps its counts.
---

# Brand assets and recurring outputs

## Open this page when

- Any request for the weekly report as a file, on demand or on a schedule.
- Any creative brief, listing brief or marketing pack.
- Any brand-kit work: reading your colours, type or logo off your own website.
- Any brand-voice score.
- Before quoting the object map, or when asked what the playbook or the law list says.
- For what the weekly report's revenue and customer numbers mean, load the skills on
  Amazon revenue basis and on new and repeat customers as well. This skill covers the
  wrapper, not the metrics inside it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `brand-assets-and-recurring-outputs`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`generate_weekly_report` · `marketing_pack` · `propose_brand_kit` · `get_ontology`
`strategy_framework`, with `framework` set to: `score_voice_consistency`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`score_voice_consistency` means `strategy_framework` with `framework` set to `score_voice_consistency`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
