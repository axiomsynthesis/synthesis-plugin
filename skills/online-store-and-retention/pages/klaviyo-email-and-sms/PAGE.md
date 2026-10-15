---
name: ssi-klaviyo-email-and-sms
description: >
  Load before you quote any email or SMS figure from Klaviyo: campaign or flow revenue, open
  rate, click rate, bounce or spam rate, which subject lines work, the best time to send,
  template performance, or "how much of our revenue does email drive" and "is email worth
  scaling". Says which Klaviyo table answers the question, why the open rate is soft and the
  email revenue share is a floor, and which join key actually matches. Also: which
  automated flows a store should have, and what to check before any SMS send.
---

# Klaviyo email and SMS, read correctly

## Open this page when

- Any email or SMS number: campaigns, flows (automations), deliverability, list engagement,
  subject lines, send times, templates.
- "How much revenue does email drive?" and "is email worth scaling?"
- Before any `run_sql` against your Klaviyo data.
- Email figures are usually compared against website revenue; read that denominator with the
  Shopify revenue skill.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `klaviyo-email-and-sms`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`klaviyo_metric` · `email_performance` · `email_flows` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
