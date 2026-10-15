---
name: ssi-ad-preflight
description: >
  Load before any ad leaves your hands: a static, a short video or a batch
  going into an upload pack ("check these ads before we publish", "is this ad
  safe to run", "why did Meta reject this"). A pass-or-fail checklist for
  claims, proof, creator and partner disclosure, Meta's health and beauty
  rules, copy that reads as machine-written, legibility, sizes, the match
  with the landing page, naming, and whether a batch is different enough.
---

# Check an ad before it goes out

## Open this page when

- Before handing over any upload pack.
- When an ad was rejected or flagged and you need the cause.
- When reviewing ads someone else made.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-preflight`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_context`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
