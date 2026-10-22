---
description: "Did that deal make money?: The profit the deal really added after the discount, the ads and the dip that followed, and whether to run it again"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Did that deal make money?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did that deal make money?" (id: amazon-deal-and-coupon-after-action, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Asks if your last deal or coupon made money or just moved sales around. It compares profit in the deal and the weeks after with a normal baseline, after the price cut, ads and the dip.

What to read: Daily profit and sales, weekly price per unit, promotions, ads, new buyers and Subscribe and Save sign-ups
What to give me: The profit the deal really added after the discount, the ads and the dip that followed, and whether to run it again

Synthesis tools to use:
- `cost_rules for=amazon-deal-and-coupon-after-action`
- `amazon_metric metric=promotion_performance months=3`
- `amazon_metric metric=pnl_daily start_date=YYYY-MM-DD end_date=YYYY-MM-DD`
- `amazon_metric metric=daily_revenue start_date=YYYY-MM-DD end_date=YYYY-MM-DD tz=America/Los_Angeles`
- `amazon_metric metric=ppc_trend weeks=13`
- `amazon_metric metric=velocity_momentum weeks=12 limit=20`
- `amazon_metric metric=ppc_ntb start_date=YYYY-MM-DD end_date=YYYY-MM-DD`
- `amazon_metric metric=sns_program weeks=12`
- `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`

Steps:
1. Use the event dates the person gives. If none, take the clearest sales bump in the daily numbers and say in the first line that the dates are your assumption.
2. Baseline: the 4 weeks ending 8 days before the event, so the quiet week before it is left out. After: the 21 days after. If 21 days have not passed, say how many have.
3. Call `amazon_metric metric=pnl_daily start_date=YYYY-MM-DD end_date=YYYY-MM-DD` from baseline start to the end of the after window, in one call if you can: per-day figures shift with the window. If it times out, split it and say so. Note `estimated_parts` and `settled_through`.
4. Call `amazon_metric metric=daily_revenue start_date=YYYY-MM-DD end_date=YYYY-MM-DD tz=America/Los_Angeles` for the same span, so deal days match Amazon's days.
5. Call `amazon_metric metric=ppc_trend weeks=13` for the ad spend rise.
6. Call `amazon_metric metric=velocity_momentum weeks=12 limit=20`. Price per unit is `net_revenue` over `units`. Price cut = (baseline price minus event-week price) x event-week units. Deal prices sit in the item price, so promotions miss them.
7. Call `amazon_metric metric=promotion_performance months=3` for coupons in the window.
8. Event profit = profit in the event and after windows, minus baseline profit per day x the same days. The dip is inside it.
9. Call `amazon_metric metric=ppc_ntb start_date=YYYY-MM-DD end_date=YYYY-MM-DD` for event days, `amazon_metric metric=sns_program weeks=12` for Subscribe and Save sign-ups, and `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`. Value each new buyer at the 3-month `ltv_contribution` minus `first_order_contribution`.

Checks before answering:
- If over half the event days' fees are estimated, or deal fees have not posted, call the profit provisional and give the settle-by date. Deal fees often post after the event.
- If profit data is missing for any day, say so. Never fill it with a guess or a zero.
- Count the dip after. Pulled-forward sales are not new.
- Drop baseline days with another event or a big ad push, and say so.
- The weekly price table can lag a week. If the event week is missing, say the price cut is not known yet.
- New-to-brand buyers are only those credited to ads, a floor. Never add their value into the headline.
- One deal is one data point. A bump can be a holiday or an ad push, so an assumed window stays labelled.
- This cannot yet compare with last year's same event.

Rounds (relook before you answer):
1. **Settled yet?** Re-read `estimated_parts` and `settled_through` from step 3. Fails when: over half the event days still hold estimated fees. Fix: call it provisional and give the date to run it again. On that later run, fails when profit moved over 15% from the provisional figure. Fix: say how much, and why.
2. **Second baseline.** Re-run step 8 with the 8 weeks ending 8 days before the event. Fails when: event profit changes sign or moves over 30%. Fix: say the answer depends on the baseline and show both.
3. **Dip length.** Re-read days 15 to 21 after the event. Fails when: daily sales there are still over 10% under baseline. Fix: stretch the after window to 35 days and redo step 8.
4. **Argue the losing case.** Compare the price cut given away with the profit added. Fails when: the price cut is over 3x the profit added. Fix: say the deal mostly paid buyers who would have bought, and suggest a shallower depth next time.
5. **Other causes.** Re-read the daily sales and ad spend. Fails when: a day in the after window had no orders, or ad spend in the baseline swung over 30% week to week. Fix: drop those days, say why, and redo step 8.

Output:
- First line: profit the deal added against a normal baseline, after price cut, ads and dip, and whether it is provisional.
- A table: period, days, sales, price cut, ad spend, profit, profit per day.
- A separate line: new buyers, Subscribe and Save sign-ups, and their 90-day value.
- One move: run it again, change the depth, or skip it.

Never:
- Never create or change a deal or coupon in Seller Central. A person does that.
- Never guess a cost the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-deal-and-coupon-after-action". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
