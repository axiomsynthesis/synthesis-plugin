---
name: ssi-revise-without-corrupting-numbers
description: >
  Load before any rewrite, repair, fix-up, plain-English, shortening or polish
  pass over text that already contains your brand's figures: "fix these lines",
  "make this readable", "tighten this answer", "cut this in half", "correct
  that number", "tidy this up before I send it". Limits every change to the
  passage a named problem covers, copies figures word for word, and throws out
  any revision that moves a number it was not asked to move.
---

# Revise without breaking the numbers

## Open this page when

- A check, a reviewer or the person you are working for has named problems in
  a draft, and you are about to fix them.
- "Make this plain English." "Cut this in half." "Tidy the wording." "Make it
  read better." Any readability or shortening pass over figures.
- "That number is wrong, fix it." A correction to one figure inside a longer
  answer, report or deck.
- You are about to hand a draft to another model or helper to revise.

Not for writing a first draft. That is the job of
`ssi-compose-the-founder-answer`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `revise-without-corrupting-numbers`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
