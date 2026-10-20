---
description: "Warn me before we run out: A morning heads-up only when a product must be restocked now, with the restock-by date and the sales at risk"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Warn me before we run out

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: every morning at 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Warn me before we run out" (id: inventory-stockout-early-warning, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every morning, checks which products are about to run out and when, counting upcoming Amazon sales, booked deals and stock already on its way. It only speaks up when something is at risk.

What to read: FBA stock, stock on its way, upcoming Amazon sales and booked deals, sales speed
What to give me: A morning heads-up only when a product must be restocked now, with the restock-by date and the sales at risk

Synthesis tools to use:
- `amazon_metric metric=stockout_forecast`
- `amazon_metric metric=velocity_momentum`
- `amazon_metric metric=closed_shipments limit=10`
- `netsuite_metric metric=inventory_position limit=200`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=stockout_forecast` and `limit=50` for each product's run-out dates and any gap before stock on its way lands. Read every page: call again with the next `result_page` the result names. Products come soonest first. Keep reading until the dates pass today plus the longest restock time.
2. Call `amazon_metric` with `metric=velocity_momentum` and `weeks=8` to catch products selling faster than usual, and products winding down: last two weeks under a fifth of the first two, while in stock.
3. Call `amazon_metric metric=closed_shipments limit=10`. The transfer time is `arrival_times` US `received_90pct_p90`. Call `netsuite_metric metric=inventory_position limit=200` for `lead_time_days`, the production lead time. It lists your own product codes, so match each to the Amazon product by name.
4. Keep a product when `late_runs_out` is before today plus its restock time plus 7 days, or falls inside a known sale window in `events`. Restock time is the transfer time, or the lead time when your own warehouse has none. Neither known: ask. Skip winding-down products. List them once a week, on Monday, not daily.
5. Size each alert as units lost times `price_recent`. Units lost is `gap_lost_units`, or for a product that runs out for good, `normal_pace_per_day` times the days until a restock could land. Drop alerts under $200.
6. Name each product from the result's `asin_names`. Call `find_product` only for a code missing from `asin_names`.

Checks before answering:
- If the stock read fails, send "stock could not be read today", not silence. Silence means all clear.
- Plan against `late_runs_out`: stock landing late and the next sale as big as the biggest recent one.
- A gap is different from running out for good: a gap ends when stock already on its way lands (a faster transfer or a slower ad pace saves those sales); running out for good needs a new order.
- If a product is selling well above its `normal_pace_per_day` in the last two weeks, say its date may come sooner.
- If the forecast says no booked deals are entered, say a booked Lightning Deal or Deal of the Day is not in the dates.
- Judge each product on its own. Never average across products.
- Alerts are sized in sales, not profit. Say so. Profit per unit is not in this check yet.
- No restock time known or given: never assume one. Give the run-out date and say the restock-by date needs the lead time.
- There is no discontinued flag to read yet. A product only out of stock is not winding down.

Output:
- Nothing when all is well.
- When at risk, a short alert led by the decision: restock-by date (run-out minus restock time minus 7 days), product, run-out date, sales at risk in dollars, gap or runs out for good, one move.
- Monday only: one line naming products winding down.

Never:
- Never place an order or create a shipment. A person does that.
- Never give a run-out date that is not from the forecast.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Inputs only I know: supplier lead time in days; units at your own warehouse or 3PL. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Nothing saves the lead time or own warehouse stock yet: say it was used for this run only. On a scheduled run, name what is missing instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-stockout-early-warning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every morning at 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
