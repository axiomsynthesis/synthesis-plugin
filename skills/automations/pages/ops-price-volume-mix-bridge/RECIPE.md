# Was it price, volume or mix?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Was it price, volume or mix?" (id: ops-price-volume-mix-bridge, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits a revenue change into three plain causes: more or fewer units, higher or lower price per unit, and a shift toward pricier or cheaper products. It turns "revenue is up 8%" into what actually drove it, so the next decision targets the right lever.

What to read: Units and net revenue per product for two periods on Amazon
What to give me: How much of a revenue change came from more units, from price, and from selling a different mix

Synthesis tools to use:
- `cost_rules for=ops-price-volume-mix-bridge`
- `query_series metric=units grain=month asin=<asin>`
- `query_series metric=net_revenue grain=month asin=<asin>`
- `top_products metric=revenue top_n=25 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `emit_chart type=waterfall`

Steps:
1. Pick the two periods: by default the last full quarter against the same quarter last year.
2. Call `top_products metric=revenue top_n=25` with `start_month` and `end_month` set to each period to choose the products that make up most of revenue. Put everything else in an "all other" row.
3. That read gives revenue and units per product. Only for a product whose units are missing, call `query_series metric=units grain=month asin=<asin>` and `query_series metric=net_revenue grain=month asin=<asin>` over both periods.
4. Price per unit = revenue divided by units, per product per period.
5. Volume effect = change in total units times the earlier period's average price. Price effect = sum over products of later units times the change in that product's price. Mix effect = the remainder.
6. Draw it with `emit_chart type=waterfall`. The chart adds up every bar as a step, so pass the earlier total first, then only the volume, price and mix changes. Never pass the later total as a last bar: it would be stacked on top and the chart would end at the two totals added together. The top of the last step is the later total; say that figure in the summary.

Checks before answering:
- The three effects must add to the total change within $1.
- Use the same product set in both periods. A product launched in between belongs in volume and mix, and should be named.
- A deal event in one period and not the other distorts price. Name it.
- Compare whole periods only. Leave out the running month.

Output:
- Chart plus table: Effect | Dollars | Share of the change.
- A second table for the top five products by contribution to the change.
- Two lines: the main driver and the one to watch.

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
