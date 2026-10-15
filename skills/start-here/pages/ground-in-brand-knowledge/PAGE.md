---
name: ssi-ground-in-brand-knowledge
description: >
  Load at the start of any analysis of your brand, when you mention a document,
  deck, file or spreadsheet ("what does our research say", "check the brief we
  uploaded"), before quoting a stored brand fact, when you say you added a file
  or connected a Drive folder and ask whether Synthesis has it, or when a stored
  fact, an earlier conclusion or a stored weekly report sits next to a live
  number. Reads what your brand already knows in the right order, dates
  everything, and re-pulls every number live. When stored and live disagree,
  live wins and the answer says so.
---

# Ground in what your brand already knows, and let live data win

## Open this page when

- At the start of any analysis of your brand, before the first number.
- When someone mentions a document, research deck, audit, panel, export or
  spreadsheet.
- Before quoting any brand-specific fact: a price, a cost, a claim, a product
  line-up, a positioning statement.
- When a stored fact, an earlier conclusion or a stored weekly brief sits next
  to a live result and the two might not agree.
- Before repeating a diagnosis or recommendation that sounds like one given
  before.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ground-in-brand-knowledge`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`brand_facts` · `brand_memory` · `brand_context` · `list_documents` · `search_file_content` · `search_files` · `list_files` · `read_file` · `get_hypotheses` · `recall_decisions` · `run_principles_engine` · `get_weekly_brief` · `get_weekly_report` · `get_links` · `data_freshness` · `data_freshness_sweep`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
