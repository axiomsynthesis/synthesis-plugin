---
description: "What each channel must return to earn the next dollar: Each paid channel's break-even return beside its return today, and a test when no split can be named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What each channel must return to earn the next dollar

Channel: Growth · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What each channel must return to earn the next dollar" (id: grw-next-dollar-split, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each channel gets less efficient as you spend more, and an average return is only a ceiling on what the next dollar buys. This works out the return each paid channel must reach just to pay for itself, from the profit margin of the channel it sells into, and sets it beside the return it shows today. It names a budget split only when a fitted curve and a simulation back it. Otherwise it proposes a short holdout test, where ads are paused for a set time or area, to measure what they really add.

What to read: Each channel's profit before ads, its measured return on ad spend, and diminishing returns curves where one exists
What to give me: Each paid channel's break-even return beside its return today, and a test when no split can be named

Synthesis tools to use:
- `cost_rules for=grw-next-dollar-split`
- `business_profit month=YYYY-MM`
- `meta_metric metric=efficiency_curve`
- `meta_metric metric=weekly_trend weeks=13`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `tiktok_metric metric=spend_trend months=6`
- `run_scenario scenario_type=budget_shift`

Steps:
1. Call `business_profit` with `month=` set to last month. For each sales channel, margin before ads = (profit plus its own ad spend) divided by sales. Break-even return = 1 divided by that margin.
2. Pair each ad source with the channel it sells into. Meta and Google spend that points at Amazon uses Amazon's break-even. Meta spend that points at the website uses the website's. TikTok shop ads use TikTok Shop's.
3. Call `meta_metric` with `metric=weekly_trend` and `weeks=13`. Use `amazon_sales_per_dollar` for Amazon-bound spend and the website return for the rest. Call `meta_metric` with `metric=efficiency_curve` for any fitted curve. It withholds campaigns that send shoppers to Amazon.
4. Call `google_ads_metric` with `metric=efficiency_trend` and `weeks=13` and read `amazon_sales_per_dollar` for the Amazon-bound weeks.
5. Call `tiktok_metric` with `metric=spend_trend` and `months=6` and read `shop_ad_roas`.
6. Rank only on marginal return from a fitted curve. An average return is a ceiling, never the next dollar. If no channel has a fitted curve, give the break-even per channel and propose a 2 to 4 week holdout test instead of a split.
7. Only when a curve exists, run `run_scenario` with `scenario_type=budget_shift from_channel=<flat> to_channel=<steep> amount_monthly=<value> contribution_margin_pct=<value>`. Name a split only when it returns a simulated result. When it returns NOT SIMULATED, report the break-even it gives and the measured ceilings, never a split.

Checks before answering:
- A curve fit on under 8 weeks of spend changes is weak. Say so.
- Daily spend steps inside one campaign over a few days are not a response curve. Do not rank on them.
- Never move more than 20% of a channel in one month.
- Platform return is not incremental. Name the haircut used, or say none is measured.
- Amazon sales per ad dollar is an average over the window and a ceiling from Amazon's own credit. It is not what the next dollar buys.
- If `business_profit` names a channel with missing costs, its margin reads high and its break-even reads low. Say so beside it.

Output:
- Answer first: which channels return less than their break-even today, and whether a split can be named. If it cannot, say so plainly and name the holdout test.
- Table: ad source, sells into, spend now, break-even return, average return today, marginal return if a curve exists.
- If a split is backed: the scenario middle and downside.
- One move: the holdout test to run, which spend to pause, for how long, and the number that decides it.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- A person changes budgets.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never call an average return the return on the next dollar.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-next-dollar-split". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
