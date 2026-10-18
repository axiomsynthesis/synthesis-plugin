---
description: "Where should the next ad dollar go?: A budget split for next month, based on what the next dollar buys in each channel"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

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
- `cost_rules for=grw-next-dollar-split`
- `meta_metric metric=efficiency_curve`
- `meta_metric metric=weekly_trend weeks=13`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `tiktok_metric metric=spend_trend months=6`
- `run_scenario scenario_type=budget_shift`

Steps:
1. Pull `meta_metric metric=efficiency_curve`. It withholds campaigns that send shoppers to Amazon, so also pull `meta_metric metric=weekly_trend weeks=13` and use `amazon_sales_per_dollar` for Amazon-bound spend.
2. Pull `google_ads_metric metric=efficiency_trend weeks=13` and read `amazon_sales_per_dollar` for the Amazon-bound weeks.
3. Pull `tiktok_metric metric=spend_trend months=6` and read `shop_ad_roas` for TikTok.
4. Rank channels by marginal return at current spend.
5. Run `run_scenario scenario_type=budget_shift from_channel=<flat> to_channel=<steep> amount_monthly=<value> contribution_margin_pct=<value>` and report the middle and the downside. When it returns NOT SIMULATED, report the break-even it gives and the measured ceilings, never a split.

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
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-next-dollar-split". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
