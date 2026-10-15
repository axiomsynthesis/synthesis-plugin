---
name: ssi-invoke-deep-synthesis
description: >
  Load when your message contains the word "deep" in any spelling about a
  business question ("@deepsynthesis", "deepsynthesis", "deep synthesis on why
  repeat fell", "go deep on this", "deep dive into our ad spend"), or when a
  deep run's status, result or error arrives, or you want the result of a deep
  run started in another session. Starts the server's deep analysis with your
  own words, waits for it patiently, reads the receipt honestly, and relays
  the finished answer exactly as written.
---

# Invoke deep synthesis

## Open this page when

- The message contains the word "deep" anywhere, in any form. That is an
  instruction, however simple or table-shaped the question looks.
- A deep run is already going and is being polled, or its result, error or restart
  notice has just come back.
- Someone asks to see the result of a deep run started in another session.

Not this page: a message that only names the server, with no "deep" in it, and
"deep" said about code or a file. If it is unclear whether a live run is wanted,
ask in one line first.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `invoke-deep-synthesis`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`deep_synthesis` · `query_series` · `deep_research_start` · `deep_research_status` · `deep_research_result`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
