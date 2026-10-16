---
name: ssi-landing-page-go-live
description: >
  Load when someone wants a new or changed landing page for paid traffic on a Shopify store
  ("build a page for these ads", "make a version of our best page with the bigger pack",
  "push this page live", "is the new page live", "the price on the page is wrong at
  checkout", "why is the page slow on phones", "do we need the cookie banner"). Builds from
  the page that already sells, changes one thing, previews on real phone sizes, proves every
  price the page shows is the price checkout charges, pushes only the new files with a way
  back, then checks the live page as a shopper would.
---

# Put a landing page live without breaking the one that works

## Open this page when

- Building a page for a new ad angle, offer or pack.
- Before pushing any page change live, and right after.
- When a shopper or the founder says the price, the link or the page looks wrong.
- When choosing what to fix first on a page that converts badly.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `landing-page-go-live`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`ga4_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
