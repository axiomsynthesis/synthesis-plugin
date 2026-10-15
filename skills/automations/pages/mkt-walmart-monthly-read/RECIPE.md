# Your Walmart month on one page

Channel: Walmart · Level: On a schedule · Status: Ready now
Schedule: monthly on the 3rd, 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your Walmart month on one page" (id: mkt-walmart-monthly-read, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A short monthly read of Walmart Marketplace: sales, growth, cancels and concentration, with one action.

What to read: Walmart Marketplace orders, units, sales, cancel rate and top items by month
What to give me: A one-page monthly read of your Walmart Marketplace business, with the one thing to fix

Synthesis tools to use:
- `walmart_metric metric=revenue months=13`
- `walmart_metric metric=orders_trend months=13`
- `walmart_metric metric=top_skus months=1 limit=15`
- `walmart_metric metric=catalog_health`

Steps:
1. Call `walmart_metric metric=revenue months=13`. Read the data window first.
2. Call `walmart_metric metric=orders_trend months=13` for cancel rate.
3. Call `walmart_metric metric=top_skus months=1 limit=15`.
4. Call `walmart_metric metric=catalog_health` for items not live.
5. Write the read: sales, change on last month and last year, cancel rate, top two items' share, and one fix.

Checks before answering:
- If orders stop months ago, the connection may be dead. Say so instead of reporting a collapse.
- This is order value, not what Walmart paid. Never call it payout.
- Use the last closed month as the headline.

Output:
- Five lines: sales, month change, year change, cancel rate, the one fix.
- A table of the top items.

Never:
- Never send the read anywhere the person has not set up.
- Never change anything in Walmart Seller Center.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-monthly-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (monthly on the 3rd, 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
