---
name: ssi-recharge-subscriptions
description: >
  Load for Recharge subscription questions on your web store: "how many subscribers do we
  have", "what is our MRR", "is churn going up", "why do subscribers cancel", "what is our
  skip rate", "how much churn is failed payments", "what will subscriptions bill next
  month", "what is a subscriber worth", or who a save flow should target. Leads with what
  actually bills and what actually got paid, treats the nominal book as a ceiling, and knows
  which subscription reader answers which question. Not for Amazon Subscribe and Save.
---

# Read Recharge subscriptions as billing and paid, never nominal

## Open this page when

- "How many subscribers do we have?" "What is our MRR (monthly recurring revenue)?"
- "Is churn going up?" "Why do people cancel?" "How much churn is failed payments?"
- "What is our skip rate?" "Is the default cadence too frequent?"
- "What will subscriptions bill over the next 8 weeks?"
- "What is a subscriber worth?" "Does subscribing on the first order raise LTV (lifetime
  value: what a customer pays over their whole time with the brand)?"
- "Which products carry the subscription book?" "Who should the save flow target?"
- Any sentence with "active subscribers", "subscription revenue" or "recurring".

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `recharge-subscriptions`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`recharge_metric` · `subscription_economics` · `ltv_drivers` · `shopify_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
