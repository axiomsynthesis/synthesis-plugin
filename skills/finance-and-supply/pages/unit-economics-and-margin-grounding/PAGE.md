---
name: ssi-unit-economics-and-margin-grounding
description: >
  Load before quoting any margin, contribution, CM1/CM2/CM3, gross-margin percent or "is
  this product profitable", before a pricing call ("can we afford to drop the price?"),
  and before feeding a margin into a scenario, a valuation or a budget ("what is our CM2",
  "is a 60% gross margin good", "why does my cost sheet say one margin and Amazon
  another"). Different tools label their lines CM1 and CM2 and mean different things, the
  banded waterfall measures nothing and only arranges numbers you typed, and a percent is
  meaningless until you say what it is a percent of.
---

# Unit economics and margin grounding

## Open this page when

- "What is our margin?", "is this product profitable?", "what is our CM2?", "what does a
  60% gross margin mean here?", "can we afford to drop the price?"
- Anyone quotes a margin band as GREEN, YELLOW or RED, or compares your margin to an
  outside benchmark.
- A margin is about to be fed into `run_scenario`, a shock test, a valuation or a budget
  split, where it scales the whole answer.
- Before writing any per-unit waterfall into a report, deck or spreadsheet.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `unit-economics-and-margin-grounding`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`unit_economics_waterfall` · `first_order_contribution_margin` · `breakeven_roas` · `operator_inputs` · `declare_not_known` · `aov`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
