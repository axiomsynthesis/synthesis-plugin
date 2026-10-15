---
name: ssi-ad-test-and-learn
description: >
  Load when launching a new batch of ads or reading how one did ("how should
  we test these statics", "which of the new ads won", "what should the next
  batch be", "when do we kill an ad"). Sets where new ads go, when to judge
  them, the kill and keep rules, and how to tag every ad so the winners'
  hooks and layouts feed the next batch.
---

# Test a batch, keep the winners, learn why they won

## Open this page when

- Planning where and how a new batch goes live.
- Reading a batch after it has run.
- Deciding the next batch.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-test-and-learn`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`meta_metric` · `register_prediction` · `log_decision` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
