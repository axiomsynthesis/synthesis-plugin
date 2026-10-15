---
name: ssi-long-tail-connectors-reading
description: >
  Load when a question touches Fairing, Triple Whale, Instacart, Loop Returns, ShipHero,
  ShipStation, Stay Ai, Yotpo, Crisp, Mailchimp, Customer.io, ActiveCampaign or Campaign
  Monitor, or what they measure: "what does our how-did-you-hear-about-us survey say", "what
  is our blended ROAS", "how are we doing on Instacart", "why are people returning things",
  "what does shipping cost us", "what do our site reviews say", "what is selling through at
  Kroger". None of these has a metric tool. Says how to check whether the data exists before
  answering, and the one scope limit each source carries, so a survey is never read as
  attribution and an ads feed is never read as sales.
---

# The long-tail connectors: check they hold anything, then read them narrowly

## Open this page when

Any question naming one of these products or the thing it measures: the post-purchase
survey, blended ROAS, Instacart, DTC returns and reasons, shipping cost, fulfilment status,
a subscription book outside Recharge and Skio, on-site reviews, retail sell-through across
several retailers, or an email question about any platform other than Klaviyo and Attentive.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `long-tail-connectors-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
