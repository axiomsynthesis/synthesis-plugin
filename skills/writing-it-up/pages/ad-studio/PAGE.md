---
name: ssi-ad-studio
description: >
  Load when asked to make paid social ads: Meta or Instagram statics, short
  vertical videos, a batch of new ad concepts, or "make ads for this landing
  page" ("make five statics for the protein bar page", "turn our best video into
  three new ones", "we need new creative for Meta"). Runs the whole loop: hooks
  from the brand's own data, layouts built in code around the real product
  photo, a pre-flight check, an upload pack, then reading results into the
  next batch.
---

# Make ads that win, then learn from them

## Open this page when

- Any request to make Meta, Instagram or other paid social ads: statics,
  short videos, carousels, a batch of concepts.
- "Make ads for this landing page", "refresh our creative", "our statics
  aren't working".
- Reviewing a batch someone else made before it goes live.

For the landing page itself, load `brand-content`. For reading how live ads
are doing, load `meta-creative-diagnosis`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-studio`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_kit` · `brand_context` · `find_product` · `winning_hooks` · `meta_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
