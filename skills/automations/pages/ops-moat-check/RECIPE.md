# What really protects your profits?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What really protects your profits?" (id: ops-moat-check, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks which of the classic lasting advantages the business really has: scale, network effects, a position rivals cannot copy, switching costs, brand, a scarce resource, or a process edge. Each must be backed by a number or it is marked "claimed, not shown".

What to read: Repeat rates, subscription share, price premium over rivals, branded search, cost per unit at scale and review counts
What to give me: Which lasting advantages the business actually has, which it only claims, and the evidence for each

Synthesis tools to use:
- `cost_rules for=ops-moat-check`
- `classify_moat`
- `strategy_framework framework=score_counter_position`
- `amazon_metric metric=ppc_branded_split`
- `amazon_metric metric=sns_program`
- `amazon_metric metric=shelf_position`
- `brand_ltv`

Steps:
1. Gather evidence: `amazon_metric metric=sns_program` and `brand_ltv` for switching costs, `amazon_metric metric=ppc_branded_split` for brand pull, `amazon_metric metric=shelf_position` for price premium held, cost per unit trend for scale.
2. Rate each advantage 0 to 10 with a line of evidence.
3. Run `classify_moat` with the ratings.
4. If a counter-position is claimed, run `strategy_framework framework=score_counter_position uniqueness=<0-10> defensibility=<0-10> lockout=<0-10> resonance=<0-10>` on it.
5. List claimed advantages with no evidence.

Checks before answering:
- A price premium held while losing share is not brand power.
- Subscription share must be measured on live subscriptions, not a past peak.
- Small brands rarely have scale or network effects. Say so plainly rather than stretching.

Output:
- Table: Advantage | Rating | Evidence | Status (shown, claimed, absent).
- Two lines: the strongest real advantage and the one cheapest to build.

Never:
- Never rate an advantage without evidence.
- Never copy any book's text.
- Never present the result as a valuation input without saying it is judged.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-moat-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
