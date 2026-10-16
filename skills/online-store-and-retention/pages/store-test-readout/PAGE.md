---
name: ssi-store-test-readout
description: >
  Load when planning or reading a test on an online store: a page against a page, a
  pre-picked pack, a price, an add-on box, free shipping, or a copy change ("set up an A/B
  test for the 4-pack", "who is winning the page test", "can we call it yet", "the new page
  is cheaper per sale, is it better", "should we test this or just ship it", "the add-on
  box changed, did it work"). Judges on money kept per visitor, writes the win line before
  launch, sizes the test against the store's real traffic, and reads what buyers actually
  bought, not only how many bought.
---

# Run a store test that can actually answer the question

## Open this page when

- Before starting any page, price, offer or layout test.
- While one runs ("who is ahead"), and on the decision day.
- When choosing between a split test and just shipping a change with a before/after read.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `store-test-readout`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`measurable_test` · `run_bayesian` · `funnel_decomposition` · `log_decision`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
