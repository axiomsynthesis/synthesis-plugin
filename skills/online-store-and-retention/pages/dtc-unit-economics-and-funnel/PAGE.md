---
name: ssi-dtc-unit-economics-and-funnel
description: >
  Load for the website margin ladder (CM1, CM2, CM3) and the site funnel. Situations: "are our
  unit economics healthy", "what do we keep per order", "what is our CM1", "where is the site
  leaking", "should we fix traffic or conversion first", "how do we raise order value", "is a
  bundle worth it", "how long should this A/B test run". Says which numbers Synthesis actually
  measures and which you type in, why the margin tool reads perfect when costs are left blank,
  and why the leak tool names the same step on almost every store.
---

# The website margin ladder and funnel

## Open this page when

- "Are our unit economics healthy?" "What do we keep per order?" "What is our CM1 or CM2?"
- "Where is the site leaking?" "Should we fix traffic or conversion first?"
- "How do we raise average order value?" "Is a bundle worth it?"
- "How do we run an A/B test properly?" "How long should this test run?"
- Any answer about to call a margin or conversion figure healthy, weak or below target.

Not for an Amazon P&L, Amazon profit tools, or the ad-return question; each has its own skill.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `dtc-unit-economics-and-funnel`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`unit_economics_waterfall` · `first_order_contribution_margin` · `funnel_decomposition` · `aov_levers` · `ga4_metric` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
