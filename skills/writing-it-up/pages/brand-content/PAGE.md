---
name: ssi-brand-content
description: >
  Load when asked to make something a customer will see: a landing page, a
  product page, an ad or social post, a banner, an email, a one-pager or a
  pitch deck ("build a landing page for the strips", "make three Instagram
  posts for the launch", "draft a page for our new bundle"). Builds it in the
  brand's own colours, type and voice, from its real products, proof and
  customer words, and never invents a claim, a review or a number.
---

# Make brand content that looks and sounds like the brand

## Open this page when

- Any request for a landing page, product page, ad, social post, banner,
  email, one-pager or deck that a customer or the public will see.
- Rewriting copy so it sounds like the brand.
- Checking a draft against the brand's look and voice before it goes out.

For a report, a chart or a deck of the brand's own numbers for the team, use
the writing-it-up guides instead. For paid social ads (Meta statics, short
videos, a batch of ad concepts), open ad-studio: it runs the ad loop.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `brand-content`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_kit` · `propose_brand_kit` · `brand_context` · `find_product` · `review_themes` · `competitor_review_voice` · `marketing_pack`
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
