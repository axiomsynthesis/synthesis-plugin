---
name: ssi-operator-sheets-reading-and-grounding
description: >
  Load for any answer that reads one of your connected Google Sheets: a target, a budget,
  a plan, a tracker, a KPI workbook, a creator offer sheet ("what is our target this
  month", "what did we plan to spend", "what does the tracker say we owe this creator",
  "my sheet and your number disagree for last week"). Sheets are your own typing, read as
  displayed, with no history, and they hold the targets and plans no connector can supply.
  Says how to find the right tab, turn its values into numbers without inventing one, and
  check it against what Synthesis measures without pretending the sheet was measured.
---

# Read your spreadsheet, and check it against what is measured

## Open this page when

- A question whose answer is in a workbook: "what is our target", "what did we plan to
  spend", "what does the tracker say we owe this creator".
- A sheet column and a measured number disagree for the same period.
- Before quoting a tab's own words back to anyone.

Nearby skills, so this one does not repeat them: the skill on a disputed number settles
the disagreement once you have both numbers (come here first, go there second); the
skill on grounding in brand knowledge treats a tab as a document to search and quote.
This skill is the numbers half.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `operator-sheets-reading-and-grounding`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`gsheets_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
