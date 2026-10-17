---
name: ssi-ad-image-prompts
description: >
  Load when an ad needs an AI-made picture: a background, a scene, a texture,
  a prop or an illustration ("make a bathroom-counter background for the
  tube", "we need a cross-section illustration of how it works", "give me a dark blue
  light-ray backdrop"). Gives prompt templates for any image model and the
  rules that keep AI away from the product, the words and fake results.
---

# Prompt an image model for the parts AI is good at

## Open this page when

- A static or video needs a background, a scene, a texture or a prop.
- A diagram-style illustration (how the product works) is wanted.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-image-prompts`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_kit`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
