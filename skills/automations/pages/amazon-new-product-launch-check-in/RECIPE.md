# How's the new product launch going?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How's the new product launch going?" (id: amazon-new-product-launch-check-in, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Gives a day 7, day 30 or day 60 readout for a new product. It puts sales, page visits, conversion, reviews and ad cost next to the launch goal, and says what is holding the launch back.

What to read: Sales, sessions, reviews, ads
What to give me: A day 7, 30 or 60 scorecard against your launch goal, and the one thing holding it back

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=plan_vs_actual`
- `amazon_metric metric=velocity_momentum`
- `amazon_metric metric=conversion_funnel`
- `amazon_metric metric=review_velocity`
- `amazon_metric metric=ppc_profit_by_asin`

Steps:
1. Use `find_product` to get the new product's ID and launch date.
2. Call `amazon_metric` with `metric=plan_vs_actual` to read the launch goal you set.
3. Call `amazon_metric` with `metric=velocity_momentum` and the product's `asin` for sales pace since launch.
4. Call `amazon_metric` with `metric=conversion_funnel`, the `asin` and `days=30` for page visits and conversion.
5. Call `amazon_metric` with `metric=review_velocity` and `days=60` for review count and rating so far.
6. Call `amazon_metric` with `metric=ppc_profit_by_asin` for the current month (or `month=` set to the last closed month) for ad spend and profit after ads.

Checks before answering:
- If no launch goal is stored, say so and compare to your other products instead. Never invent a goal.
- A week of data is too little for a trend. On day 7, say what to watch, not what is true.
- If any tool returns nothing for the product, say that number is missing.

Output:
- One line first: percent of goal reached and the one thing holding it back.
- A scorecard table: measure, goal, actual, status.
- One move for the next 30 days and the number that will show it worked.

Never:
- Never change ads, price or the listing. A person does that.
- Never guess a goal or a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-new-product-launch-check-in". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
