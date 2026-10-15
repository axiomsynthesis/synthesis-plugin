---
name: ssi-short-video-ads
description: >
  Load when making a short vertical video ad of about 5 to 10 seconds with
  text over it, including ones with an AI-made person reacting to or handling
  the product ("make a 7-second video like our best one", "an AI girl looking
  surprised holding the tube", "turn this static into a quick video"). Gives
  the second-by-second structure, prompts for image-to-video models, overlay
  rules, and the legal lines an AI actor must not cross. Also covers 15, 30
  and 60 second scripts and a brief for a real creator.
---

# Make a short text-over video that clicks

## Open this page when

- Any short vertical video ad of about 5 to 10 seconds.
- Remaking the brand's best short video in new versions.
- Any ad with an AI-made person in it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `short-video-ads`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
