---
name: ssi-distribution-and-risk-reads
description: >
  Load before saying your business is concentrated, a move is real rather than noise, a
  metric has hit a tipping point, a plan survives a bad quarter, or a growth rate compounds
  ("how dependent are we on one product", "is this drop real", "did something change in
  March", "what happens if revenue falls 30%", "who are our top and bottom sellers"). These
  tools measure nothing. They arrange numbers you pass in, and hand back bands, verdicts
  and dollar figures that read as findings. This says where each input must come from,
  what each tool refuses, and which of its outputs are invented defaults.
---

# Distribution and risk reads

## Open this page when

- Concentration: "how much of our revenue is one product / one customer / one channel",
  Pareto, Gini, the 80/20, single-point-of-failure questions.
- Spread: quartiles, deciles, top and bottom performers, outliers, "which products are
  unusual".
- Real or noise: a week-on-week or month-on-month move you are about to call a trend.
- A break: "did something change", tipping points, thresholds, acceleration.
- Downside: "what if revenue drops", cash runway under a shock, whether volatility eats a
  growth rate.
- Before presenting any single undifferentiated number.
- For forecasts and the break test on a revenue series, see also
  `ssi-forecasting-and-trend-reads`. For whether two periods are even comparable, load
  `ssi-compare-like-with-like` first: these tools will happily band apples against
  oranges.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `distribution-and-risk-reads`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`quartile_breakdown` · `percentile_breakdown` · `data_cut_profile` · `propose_brand_fact`
`strategy_framework`, with `framework` set to: `power_law_analysis` · `magnitude_score` · `signal_noise_decomp` · `detect_phase_transition` · `stress_test` · `ergodicity_check`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`power_law_analysis` means `strategy_framework` with `framework` set to `power_law_analysis`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
