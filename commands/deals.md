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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-deal-and-coupon-after-action". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
