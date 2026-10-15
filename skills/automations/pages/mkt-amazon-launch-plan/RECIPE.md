# Plan a new product launch

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan a new product launch" (id: mkt-amazon-launch-plan, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds a launch plan from your own data: the searches to win, a launch price, a weekly ad budget, a review goal and the stock to send.
It uses a past launch of yours as the yardstick so the plan is not wishful.

What to read: Search demand and rivals for the new product's searches, how a similar past launch of yours ramped, break-even ad cost and the live shelf
What to give me: A 60-day plan with target searches, launch price, weekly ad budget, review goal and stock to send, built from your past launches

Synthesis tools to use:
- `amazon_metric metric=search_query_performance grain=month periods=3 scope=nonbranded top=50`
- `amazon_metric metric=search_competitors grain=week periods=4 top=20`
- `scrape_amazon_search k=20`
- `amazon_metric metric=velocity_momentum weeks=26`
- `breakeven_roas`
- `export_xlsx`

Steps:
1. Ask for the product, its cost, target price and the closest past launch you have.
2. Call `amazon_metric metric=search_query_performance grain=month periods=3 scope=nonbranded top=50` and pick 5 to 8 searches that fit the product.
3. Call `amazon_metric metric=search_competitors grain=week periods=4 top=20` for who leads those searches. Rival data comes by the week only, so read the last four closed weeks.
4. Call `scrape_amazon_search keyword=<main search> k=20` once for the live price ladder and review counts.
5. Call `amazon_metric metric=velocity_momentum asin=<similar past launch> weeks=26` for how that launch ramped.
6. Call `breakeven_roas` with the planned price, cost and fees to set the ad ceiling after launch.
7. Build the plan with `export_xlsx`: weekly rows for 8 weeks with price, ad budget, ad cost share cap, units expected, reviews goal; plus a tab for target searches.

Checks before answering:
- If there is no similar past launch, say the ramp is a guess and use a cautious one.
- Fees for a new product are estimates until the first settlement. Label them.
- Scraped shelf data draws on a shared monthly allowance. One call only.
- Shares are percentages. Never rescale.

Output:
- Five lines: searches, price, budget, review goal, units to send.
- File `launch_plan_<product>.xlsx`.
- The day 7, 30 and 60 numbers that say the launch is on track.

Never:
- Never create listings, ads or shipments.
- Never promise the ramp will match the past launch.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-launch-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
