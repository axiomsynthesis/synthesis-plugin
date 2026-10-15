---
name: ssi-audit-your-draft
description: >
  Load before sending any answer, memo, deck text or report narrative that
  states your brand's figures, and whenever someone asks "are these numbers
  right?", "did you check this?" or "can I send this to my team?". Also load
  when a figure re-check comes back with confirmed, mismatched or unverifiable
  results. Re-derives every figure at its own level first, then runs the ship
  checks, removes sentences that are known wrong, qualifies the ones that are
  only unverified, and says plainly which figures were never re-derived.
---

# Audit your draft before it ships

## Open this page when

- You are about to send an answer, memo, deck text or report narrative with
  dollar figures, counts, rates, margins or "best since" claims in it.
- You have re-derived a draft's figures and need to read what confirmed,
  mismatch and unverifiable mean for the draft.
- Someone asks "are these numbers right?" or "did you check this?"
- Not needed for a deep synthesis answer. It arrives already checked by the
  server, with known-wrong sentences removed. Relay it as handed to you; do not
  rewrite it or re-audit it by editing it (as of September 2026).

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `audit-your-draft`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`revenue_by_sku` · `units_sold` · `product_customers` · `query_series` · `check_reasoning` · `amazon_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
