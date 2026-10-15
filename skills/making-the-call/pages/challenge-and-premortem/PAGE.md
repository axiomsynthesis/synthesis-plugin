---
name: ssi-challenge-and-premortem
description: >
  Load before giving a final recommendation on your brand, or when you push back
  on one: "are you sure?", "argue the other side", "what could go wrong", "what if
  we're wrong", "give me the opposite call", "that seems wrong". Builds the single
  strongest case against the call, argued with numbers, gives an honest verdict
  on whether it reverses the call, then runs a pre-mortem with three named
  failure modes and the early warning sign for each.
---

# Argue the strongest case against before recommending

## Open this page when

- You are about to commit to a recommendation that costs money, time, or is hard to undo.
- The person challenges a recommendation already given ("are you sure?", "that seems wrong").
- The person asks you to argue the other side, or asks for the opposite call.
- A new answer points the other way from something recommended in an earlier session.
- Not for a purely descriptive question ("what was revenue last month?"). There is no call to attack.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `challenge-and-premortem`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## No tool of its own

This page is judgment rather than a reader. The method names whatever
tools the question needs.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
