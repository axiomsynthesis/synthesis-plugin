---
name: ssi-reversibility-and-decision-doors
description: >
  Load before recommending a pause, kill, exit, channel stop, big inventory or
  supplier commitment, a price change, a large budget move, or any other
  consequential action for your brand: "should we pause Meta", "should we kill
  this product", "should we drop Walmart", "should we place this big order",
  "should we cut ads". Prices the extreme action against the best reversible
  alternative (dial back, cap, move the budget), sizes the confidence needed by
  whether the decision can be undone, and runs your brand's policy check before
  the recommendation is made.
---

# Price a pause or kill against the dial-back

## Open this page when

Load this before you write any of these:

- "Pause", "kill", "stop", "exit" or "cut" a running program, campaign, channel or product.
- A big inventory buy, a supplier commitment, a price change, or a channel launch
  (this covers adding or dropping a channel or a product).
- A budget move above your brand's single-action cap.
- A question the "decision_weight" framework classifies as DECISION.
- Any answer where you are about to commit and ask "should we".

Do not load it for a plain "how did we do" read with no action attached.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `reversibility-and-decision-doors`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`strategy_framework` · `working_capital` · `media_response_model` · `diminishing_returns` · `run_scenario` · `recall_decisions` · `product_ltv_windowed` · `policy_check` · `propose_operator_action` · `log_decision` · `log_outcome`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
