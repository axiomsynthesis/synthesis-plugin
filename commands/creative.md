---
description: "Synthesis Creative: your creative strategist. Which ads stop, warm and close, which hooks, storylines and offers win, then five ready-to-shoot concepts, each checked and saved"
argument-hint: "[optional: a product, a channel, or anything to focus on]"
disable-model-invocation: true
---

# Synthesis Creative

Focus for this run, if any: $ARGUMENTS

Pull the method first: call the Synthesis tool `get_skill` with name
`ssi-creative`, and follow it step by step.

1. Call `winning_hooks` with `view` set to `strategist`. If it answers with
   `gated: true`, stop: tell the person what Synthesis Creative does and what
   it costs, exactly as its `upgrade` block says, and give them
   `upgrade.checkout_url`. Nothing else runs.
2. Show where the money sits by job (stoppers, warmers, closers), the best
   ads at each job, and the ads that fill carts other ads close. Then the
   winning hook, creative, storyline and offer for each job, each against the
   brand's own average. Keep thin rows apart as tests.
3. Call `winning_hooks` with no view for the hooks that sell over 90 days and
   the demand behind them, then check what rivals run.
4. Write five concepts. Each names the job it is built for (stop, warm or
   close), the hook, storyline and offer it builds on, the number that proves
   them, and the index it must beat. If the focus above names a product or a
   channel, all five fit it.
5. Run every concept through `ssi-ad-preflight`. Drop and name any that
   still fails.
6. Save each passing concept to the ideas list with `ad_idea_bank`, then
   show the person the five, the proof behind each, and that they are saved.
