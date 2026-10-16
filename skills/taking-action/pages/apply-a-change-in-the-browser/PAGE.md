---
name: ssi-apply-a-change-in-the-browser
description: >
  Load when the brand wants its own Claude to make the changes on a Synthesis change list,
  in the brand's own browser and signed in as the brand: "apply this for me", "make these
  changes", "go pause those ads", "add the negatives in the ad console", "tag these
  customers in Shopify", "change the subject line in Klaviyo", "do it in Ads Manager".
  The protocol for one change at a time: check the account on screen, show the change,
  get a yes, make it, read it back, and log each row as confirmed, not confirmed or
  skipped. Platform steps for Meta Ads Manager, Shopify admin, the Amazon Ads console and
  Klaviyo are in its reference pages.
---

# Apply a change in the browser

## Open this page when

- "Apply this list for me", "make these changes", "go do it", "can you change it for me?"
- After any change list from the taking-action pages, when the brand would rather not upload
  the file or click through the changes by hand.
- "Pause those ads in Ads Manager", "add the negatives", "change that bid", "tag these
  customers", "create the discount code", "pause the flow", "change the subject line".
- Not for deciding what to change. The change list decides that. If there is no list yet,
  build it first with the action page for that platform and the change-list standard.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `apply-a-change-in-the-browser`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`log_decision`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
