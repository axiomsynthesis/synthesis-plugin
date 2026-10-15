---
name: ssi-gorgias-customer-service
description: >
  Load before you quote any customer-service figure from Gorgias: ticket volume, why
  customers write in, channel mix, time to close or one-touch rate, agent load, or how many
  customers have ever contacted support ("are support tickets up", "what are people
  complaining about", "how fast do we reply", "what is our CSAT"). Names the right table for
  each question, answers the CSAT question honestly when there is no survey data behind it,
  and stops tag noise and content-free subject lines being read as customer demand.
---

# Gorgias customer service, read correctly

## Open this page when

- Any support, CX, ticket, complaint, contact-reason, response-time or agent question.
- "Is something going wrong?" answered from the inbox rather than from sales.
- Before any `run_sql` against your Gorgias data.
- Before answering a CSAT or satisfaction-score question.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `gorgias-customer-service`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`gorgias_metric` · `describe_schema` · `run_sql` · `warehouse_table_preview`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
