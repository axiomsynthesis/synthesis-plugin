---
description: "Synthesis Creative: five ready-to-shoot ad concepts built on the hooks that already make money, each checked and saved"
argument-hint: "[optional: a product, a channel, or anything to focus on]"
disable-model-invocation: true
---

# Synthesis Creative

Focus for this run, if any: $ARGUMENTS

Pull the method first: call the Synthesis tool `get_skill` with name
`ssi-creative`, and follow it step by step.

1. Call `winning_hooks`. If it answers with `gated: true`, stop: tell the
   person what Synthesis Creative does and what it costs, exactly as its
   `upgrade` block says, and give them `upgrade.checkout_url`. Nothing else
   runs.
2. List the winners and the promising hooks, one line each, kept apart. If
   there are no winners yet, say so and build on promising hooks as tests.
3. Check the demand behind each winner, then what rivals run.
4. Write five concepts that double down on the winners. If the focus above
   names a product or a channel, all five fit it.
5. Run every concept through `ssi-ad-preflight`. Drop and name any that
   still fails.
6. Save each passing concept to the ideas list with `ad_idea_bank`, then
   show the person the five, the proof behind each, and that they are saved.
