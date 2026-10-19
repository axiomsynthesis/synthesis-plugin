---
description: "Walmart profit after every fee: Walmart profit line by line, what Walmart takes per $100, and what is unpaid"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Walmart profit after every fee

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Walmart profit after every fee" (id: money-walmart-profit-every-fee, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what Walmart Marketplace really left you for one month: sales, then Walmart's commission, fulfilment and label charges, warehouse and service fees, refunds and product cost, the same way the Profit page counts them. It checks the sales against what Walmart itself recorded and says what is still unpaid.

What to read: Walmart Marketplace sales, Walmart commission, fulfilment and label charges, warehouse and service fees, refunds, product cost, and what Walmart paid out
What to give me: Walmart profit line by line, what Walmart takes per $100, and what is unpaid

Synthesis tools to use:
- `cost_rules for=money-walmart-profit-every-fee`
- `walmart_metric metric=profit month=YYYY-MM`
- `walmart_metric metric=payouts periods=6`
- `walmart_metric metric=orders_trend months=12`
- `operator_inputs section=cogs`

Steps:
1. Call `walmart_metric` with `metric=profit` and `month=` set to last month.
2. If the result has `no_headline_reason`, there is no profit to state. Say why and list `uncosted_products`. Still show the lines that are real.
3. If the month has no orders, call `walmart_metric` with `metric=orders_trend` and `months=12`. Find the last month with orders and say the channel has sold nothing since then. Stop there.
4. Read every entry in `column.lines` and `column.tie_out`. Sort the lines into counted, estimated (orders not paid out yet) and not connected.
5. Call `walmart_metric` with `metric=payouts` and `periods=6` for what Walmart paid out and its fee rates per payout.
6. Call `operator_inputs` with `section=cogs` to check costs are entered for the products Walmart sells.

Checks before answering:
- Read `data_quality_flags` first. If `gated` is true, there is no number: give the reason.
- If `tie_out` shows our sales do not match Walmart's own record, say so before any profit.
- A payout period is not the same orders as a sales month. Use the profit column for profit and the payouts only for rates and what is unpaid.
- A small month swings on a handful of orders. Say how many orders the month holds.
- A connected account with no orders is a stopped channel, not an unconnected one. Never call it unconnected. Say the date it last sold.
- Check the date of the newest payout. If it is more than a month old while orders still come in, say the payouts may be stale and the fee rates may be out of date.
- Walmart Connect ad spend is not read yet. If the brand runs Walmart ads, profit here reads too high. Say so in plain words.

Output:
- One line first: Walmart profit for the month, its share of sales, settled or partly estimated. If the channel has stopped selling, that line is the date it last sold and nothing else.
- A table: line, dollars, share of sales, counted / estimated / not connected.
- Two lines: what Walmart takes per $100 of sales, and the amount not yet paid.
- One move: the one fee or cost to work on first.

Never:
- Never call order sales the payout.
- Never guess a product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-walmart-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
