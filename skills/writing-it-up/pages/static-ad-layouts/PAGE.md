---
name: ssi-static-ad-layouts
description: >
  Load when building a static image ad for Meta or Instagram ("make a static
  for this hook", "lay out five statics", "make the 9:16 version", "is this ad
  well composed"). Gives golden-ratio grids for every Meta size, a type scale,
  a colour rule, twelve proven static layouts, and the method that places the
  real product photo and exact words in code so nothing is garbled.
---

# Lay out a static ad that reads in one glance

## Open this page when

- Building any static image ad, or another size of an existing one.
- Reviewing a static's composition before it ships.

Hooks come from `ad-hooks`. Backgrounds and props come from `ad-image-prompts`.
Every finished static goes through `ad-preflight`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `static-ad-layouts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_kit` · `find_product` · `render_report`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
