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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: plan-tiktok-gmv-max-pause-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
