---
name: ssi-exports-and-deliverables
description: >
  Load before turning an answer into a file someone can forward — a PDF, a Word memo, a
  slide deck, a spreadsheet, a dashboard or a one-call framework deck ("send me that as a
  PDF", "build the board deck", "export the P&L to Excel", "make me a dashboard", "make a
  battlecard", "can I have something I can send to our investor"). Says what to build
  when a dashboard is asked for with no detail, says which door runs the pre-render size check and which one
  does not, what the auto-built decks quietly assume when you leave their inputs blank,
  which template spends a metered search allowance and describes a product that is not
  yours unless you name one, and how long the download link lives.
---

# Exports and deliverables, built so the file can be forwarded

## Open this page when

- Any request for a PDF, Word document, deck, slide, spreadsheet or "something I can
  send".
- "Make me a dashboard", "build a dashboard", "can I get a dashboard", with or without
  any detail about what goes on it.
- Before `build_deck`, and always before its competitive template.
- When a deliverable comes back RENDER REFUSED and you are deciding whether to pass
  `force`.
- When someone asks why the file looks different from the weekly report, or why a link
  they were sent has stopped working.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `exports-and-deliverables`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_kit` · `render_report` · `export_pdf` · `export_docx` · `export_pptx` · `export_xlsx` · `build_deck`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
