---
name: ssi-ad-hooks
description: >
  Load when writing the headline or opening line of an ad: a static's big
  words, the first text card of a short video, or the first line of primary
  text ("write hooks for the toothpaste ads", "give me ten angles for Meta",
  "why do our ads not stop the scroll"). Builds hooks from the brand's own
  facts and customers' own words across distinct hook families, and refuses
  any hook that rests on a claim not on file.
---

# Write hooks that stop the scroll and stay true

## Open this page when

- Writing headlines for statics, first text cards for videos, or the first
  line of an ad's primary text.
- Diagnosing ads that get seen but not clicked.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-hooks`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_context` · `review_themes` · `competitor_review_voice` · `meta_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
