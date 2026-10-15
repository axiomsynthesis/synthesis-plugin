---
name: ssi-decision-frameworks
description: >
  Load before running any strategy grid or option scorer: SWOT, BCG, Ansoff, Five Forces,
  Blue Ocean, a positioning map, a scenario grid, a war game, pros and cons, a priority
  ranking, a weighted scorecard or Kelly sizing ("score these options", "put our products on
  a BCG matrix", "which action should I do first", "how big should this bet be", "where is the
  whitespace in my category"). None of these tools measures anything. They arrange the numbers
  you type in and hand back a ranking, a band or a quadrant that looks like a finding. This
  says where each input must come from, which defaults pass for measurements, and which
  quiet fallbacks turn a typo into a confident wrong answer.
---

# Decision frameworks, and why their output is not evidence

## Open this page when

- Any request to "score", "rank", "prioritise", "map" or "put on a matrix".
- Any strategy framework by name: SWOT, BCG, Ansoff, Porter's five forces, Blue Ocean, Jobs To
  Be Done, Playing To Win, Grove's forces, Schwartz awareness levels, Kelly sizing.
- Before building a scenario grid, a war game or a plan for answering a competitor's move.
- Not for the numbers themselves. Get the figures from your channel tools first (Amazon,
  Shopify, Meta and the rest), then come back here to arrange them.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `decision-frameworks`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`score_counter_position`
`strategy_framework`, with `framework` set to: `weighted_score` · `plot_2x2` · `bcg_matrix` · `ansoff_matrix` · `positioning_map` · `scenario_2x2` · `swot` · `errc_grid` · `playing_to_win` · `jobs_to_be_done` · `awareness_levels` · `five_forces` · `ten_x_forces` · `war_game` · `response_severity` · `pros_cons` · `rank_decision_options` · `kelly_sizing` · `priority_score`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`weighted_score` means `strategy_framework` with `framework` set to `weighted_score`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
