---
name: ssi-explain-a-metric-move
description: >
  Load for any "why did this go up or down" question ("why is revenue down this month",
  "what drove the jump in July", "why did conversion fall", "is this growth real"), and
  before writing the words because, driven by, due to or thanks to next to a number. Turns
  a spike into a ruled list of candidate causes, each with a verdict, a size and its
  evidence, plus the part still unexplained. Carries the split that separates "the products
  got worse" from "the traffic moved to a worse product".
---

# Why did this number move?

## Open this page when

- You ask why revenue, orders, customers, conversion or contribution moved.
- A draft is about to say "because", "driven by", "thanks to" or "due to" beside a figure.
- A chart shows a spike or a collapse and somebody wants it captioned.
- Two figures from the same report disagree and the gap needs a cause.
- A month, week or product looks like a step change and the word "growth" is about to be
  used.

Do not load it to find out whether a number moved. That is `analyze_trend`. Load it once
the move is established and a reason is wanted.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `explain-a-metric-move`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`explain_metric_move` · `amazon_metric` · `analyze_trend` · `query_series`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
