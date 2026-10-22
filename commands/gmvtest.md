---
description: "Plan and read a TikTok GMV Max pause test: A written pause test with dates and the result that would prove it wrong, then the readout of whether GMV Max really sells"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Plan and read a TikTok GMV Max pause test

Channel: TikTok Shop · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan and read a TikTok GMV Max pause test" (id: plan-tiktok-gmv-max-pause-test, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
GMV Max reports its own sales, and they run high. This plans a pause test: stop GMV Max, hold other ads steady, and see what really falls in the shop and on Amazon. You pause it yourself.

What to read: GMV Max spend, TikTok Shop sales net of samples and cancels, shop profit, Amazon branded searches and Amazon profit per unit
What to give me: A written pause test with dates and the result that would prove it wrong, then the readout of whether GMV Max really sells

Synthesis tools to use:
- `cost_rules for=plan-tiktok-gmv-max-pause-test`
- `tiktok_metric metric=shop_ad_efficiency months=6`
- `tiktok_metric metric=shop_sales_trend months=6`
- `tiktok_metric metric=shop_profit`
- `tiktok_metric metric=spend_trend months=6`
- `tiktok_metric metric=campaign_leaderboard months=1`
- `amazon_metric metric=search_query_trend grain=week periods=12`
- `amazon_metric metric=contribution_by_asin months=1`
- `meta_metric metric=weekly_trend weeks=12`
- `register_prediction`
- `log_decision kind=campaign`

Steps:
1. Ask: pause length (default 2 weeks), start date (default next Sunday, to match Amazon's Sunday to Saturday weeks), whole shop or one product.
2. Call `tiktok_metric` with `metric=shop_ad_efficiency` and `months=6`. Compare GMV Max's own sales with real shop sales for two closed months.
3. Call `tiktok_metric` with `metric=shop_sales_trend` and `months=6` for shop sales net of cancels and free samples.
4. Call `tiktok_metric` with `metric=shop_profit`. If it times out, retry once without context. If product costs are missing, judge on sales only.
5. Weekly GMV Max spend divided by the shop's margin is the shop sales it must add. If that beats the whole shop's weekly sales, it cannot pay on the shop. The test is then only about Amazon.
6. Call `tiktok_metric` with `metric=spend_trend` for weekly spend, then `metric=campaign_leaderboard` with `months=1`. Its totals run from each campaign's first spend. Use last_day and days_since_last_spend to list campaigns still spending.
7. Call `amazon_metric` with `metric=search_query_trend`, `grain=week` and `periods=12`, every result_page, for branded searches. Call `amazon_metric` with `metric=contribution_by_asin` and `months=1`. Profit per unit is total_contribution over units. Break-even extra units a week is weekly GMV Max spend over that.
8. Call `meta_metric` with `metric=weekly_trend` and `weeks=12`. Split spend aimed at Amazon from spend aimed at the website.
9. Write the plan: dates, campaigns still spending, spend that stays flat, holdout weeks, the result that proves GMV Max wrong. Save it with `register_prediction` and `log_decision` with `kind=campaign`.
10. The person pauses it. There is no tested browser path or TikTok write access. Give the clicks: Ads Manager, GMV Max, each campaign still spending by name, Pause. Warn this also stops paid boosts on creator posts. Ask first whether an agency pays for those.
11. At the end, read steps 2 to 8 again. Compare pause weeks with holdout weeks.

Checks before answering:
- Safe test: planning changes nothing. A dry run writes the plan only.
- Spend: say GMV Max spend a week. Ad credits are netted out, so billing may show a smaller saving.
- Confirm GMV Max spend was $0 from the start date, or the test did not run.
- If average weekly Meta or Amazon ad spend in pause weeks differs from holdout weeks by over 20%, say the readout is mixed.
- Never add creator platform sales to shop sales.
- Keep sale events, such as a Prime sale week, out of pause and holdout weeks.

Rounds (relook before you answer):
1. **Natural test first.** Re-read step 6's weekly spend. Find a past week where GMV Max spend fell 40% or more against the 4 weeks before, with no sale event. Fails when: in such a week shop sales and Amazon units held within 10%. Fix: say the answer may already be known, and offer a shorter test or none.
2. **Can an Amazon lift pay?** Re-read step 7. Fails when: the extra Amazon units a week needed to break even are over 25% of that product's normal Amazon units. On one live brand GMV Max needed about 129 extra Amazon orders per $1,000 and measured about 20. Fix: say the test is about the shop only.
3. **Clean holdout.** Re-read steps 7 and 8 for the planned weeks. Fails when: Meta spend aimed at Amazon or Amazon ad spend is planned to move over 20%, or a sale event falls inside. Fix: move the dates or hold that spend flat.
4. **Did it really pause?** Two days after the start, re-read step 6. Fails when: any GMV Max campaign shows spend after the start date. Fix: name it and give the pause click again.
5. **Argue the null.** At readout, take the normal week-to-week swing in shop sales across the holdout weeks. Fails when: the drop in the pause weeks is smaller than that swing. Fix: call it not proven and offer 2 more weeks, never a verdict.

Output:
- One line first: what GMV Max really added a week, or the planned dates.
- The plan: dates, campaigns, what stays flat, the result that proves it wrong.
- After the test: shop sales and Amazon orders, pause against holdout weeks, the verdict.

Never:
- Never pause or change a TikTok campaign. The person does it.
- Never judge GMV Max on its own reported sales.
- Never call a profit when product costs are missing.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: plan-tiktok-gmv-max-pause-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
