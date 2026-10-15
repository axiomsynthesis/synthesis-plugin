# What could seriously hurt the business?

Channel: Leadership · Level: On a schedule · Status: Ready now
Schedule: monthly, 1st business day 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What could seriously hurt the business?" (id: ops-risk-register, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Keeps a short, ranked list of the ways the business could get badly hurt, and checks them monthly against measured numbers. Unlike a pre-mortem on one decision, this covers the whole company and moves as the numbers move.

What to read: Paid growth dependence, cash, channel and customer concentration, margins and stock risk
What to give me: A monthly ranked list of the biggest risks, each with a measured tripwire

Synthesis tools to use:
- `strategy_framework framework=death_mode_risk_zones`
- `strategy_framework framework=premortem_score`
- `channel_revenue_mix`
- `customer_concentration`
- `amazon_metric metric=days_of_cover limit=50`
- `mer month=YYYY-MM`

Steps:
1. Pull the inputs: `channel_revenue_mix` and `customer_concentration` for dependence, `mer month=YYYY-MM` for paid growth reliance, `amazon_metric metric=days_of_cover limit=50` for stock risk on top products, and margin from closed books if connected.
2. Run `strategy_framework framework=death_mode_risk_zones`. It reads the brand's own figures, so set its zones beside the inputs above.
3. List candidate risks with a chance from 0 to 1, an impact from 1 to 10 and how hard each is to see coming from 0 to 1. Run `strategy_framework framework=premortem_score failure_modes=[{name, prob, impact, detection_penalty}]` to rank them.
4. For each of the top five, set a tripwire on a measured metric and an owner.
5. Compare with last month's register: new, rising, falling, retired.

Checks before answering:
- The company channel split is heavily modelled. If its own flag says unreliable, use invoiced revenue by account instead and say so.
- A risk zone the tool marks as not modelled is unknown, not zero.
- Probabilities and impacts are judgement. Label them as the team's.

Output:
- Table: Risk | Measured signal now | Tripwire | Probability | Impact | Owner | Change since last month.
- Two lines: the risk that rose most and the one action to reduce it.

Never:
- Never present a judged probability as measured.
- Never drop a risk because its data went missing.
- Never take an action on a risk.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-risk-register". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (monthly, 1st business day 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
