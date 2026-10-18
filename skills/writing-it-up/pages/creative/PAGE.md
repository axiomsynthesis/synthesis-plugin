---
name: ssi-creative
description: >
  Load when asked which ad hooks or angles are making money, what ads to make
  next, for new ad concepts built on what already sells, or for the full
  Synthesis Creative run ("which hooks are working", "what should our next five
  ads be", "give me concepts that double down on our winners", "/creative").
  Synthesis Creative is a paid add-on: a locked tool answers with an upgrade.
---

# Synthesis Creative: ads built on what already sells

## Open this page when

- Asked which hooks, angles or opening lines are making money.
- Asked what ads to make next, or for concepts that double down on winners.
- Running `/creative`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `creative`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`winning_hooks` · `reddit_mentions` · `competitor_ads` · `ad_idea_bank`
`amazon_metric`, with `metric` set to: `customer_personas`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_customer_personas` means `amazon_metric` with `metric` set to `customer_personas`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
