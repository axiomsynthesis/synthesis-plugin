---
description: "Which Meta ads for Amazon to keep, cut or move up: Keep, cut and move-up lists for Amazon-bound Meta ads, each ad with its spend, return, orders and the dollars a week at stake, judged by the brand's own ad rules"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Meta ads for Amazon to keep, cut or move up

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Meta ads for Amazon to keep, cut or move up" (id: meta-amazon-keep-cut-promote, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Judges every Meta ad that sends shoppers to Amazon by Amazon's own orders, not Meta's.
Meta cannot see Amazon sales, so it joins Amazon Attribution to Meta spend per ad.
Then it applies the brand's ad rules and hands back keep, cut and move-up lists with the dollars at stake.
Changes go through "Switch Meta ads on or off for me" and "Change a Meta budget for me".

What to read: Meta spend for every ad that sends shoppers to Amazon, the Amazon orders and sales Amazon Attribution credits to each, over the last two closed weeks, each product's Amazon margin and each ad's campaign and daily budget
What to give me: Keep, cut and move-up lists for Amazon-bound Meta ads, each ad with its spend, return, orders and the dollars a week at stake, judged by the brand's own ad rules

Synthesis tools to use:
- `cost_rules for=meta-amazon-keep-cut-promote`
- `meta_metric metric=amazon_ads period=weekly weeks=3`
- `meta_metric metric=ad_daily_trend days=14`
- `amazon_metric metric=contribution_by_asin months=3`
- `ad_health_check`

Steps:
1. Call `meta_metric` with `metric=amazon_ads`, `period=weekly` and `weeks=3`. The newest closed week is the 7-day read. The two newest together are the 14-day read. Return is Amazon sales over Meta spend.
2. If it says unavailable, no_linked_ads or error, stop and say why. Never treat it as zero orders. If linked spend is under 80%, say so first.
3. Ask, in one message, what only the owner knows. The return bar for each product family. Default: 1.5 for one family, 1.2 for a higher-margin one. Any sale days in these weeks. Which campaigns an outside agency runs. The agency or influencer bill for the period.
4. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3`. The break-even return for a product is 1 over its margin share after Amazon fees.
5. Call `ad_health_check` with `ads={"ad_ids": ["<id>"]}` and `only=["schedule_budget","switched_on"]` for each ad you would cut or move up. Read its campaign, daily budget and switches.
6. Sort each ad as a test (first ran in the last 28 days) or scaling. Apply the default rules, each one overridable by the owner:
   - Test ad: cut at $150 spent with no Amazon order. Cap test ads at $75 a day.
   - Move up at $300 spent with the 14-day and 7-day returns both at or above the bar, and 10 or more orders.
   - Scaling ad: cut when the return is under 1.0 after $500 spent, on both windows.
   - The two windows must agree. If they do not, hold.
   - Leave out any day in the last 2 days, and any week with a big sale day in it.
7. For each cut, call `meta_metric` with `metric=ad_daily_trend`, `ad_id=<id>` and `days=14`. An ad whose spend and return are both climbing is ramping. Hold it.
8. Dollars at stake: for a cut, its weekly spend minus the Amazon profit it brings. For a move up, the profit at its return on the extra budget.

Checks before answering:
- Agency or influencer bills are their own cost line. Never add them to Meta spend or hide them in the return.
- Savings are real only if the budget comes down when ads go off. Otherwise Meta spends the same money on the other ads. Say so on every cut.
- Campaigns an outside agency runs go in their own list. The owner decides.
- Ads that share one Amazon link are one row. Never split their sales.
- Amazon keeps crediting orders for 14 days after a click. Say when the newest week has not settled.

Rounds (relook before you answer):
1. **Second window.** Re-read every cut and move-up on the 7-day week alone. Fails when: an ad's 7-day return sits on the other side of the bar from its 14-day return. Fix: move it to hold.
2. **Still settling.** Re-read the unsettled week with the 2-day lag removed. Fails when: an ad cut for no order has an order inside the last 2 days, or its return rises past the bar. Fix: hold it a week.
3. **Bar vs margin.** Check each family's bar against step 4. Fails when: a bar is under that family's break-even return, so a kept ad loses money. Fix: raise the bar and re-sort.
4. **Order count.** Fails when: a move-up rests on fewer than 10 orders. Fix: back to keep.
5. **Argue the losing case.** For the biggest cut, make the case to keep it from the daily trend. Fails when: spend rose in the last 7 days and return rose with it. Fix: hold as ramping.
6. **Money adds up.** Fails when: the cut savings exceed the spend those ads had, or the budget is not lowered. Fix: say no money is saved yet.

Output:
- One line first: 14-day spend, Amazon sales and return, and the dollars a week at stake.
- Cut: each ad, spend, orders, return on both windows, the rule, and the budget to lower.
- Move up: each ad, return on both windows, orders, and the suggested budget, never over $75 a day for a test.
- Keep, hold and agency lists: one line each.

Never:
- Never change, pause or raise an ad. A person does that.
- Never put an outside agency's campaign on the cut list without the owner's word.
- Never judge an Amazon-bound ad on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-amazon-keep-cut-promote". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
