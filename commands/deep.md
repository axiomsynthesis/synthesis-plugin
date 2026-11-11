---
description: "A deep answer on your own Claude: the Brand Brain, specialist helpers at once, a reasoning check and a skeptic who re-pulls every number, then a checked answer"
argument-hint: "[your question]"
disable-model-invocation: true
---

# A deep answer, on this Claude

The question: $ARGUMENTS

If no question came with /deep, ask for it in one line and stop.

This runs on the person's own Claude plan. Do not call `deep_synthesis` at any step:
that is the separate server-run deep answer, and the person chose this one.

## 1. Ground it (you, before anyone else)

- Call the Synthesis tool `brand_context_frame` once, if this session has not yet.
- Call `brand_brain` with `action` set to `what_matters`: what is at stake this month,
  ranked by dollars. Then with `action` set to `open` and `page` set to the product,
  range or channel the question is about (a name works): its numbers, its links and
  what the brand's facts and files say about it. Note the page ids for the helpers.
- Call `brand_memory` with `past_answers` set to 3 and `about` set to the question's
  main words: what the brand concluded last time. Each was true on its date.
- Call `run_principles_engine` with the question as `query`: the lessons this brand
  has already earned. Treat them as starting beliefs to test, not as findings.

## 2. Frame it

Write the frame, for yourself and every helper, in these lines:

1. The real decision underneath the question.
2. The brand, today's date, and the last fully closed week and month.
3. What the answer needs, each marked in hand, maybe, or missing.
4. What the question takes for granted that might be false (one to three).
5. The sharper question you will actually answer, if it differs.
6. The answer shape to avoid, for example a trend table that never says why.
7. The one thing that would change the call.

## 3. Send the helpers out, all at once

In ONE message, start the helpers this question needs, in parallel. Each is a
subagent this plugin ships; its name in your agent list starts with `synthesis:`.

- `connections-analyst`: what the question is linked to on the Brand Brain, which
  links were tested and held, and our own moves in the same weeks. Send it every time.
- `amazon-analyst`: Amazon sales, traffic, conversion, search, reviews.
- `ads-analyst`: Amazon Ads, Meta, Google and TikTok spend and return.
- `customer-analyst`: the website, repeat buying, customer groups, subscriptions, email.
- `money-analyst`: profit after every cost, margins after fees, cash, what-ifs.
- `rivals-analyst`: competitors, the shelf, search share, rival prices and reviews.
- `stock-analyst`: stock, run-outs, reorders, inbound shipments, cash tied up in stock.

Give each one the question word for word, your frame, the date window and the
Brand Brain page ids from step 1. Skip a helper only when its area plainly has
nothing to do with the question, and say which you skipped and why.

## 4. Write the draft

From their findings only, write the answer in the house voice, in the order a
strategy or "why" answer takes. Every number you use must come from a finding that
names its source. Where two helpers disagree, say so and say which number is senior
(measured beats inferred; money in the bank beats orders placed). A link the map
tested and found did not hold may not carry a "this caused that" sentence.

## 5. Check the reasoning

Start the `reasoning-checker` subagent with the question, your frame, the draft and
every helper's findings. Where it says the call does not follow from the evidence,
change the call or the evidence it rests on. Keep its certificate for the skeptic.

## 6. Send the skeptic

Start the `skeptic` subagent with the question, the draft, every helper's findings
and the certificate. Fix everything it marks Wrong, Unsourced or Missing its warning.
If its verdict is "Does not hold", rewrite the call; do not argue with it.

## 7. Look back once

Read the draft for the one gap that could change the call: something a helper could
not measure that the call leans on, a disagreement left open, or what the skeptic
named as missing. If there is one, send ONE helper back with one narrow question,
then update the draft. One round only. If no gap would change the call, skip this.

## 8. Check the finished draft

Call the Synthesis tool `check_reasoning` with `metric` set to `draft`, the whole
answer as `draft` and the question as `question`. Fix every problem it lists and
run it once more. If it times out, try once more. If a check still could not run,
say so in the answer's last line.

## 9. Answer

Give the person the checked answer. Under it, one line: which helpers ran, that every
number was pulled twice, whether the reasoning check held or changed the call, and
what the checks do not cover (the result lists it).
Then save it to the brand's memory with `capture_turn`: the question and this answer.
