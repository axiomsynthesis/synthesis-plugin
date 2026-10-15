# Where should the next ad dollar go?

Channel: Growth · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where should the next ad dollar go?" (id: grw-next-dollar-split, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each channel gets less efficient as you spend more. This estimates what the next $10,000 buys in each channel and proposes moving budget from the flattest curve to the steepest, with a simulation of the range of outcomes.

What to read: Diminishing returns curves for Meta and the other paid channels
What to give me: A budget split for next month, based on what the next dollar buys in each channel

Synthesis tools to use:
- `meta_metric metric=efficiency_curve`
- `google_ads_metric metric=impression_share days=30 limit=25`
- `tiktok_metric metric=spend_trend months=6`
- `run_scenario scenario_type=budget_shift`

Steps:
1. Pull `meta_metric metric=efficiency_curve`.
2. Pull `google_ads_metric metric=impression_share days=30 limit=25` for budget-limited campaigns with headroom.
3. Pull `tiktok_metric metric=spend_trend months=6`.
4. Rank channels by marginal return at current spend.
5. Run `run_scenario scenario_type=budget_shift from_channel=<flat> to_channel=<steep> amount_monthly=<value> contribution_margin_pct=<value>` and report the middle and the downside.

Checks before answering:
- A curve fit on under 8 weeks of spend changes is weak. Say so.
- Never move more than 20% of a channel in one month.
- Platform return is not incremental. Name the haircut used.

Output:
- Answer first. Table: channel, spend now, return on the next dollar, proposed spend. Scenario middle and downside.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- A person changes budgets.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-next-dollar-split". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
