---
name: ssi-compose-the-founder-answer
description: >
  Load when writing any final answer, report narrative, deck commentary, alert,
  table header or gap message that a founder, operator or marketer at your brand
  will read: "what should I do about this", "write up what happened this month",
  "give me the summary for my team", "why did sales drop, and what now". Sets the
  shape and the voice: a plain verdict in the first sentence, a set section
  order, moves sized in dollars with a dated trigger, the do-nothing line,
  caveats said once in plain words, and no jargon, codes or narrated checks.
---

# Write the answer a founder will read

## Open this page when

- You are about to write the final answer to a business question, simple or deep.
- You are writing the prose of a report, a deck's commentary, an alert, or a
  one-line summary for a founder or operator.
- You are writing text that is fixed in a report layout: a table header, the
  message in an empty section, the note that says what to connect.
- You are about to correct a number you gave earlier.

Neighbouring skills carry detail this one only points to: `ssi-audit-your-draft`
for the full pre-send audit, and `ssi-revise-without-corrupting-numbers` for any
second pass over a draft that already has figures in it.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `compose-the-founder-answer`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`check_reasoning` · `declare_not_known` · `register_prediction` · `capture_turn`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
