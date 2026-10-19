# Was it price, volume or mix?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Was it price, volume or mix?" (id: ops-price-volume-mix-bridge, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits a revenue change into plain causes: more or fewer units, higher or lower price per unit, a shift toward pricier or cheaper products, and products that were new or dropped. It compares like with like, so a sale event that moved between months is not read as a price or volume change.

What to read: Units and net revenue per product for two periods on Amazon
What to give me: How much of a revenue change came from units, price, mix, and new or dropped products

Synthesis tools to use:
- `cost_rules for=ops-price-volume-mix-bridge`
- `query_series metric=units grain=month asin=<asin>`
- `query_series metric=net_revenue grain=month asin=<asin>`
- `top_products metric=revenue top_n=25 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `brand_brain action=moves kind=promotion`
- `query_series metric=units grain=week`
- `emit_chart type=waterfall`

Steps:
1. Pick the two periods. By default, the last 12 closed months against the 12 before. If the person picks a quarter or a month, call `brand_brain action=moves kind=promotion` with `since` and `until` covering both periods, to find big sale events such as Prime Day. The move log holds the brand's own logged events. If it shows none, call `query_series metric=units grain=week` over both periods and treat a week far above its neighbours as a sale event. If only one period has one, move the window so both do or neither does, and say so.
2. Call `top_products metric=revenue top_n=25` with `start_month` and `end_month` set to each period to choose the products that make up most of revenue. Put everything else in an "all other" row.
3. That read gives revenue and units per product. Only for a product whose units are missing, call `query_series metric=units grain=month asin=<asin>` and `query_series metric=net_revenue grain=month asin=<asin>` over both periods.
4. Sort products into three groups: sold in both periods, new (later period only) and dropped (earlier period only). New and dropped products are their own bars, at their own revenue.
5. For products sold in both periods only: price per unit = revenue divided by units. Volume = change in their total units times the earlier period's average price. Price = sum of later units times the change in that product's price. Mix = sum of (later share minus earlier share) times later total units times the earlier price.
6. Draw it with `emit_chart type=waterfall`. Pass the earlier total first, then only the volume, price, mix, new and dropped changes. Never pass the later total as a last bar: it would be stacked on top. The top of the last step is the later total. Say that figure in the summary.

Checks before answering:
- The bars must add to the total change within $1. If they do not, show the gap as "unexplained" and never fold it into mix.
- Revenue here is after promotions, so deeper coupons and deals show up as price. Say so beside the price bar. A split of list price from discount depth is not available yet.
- If you moved a period to line up a sale event, say which event and the new dates.
- Compare whole periods only. Leave out the running month.

Output:
- One line first: the main driver in dollars and what to do about it.
- Chart plus table: Effect | Dollars | Share of the change.
- A second table for the top five products by contribution to the change, with new and dropped products named.
- One line on the one to watch.

Never:
- Never mix order-basis revenue with settlement revenue in one bridge.
- Never compare a part month.
- Never change prices.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-price-volume-mix-bridge". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
