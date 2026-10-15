---
description: "Run any Synthesis automation by name, like /go fee check"
argument-hint: "<automation name, like fee check or reorder plan>"
disable-model-invocation: true
---

# Run a Synthesis automation

The person asked for: $ARGUMENTS

1. Load the Synthesis automations skill. Its table lists every automation by
   id and title, and each one has its own page.
2. If the person typed nothing after /go, say in one line: type /go and a
   name, like /go fee check, to run any automation. Then list these five
   with a few words each and stop: /fees, /stockout, /reorder, /whyprofit,
   /adloss.
3. Otherwise find the automation that best matches what they typed, by its
   title, its id or what it does.
   - One clear match: name it in one line, read its page, and follow it step
     by step with the Synthesis tools. Do not ask them to confirm.
   - Two or three could fit: list them, one line each, and ask which one.
   - Nothing fits: say so and list the three closest.
4. Words after the automation's name are extra instructions for this run,
   such as a product, a month or a channel. Apply them.
