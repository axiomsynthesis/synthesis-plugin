---
name: ssi-amazon-ppc-decisions
description: >
  Load when deciding what to change in Amazon ads: which search terms waste money, what to
  negate or harvest, whether ACoS is too high, how to split budget, whether ads grow the
  business, or whether to cut a product's ads ("what should I negate", "is 60% ACoS too
  high", "should we cut ads on the single", "where is the budget going wrong", "how hard
  can we bid"). Uses your own break-even from settled margin, treats a term that sold
  nothing as the worst case, checks negatives at both levels, decides at the product
  family, protects entry products, and recommends rather than writing bids.
---

# Deciding what to change in Amazon advertising

## Open this page when

- "What should I negate?", "which searches waste money?", "what should we harvest?"
- "Is our ACoS too high?", "what is our break-even?", "how hard can we bid?"
- "Should we cut ads on this product?", "which products lose money after ads?"
- "How should the budget be split?", "is spend going to the right searches?"
- "Are ads growing the business or just buying sales we would have had?"
- Before writing any bid, budget, negative or harvest recommendation in an answer or report.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-ppc-decisions`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`breakeven_roas` · `describe_schema` · `run_sql` · `propose_brand_fact` · `log_decision` · `register_prediction`
`amazon_metric`, with `metric` set to: `ppc_keyword_roi` · `breakeven_acos_ltv` · `ppc_search_terms` · `ppc_match_type_coverage` · `ppc_keywords` · `ppc_keyword_bids` · `ppc_branded_split` · `ppc_spend_by_parent` · `ppc_profit_by_asin` · `ppc_halo` · `ppc_placements` · `ppc_budget_utilisation` · `ppc_organic_vs_paid` · `tacos` · `ppc_purchase_latency`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_ppc_keyword_roi` means `amazon_metric` with `metric` set to `ppc_keyword_roi`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
