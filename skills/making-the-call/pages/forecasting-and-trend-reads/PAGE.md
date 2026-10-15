---
name: ssi-forecasting-and-trend-reads
description: >
  Load before saying what a number will do next or whether it has really changed: a revenue
  forecast or range, a "what has to go right" case, a belief update from a small test, a
  sustained-trend verdict, a break in a series, or a fragility score ("what will Q4 look
  like", "is this drop real or noise", "did something change in June", "how confident can I
  be off 40 conversions", "should we move budget or raise the price"). Most of these tools
  measure nothing: they arrange numbers you type in and hand back a confident-looking answer.
  This says where each input must come from, which defaults are invented, and which output
  can never fire.
---

# Forecasting and trend reads

## Open this page when

- Any forward-looking revenue number, range, fan or scenario.
- "Is this move real?": a drop, a spike, a step change, a plateau.
- Small-sample rates: a test with 40 conversions, a new product's early repeat rate.
- Before putting a probability, a percentile or a "confidence" word in an answer.
- For a metric's plain history without forecasting, use `metric_timeseries` and load
  `ssi-metric-definitions-and-citation`.
- For why a move happened, load `ssi-explain-a-metric-move`. For whether a change can be
  undone, load `ssi-reversibility-and-decision-doors`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `forecasting-and-trend-reads`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`analyze_trend` · `run_monte_carlo` · `run_scenario` · `run_bayesian` · `run_markov_forecast` · `register_prediction`
`strategy_framework`, with `framework` set to: `detect_regime_shift` · `antifragility`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`detect_regime_shift` means `strategy_framework` with `framework` set to `detect_regime_shift`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
