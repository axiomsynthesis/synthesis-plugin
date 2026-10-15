---
name: ssi-shopify-winback-tags
description: >
  Load when you want to act on lapsed website customers: "who should we win back", "give me
  a list of lapsed repeat buyers to tag", "build a win-back segment for Klaviyo", "tag
  customers who haven't ordered in six months", "export the win-back list so I can upload
  it". Turns the Shopify win-back candidates into a reviewed change list sized by tier, with
  the contact file as a download only (never in the chat) and a safe way to load it into
  Klaviyo or Shopify yourself, and says plainly what the list cannot tell you about marketing
  consent and recent orders.
---

# Win-back tags for lapsed Shopify customers

## Open this page when

- You want a list of lapsed repeat customers to email, tag or put in a segment.
- You are about to upload customers into Klaviyo or into Shopify's customer import.
- Someone asks "how many customers could we win back, and who are they".
- For how the win-back table is built and how to read it, also load
  `ssi-shopify-summary-tables`. For the email side, load `ssi-klaviyo-email-and-sms`. The
  column meanings of the change list are defined in `ssi-change-list-standard`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `shopify-winback-tags`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`shopify_metric` · `export_xlsx`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
