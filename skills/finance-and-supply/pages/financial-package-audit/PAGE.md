---
name: ssi-financial-package-audit
description: >
  Load when you are handed another company's own finance pack (P&L workbooks, a financial
  model, a cash or health model, a data-room export) and need to know whether the numbers
  are real, want the P&L rebuilt, or are deciding whether to invest, lend, buy or get
  involved ("are these numbers real", "rebuild their P&L", "should I put money in", "check
  this acquisition target's model", "does this data room hold up"). Audits a spreadsheet
  nobody on your side built: recalculates before reading, tests every "check" row, finds
  formulas that skip a cell, ties net income to their books, hunts undisclosed debt, and
  answers the decision first.
---

# Audit another company's finance pack

## Open this page when

- Another company's own finance pack has arrived: a profit-and-loss workbook, a
  financial or cash model, a data-room export.
- "Are these numbers real", "rebuild their profit and loss", "does this data room
  hold up", "check this acquisition target's model".
- Deciding whether to invest in, lend to, buy or join another company.

Not this page: your own numbers. Nothing here is connected data, so every check
has to be built by hand from the pack itself.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `financial-package-audit`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`export_xlsx` · `export_pptx` · `export_pdf` · `export_docx`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
