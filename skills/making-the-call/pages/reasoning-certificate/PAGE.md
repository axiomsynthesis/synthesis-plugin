---
name: ssi-reasoning-certificate
description: >
  Load after the evidence about your brand is gathered and checked, and before
  writing a recommendation the answer rests on. "Should we do this?" "Is that
  call sound?" "How sure are you?" "Why do you think that?" Runs six questions
  on the reasoning, fills a private reasoning certificate, and decides what the
  answer may claim, how strongly, and which one-line qualifiers go next to which
  claims. The certificate itself is never shown in the answer.
---

# Certify the reasoning before you write

## Open this page when

- You have the evidence and are about to write a recommendation, a diagnosis,
  a forecast or a "why" answer that someone will act on.
- A conclusion depends on a cause, a trend, or a forecast rather than one
  pulled number.
- The person pushes back and you feel the pull to change your call.
- Not for a plain lookup ("what was revenue last month?"). A single pulled
  number with its source needs no certificate.

If you are inside a deep-synthesis run, its verify stage asks for this same
certificate as a labeled block and checks it. Follow that stage's own
instructions there. This skill is the same discipline for every other answer.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `reasoning-certificate`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`strategy_framework` · `measurable_test` · `register_prediction` · `get_calibration_for_claim`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
