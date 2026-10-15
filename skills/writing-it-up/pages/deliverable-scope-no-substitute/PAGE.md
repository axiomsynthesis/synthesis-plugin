---
name: ssi-deliverable-scope-no-substitute
description: >
  Load when you ask for an export, deck, P&L, spreadsheet or report for a
  month, basis, channel or season whose data is missing or incomplete: "export
  June's P&L" before June is closed, "build me the board deck for last month",
  "compare this season to last" with only part of last season on file, "the
  file I sent should be in there". It stops a quiet swap to a near-version (last
  month, a partial file) and hands the choice back instead.
---

# When the requested data does not exist, ask. Do not substitute.

## Open this page when

- A request for a file (spreadsheet, deck, PDF, Word doc, report) names a month,
  a date window, a season, a channel or a basis. Basis means how money is
  counted: when orders were placed, when money settled into the bank, or when it
  was booked in the accounting ledger.
- And a tool comes back gated, flagged, empty, or covering less than the window
  that was asked for.
- Also load it when two files are about to be compared year on year, and when
  someone says "the file I sent should be in there".

The rule in one line: deliver exactly what was asked, or stop and say what is
missing. Never hand over a near-version with a caveat stapled on.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `deliverable-scope-no-substitute`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`monthly_pnl` · `net_revenue` · `build_deck` · `data_freshness` · `warehouse_freshness` · `data_freshness_sweep` · `list_documents` · `search_files` · `list_files` · `read_file` · `declare_not_known` · `render_report` · `export_xlsx`
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
