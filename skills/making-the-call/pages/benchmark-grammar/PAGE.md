---
name: ssi-benchmark-grammar
description: >
  Load before calling any metric good, bad, healthy, weak, strong or below target,
  before comparing a number to a benchmark, band, threshold, "industry average" or
  "what it should be", and before turning a cut-off you proposed into a rule ("is
  our repeat rate good", "is 12% healthy", "how do we compare to the category",
  "what should our ROAS be", "are we below target", "should we pause this, it's
  under benchmark", "only flag it if it's over X"). Says which reference may grade
  a number (only a goal you set), how to use your own baseline and outside priors
  as headroom instead, and which lines to never write.
---

# Benchmarks are headroom, never grades

## Open this page when

- "Is our repeat rate good?" "Is 12% healthy?" "How do we compare to the category?"
- "What should our ROAS (sales per dollar of ad spend) / TACoS (the share of Amazon
  revenue spent on ads) / conversion / Subscribe and Save share be?"
- "Are we below target?" "Should we pause this, it's under benchmark?"
- Any answer or report about to write good, bad, healthy, weak, green, red, on
  track, behind.
- You say "only show it if it's over X" or "flag anything under Y". That cut-off is
  a hypothesis. See "What caps results here".
- A tool comes back with a verdict word (excellent, good, average, poor, HEALTHY,
  WARNING, CRITICAL).

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `benchmark-grammar`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_facts` · `brand_context` · `amazon_metric` · `query_series` · `metric_timeseries` · `percentile_breakdown` · `benchmark_metric` · `check_reasoning` · `metric_health_band` · `propose_brand_fact` · `log_decision` · `register_prediction`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
