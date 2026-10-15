---
name: ssi-operator-number-disagrees
description: >
  Load when someone on your team, your spreadsheet, your agency or an ad platform quotes a
  figure that differs from the one Synthesis returns: "we did 10 orders a day", "that was
  our best day ever", "the dashboard says something else", "Meta shows a better return than
  you do", "my sheet says revenue was higher". Tests the Synthesis side first, finds the
  window, time zone, settling, basis or scope that explains the gap, and shows both numbers
  with the likely cause. Never defends and never averages.
---

# Settle a number someone disputes

## Open this page when

- Someone on your team, a sheet or an agency quotes a daily, weekly or monthly figure
  that differs from what the tools return.
- "That was our best day ever." "We get about ten orders a day on the site." "Our
  spreadsheet says revenue was higher."
- An ad platform's own dashboard shows a different return or spend.
- A connected spreadsheet column drifts from the measured figure for the same thing.
- Before you write "your number is wrong" in any answer or report.

Not for: a tool that returns nothing or refuses. That is a data-connection question
first. Treat an empty or failed read as "not measured", never as zero.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `operator-number-disagrees`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`warehouse_tables` · `data_freshness` · `warehouse_freshness` · `warehouse_row_counts` · `amazon_metric` · `shopify_metric` · `query_series` · `gsheets_metric` · `meta_metric` · `propose_brand_fact` · `record_contradiction`
`check_reasoning`, with `metric` set to: `comparable_basis`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`check_comparable_basis` means `check_reasoning` with `metric` set to `comparable_basis`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
