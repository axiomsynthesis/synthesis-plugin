---
name: ssi-competitor-ad-research
description: >
  Load when asked what ads rivals or leading brands are running and which of
  them work ("what statics are the top brands running", "show me our
  competitors' Meta ads", "what formats are winning in our category"). Uses
  Meta's public Ad Library, treats long-running ads as the winners, records
  each ad's layout and hook family, and turns them into patterns, never copies.
---

# Study what other brands' winning ads have in common

## Open this page when

- Before a new batch, to see what is working in the category and beyond it.
- When the brand asks what rivals are running.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `competitor-ad-research`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`competitor_ads` · `competitor_review_voice`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
