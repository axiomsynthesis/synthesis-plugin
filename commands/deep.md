---
description: "A deep answer on your own Claude: specialist helpers at once, a skeptic who re-pulls every number, then a checked answer"
argument-hint: "[your question]"
disable-model-invocation: true
---

# A deep answer, on this Claude

The question: $ARGUMENTS

If no question came with /deep, ask for it in one line and stop.

This runs on the person's own Claude plan. Do not call `deep_synthesis` at any step:
that is the separate server-run deep answer, and the person chose this one.

## 1. Frame it (you, before anyone else)

- Call the Synthesis tool `brand_context_frame` once, if this session has not yet.
- Call `brand_brain` for what this week's warnings already say about the question.
- Write a frame of five short lines, for yourself and the helpers: the real decision
  underneath the question; the brand; today's date and the last fully closed week and
  month; which channels the question touches; the one thing that would change the call.

## 2. Send the helpers out, all at once

In ONE message, start the helpers this question needs, in parallel. Each is a
subagent this plugin ships; its name in your agent list starts with `synthesis:`.

- `amazon-analyst`: Amazon sales, traffic, conversion, stock, search, reviews.
- `ads-analyst`: Amazon Ads, Meta, Google and TikTok spend and return.
- `customer-analyst`: the website, repeat buying, customer groups, subscriptions, email.
- `money-analyst`: profit after every cost, margins after fees, cash, what-ifs.

Give each one the question word for word, your frame and the date window. Skip a
helper only when its area plainly has nothing to do with the question, and say which
you skipped and why.

## 3. Write the draft

From their findings only, write the answer in the house voice, in the order a
strategy or "why" answer takes. Every number you use must come from a finding that
names its source. Where two helpers disagree, say so and say which number is senior
(measured beats inferred; money in the bank beats orders placed).

## 4. Send the skeptic

Start the `skeptic` subagent with the question, your draft and every helper's
findings. Fix everything it marks Wrong, Unsourced or Missing its warning. If its
verdict is "Does not hold", rewrite the call; do not argue with it.

## 5. Check the finished draft

Call the Synthesis tool `check_reasoning` with `metric` set to `draft`, the whole
answer as `draft` and the question as `question`. Fix every problem it lists and
run it once more. If a check could not run, say so in the answer's last line.

## 6. Answer

Give the person the checked answer. Under it, one line: which helpers ran, that every
number was pulled twice, and what the checks do not cover (the result lists it).
The answer saves itself to the brand's memory when you finish; do not save it.
