# Did that deal make money?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did that deal make money?" (id: amazon-deal-and-coupon-after-action, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks back at your last deal or coupon and asks one question: did it make money, or did it just move sales around? It compares profit during the deal with the weeks before and after, counting the discount and the extra ad spend.

What to read: Orders, promotions, ads
What to give me: The profit the deal really added after the discount, the ads and the dip that followed, and whether to run it again

Synthesis tools to use:
- `cost_rules for=amazon-deal-and-coupon-after-action`
- `amazon_metric metric=promotion_performance`
- `amazon_metric metric=pnl_daily`
- `amazon_metric metric=ppc_trend`
- `amazon_metric metric=daily_revenue`

Steps:
1. Call `amazon_metric` with `metric=promotion_performance` and `months=3` to get each promotion's sales against the discount given. This read carries no deal dates. Use the start and end dates the person gives. If they give none, take the clearest sales bump in the daily numbers, and say in the first line that the window is your assumption and which dates you used.
2. Call `amazon_metric` with `metric=pnl_daily` and `days=90` to get daily profit before, during and after the deal.
3. Call `amazon_metric` with `metric=ppc_trend` and `weeks=13` to see how much ad spend rose around the deal.
4. Call `amazon_metric` with `metric=daily_revenue` and `days=90` to measure the dip in the two weeks after the deal.
5. Work out profit with the deal against a baseline of the two weeks before, minus the dip after.

Checks before answering:
- Use settled days only. The last few days can still change.
- If profit data is missing for any day, say so. Never fill it with a guess or a zero.
- Count the dip after the deal. Sales that were only pulled forward are not new.
- One deal is one data point. Say so before calling deals good or bad in general.
- A sales bump is not proof of a deal. A holiday or an ad push makes the same shape, so an assumed window stays labelled as assumed.

Output:
- One line first: the profit the deal added in dollars, after the discount, ads and the dip.
- A table: period, sales, discount, ad spend, profit.
- One move: run it again, change the depth, or skip it, and how we will know next time.

Never:
- Never create or change a deal or coupon in Seller Central. A person does that.
- Never guess a cost the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-deal-and-coupon-after-action". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
