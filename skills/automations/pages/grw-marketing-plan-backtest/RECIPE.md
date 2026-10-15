# Test a marketing belief on your past

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Test a marketing belief on your past" (id: grw-marketing-plan-backtest, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes a belief like discount buyers never come back, or bundles bring better customers, and checks whether it held in your own history before you build a plan on it.

What to read: Your own sales history and a rule you believe
What to give me: Whether a marketing belief actually held in your own history

Synthesis tools to use:
- `backtest_rule`

Steps:
1. Ask for the rule in one sentence.
2. Turn it into a population, a metric, a split and a direction.
3. Run `backtest_rule name=<rule> population=<who> metric=<what> split=<groups> direction=<higher or lower> comparison=<ratio or difference> threshold=<value>`.
4. Say plainly: held, did not hold, or not enough data.

Checks before answering:
- State the sample sizes on both sides.
- A held rule is an association, not a cause.

Output:
- Answer first: held or not. The two numbers, sample sizes and one line on what to do.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-marketing-plan-backtest". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
