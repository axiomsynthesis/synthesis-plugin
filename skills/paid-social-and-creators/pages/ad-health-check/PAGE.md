---
name: ssi-ad-health-check
description: >
  Load when someone wants one verdict across all their ad accounts rather than one platform
  ("check my ads", "ad health check", "audit my ad accounts", "is my ad spend healthy",
  "what is wrong with my ads", "run a health check on Amazon, Meta and Google ads"). One
  server call runs fifteen fixed checks across Amazon ads, Meta, Google Ads, TikTok ads and
  the books, decides pass, fail, unknown or not applicable for each, ranks failures by
  dollars a month and states how much could be read. Not for a single metric on one
  platform: that platform's own page answers it.
---

# The ad health check

## Open this page when

- Any request for a health check, audit or review across ad accounts.
- "Is my ad spend healthy", "what is wrong with my ads", "where am I wasting ad money".
- After fixing something, to recheck one platform.
- Not for one number on one platform (Meta spend last month, Amazon ACoS): open that
  platform's page instead.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-health-check`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`ad_health_check`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
