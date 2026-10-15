---
name: ssi-meta-creative-diagnosis
description: >
  Load when you ask which Meta ads are working, why an ad is failing, whether a
  creative is tired or worn out, which ads to scale or cut, or how fast to raise
  budget on a winner ("which of my Meta ads actually work", "is it the hook or the
  landing page", "are my ads tired", "what should I kill"). Walks one ad through a
  fixed ladder (first frame, middle, call to action, landing page, fatigue), judged
  against your account's own median rather than a textbook line, with sample floors
  so an ad that was barely shown is not blamed.
---

# Meta creative diagnosis

## Open this page when

- "Which of my Meta ads are actually working?"
- "Why is this ad failing?" / "Is the hook bad or the landing page?"
- "Are my ads tired?" / "Is this creative worn out?"
- "What should I scale, and how fast?" / "What should I kill?"
- "Do we need more creative, or more budget?"

Do not load it for account-level return questions ("is Meta paying back overall?").
Those belong to `ssi-meta-budget-advice`, and for a brand whose Meta ads send buyers to
Amazon, `ssi-meta-amazon-attribution-scoring`. This skill is about one ad at a time.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-creative-diagnosis`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `meta_metric` · `score_creative_metrics` · `tiktok_metric` · `log_decision` · `register_prediction` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
