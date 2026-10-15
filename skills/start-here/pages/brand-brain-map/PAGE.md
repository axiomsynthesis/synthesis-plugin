---
name: ssi-brand-brain-map
description: >
  Load at the start of any open review of your business ("what should I focus
  on", "what needs a look this week", "walk me through this week"), and for
  connective questions one metric cannot answer: what a product, channel,
  rival or search is linked to, how two things relate, whether a link between
  two weekly numbers is real, what you changed and what happened after.
  Reads your Brand Brain map: ranked by money at stake, every number dated.
---

# Read your Brand Brain

## Open this page when

- Any open question about the whole business: start with `what_matters`.
- "What needs a look", "what changed this week", "walk me through the week".
- What a product, channel, rival or search is connected to, or how one reaches
  another.
- Before quoting a "link" or "connection" from the map as a finding.
- What you changed, and what happened after it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `brand-brain-map`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_brain`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
