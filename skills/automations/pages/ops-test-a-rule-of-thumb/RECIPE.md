# Is your team's rule of thumb actually true?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your team's rule of thumb actually true?" (id: ops-test-a-rule-of-thumb, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every team runs on rules of thumb. This tests one against the brand's own past before it shapes a plan. It is the cheapest way to avoid a strategy built on something that was never true for this business.

What to read: Your own customer and order history, split the way the rule says
What to give me: Whether a rule your team relies on was true in your own history, and by how much

Synthesis tools to use:
- `cost_rules for=ops-test-a-rule-of-thumb`
- `backtest_rule`
- `query_series metric=gateway_repeat asin=<asin>`
- `product_ltv asin=<asin>`

Steps:
1. Ask for the rule in one sentence and turn it into a comparison: which group, which metric, which direction, and how big a difference counts.
2. Run `backtest_rule name=<rule> population=<who> metric=<metric> split=<groups> direction=<higher|lower> comparison=<ratio|difference> threshold=<size>`.
3. Cross-check one side with a governed read, such as `product_ltv asin=<asin>` or `query_series metric=gateway_repeat asin=<asin>`.
4. Report whether the rule held, the size of the difference, and the group sizes.

Checks before answering:
- Both groups must have had the same time to show the result. Young customers have not had time to repeat.
- A small group (under 200) cannot settle a rule. Say so.
- A rule that held in the past can stop holding. Say the period tested.

Output:
- Three lines per rule: held or not, the measured difference, and the group sizes and period.

Never:
- Never call a rule proven on a small group.
- Never stretch the result beyond the period and channel tested.
- Never change a plan on the person's behalf.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-test-a-rule-of-thumb". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
