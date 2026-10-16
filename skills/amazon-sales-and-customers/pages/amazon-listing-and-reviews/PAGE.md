---
name: ssi-amazon-listing-and-reviews
description: >
  Load before answering anything about your Amazon listing's quality, its main image, its
  price or rank against rivals, its star rating and review flow, or who buys it ("is our
  listing worse than theirs", "why did our rating drop", "are competitors getting reviews
  faster", "who are our Amazon customers", "can I say this in my title"). Separates the two
  listing scores that share a name and score different things, keeps a rating step from
  being read as a review average, stops a variation rollup reading as Amazon deleting
  reviews, and explains why Amazon demographics come back unavailable.
---

# Amazon listing quality, shelf position and reviews

## Open this page when

- Any Amazon listing audit, listing score, title, bullet or image question, or "is our page
  as good as theirs".
- Any request to write or approve Amazon listing copy (a title, a bullet, A+ content), where
  the question is what the page is allowed to say. See the copy rules below.
- Any star rating, review count, review pace or "why did our rating fall" question.
- Any competitor price, BSR (Best Sellers Rank), shelf position or "who is gaining on us".
- Any Amazon customer mix, demographic or value-segment question.
- For search share and keyword gaps, load ssi-amazon-search-share-sqp instead. This skill says
  WHEN a rating moved and on WHICH listing, never WHY. The why lives in the review text.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-listing-and-reviews`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric`
`strategy_framework`, with `framework` set to: `score_listing`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`score_listing` means `strategy_framework` with `framework` set to `score_listing`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
