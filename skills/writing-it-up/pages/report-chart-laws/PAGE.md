---
name: ssi-report-chart-laws
description: >
  Load before drawing any chart in a report, deck, artifact or answer: bars, stacked bars,
  lines, small multiples, funnels, year-over-year overlays, rival lines, stat tiles ("chart
  our sales by week", "show new vs repeat buyers", "plot us against the top rivals",
  "compare this Prime Day with last year's", "this chart looks wrong"). Gives the rules every
  chart must pass so it cannot mislead: where the numbers may come from, clipped bars, axes,
  units, event labels, colour-blind colours, label fitting and printing the numbers beside
  the picture.
---

# Draw charts that cannot mislead

## Open this page when

- Before any chart in a chat answer, an artifact, a PDF report or a deck.
- Before adding stat tiles (headline number boxes) to a page.
- When a chart "looks wrong", "doesn't make sense" or "none of them look proper".
- When reviewing a finished report before it goes out.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `report-chart-laws`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`query_series` · `metric_timeseries` · `emit_chart` · `render_report`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
