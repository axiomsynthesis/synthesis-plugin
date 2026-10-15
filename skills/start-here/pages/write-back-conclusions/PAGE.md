---
name: ssi-write-back-conclusions
description: >
  Load at the end of a substantive answer, when you attach a file, when a
  forward-looking number is stated ("we should hit 20% repeat by March"), when a
  stored fact about your brand turns out wrong, or when you commit to a decision
  or report how one played out ("we're going ahead with the price cut", "the
  bundle test failed"). Files only checked conclusions, facts, predictions,
  decisions and files back to Synthesis, to the right tool, at the right
  approval level, so your brand's memory compounds instead of filling with
  stale numbers.
---

# Write back what was learned

## Open this page when

- A substantive answer is finished, or a file has been attached to the chat.
- A forward-looking number has been stated, a durable fact about the brand has been
  learned, or a stored fact has turned out to be wrong.
- A decision is committed to, or someone reports how one played out.

Each of those is a trigger, not a habit. Do not file a plain single-number lookup
with no reading attached.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `write-back-conclusions`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`capture_turn` · `commit_extracted_memories` · `register_prediction` · `propose_brand_fact` · `propose_principle` · `record_contradiction` · `propose_hypothesis` · `get_hypotheses` · `record_hypothesis_result` · `log_decision` · `recall_decisions` · `link_outcome_to_prediction` · `log_outcome` · `resolve_prediction` · `track_record` · `describe_action` · `enact_ontology_action` · `ingest_file` · `get_upload_link` · `finalize_upload` · `log_question` · `rate_synthesis_output`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
