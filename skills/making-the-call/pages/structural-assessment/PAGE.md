---
name: ssi-structural-assessment
description: >
  Load when you ask for a full structural assessment, a brand health check, the full picture,
  a full diagnostic, or "where does my brand stand" / "what shape is the business in". Gives
  the seven things such an assessment must cover, the five-finding cap that keeps it readable,
  the rule that turns a second request inside two weeks into a status update, and why a
  priority ranking built on unmeasured inputs must never be printed as a score.
---

# The full structural assessment

## Open this page when

- A full structural assessment, a brand health check, a full diagnostic, "the full
  picture", "where does my brand stand", "what shape is the business in".

Not this page: the scheduled weekly or monthly report. This is a one-off read, and
it carries its own limits on length, on repeats and on what may be ranked.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `structural-assessment`. The `doctrine` field of the result is this page's
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
