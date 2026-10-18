# Next month's storage bill, before it hits

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Next month's storage bill, before it hits" (id: money-storage-fee-forecast, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Estimates next month's Amazon storage bill per product before Amazon posts it, including the jump from October to December. It names the products driving the bill and the ones that could avoid the most fee by selling through or being removed.

What to read: FBA stock, stock on its way, the sales forecast, posted storage fees, stock age
What to give me: Next month's Amazon storage bill, the products driving it, and the fee each could avoid

Synthesis tools to use:
- `cost_rules for=money-storage-fee-forecast`
- `amazon_metric metric=storage_fee_forecast limit=20`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=storage_fee_forecast` and `limit=20`.
2. Open with `headline`: next month's bill in dollars, the change from this month, the bill if stock is kept at today's level, and the last posted bill.
3. Read `rates` and say whether each month's rate is measured from posted bills or is Amazon's published rate.
4. Read `backtest` and `model_beats_naive`, and quote the error against "same as last month".
5. Name the products in `products` and `avoid_most` with `find_product`.

Checks before answering:
- If `could_not_forecast` is set, say why. Never call it a $0 bill.
- If `model_beats_naive` is not true, say the forecast was not more accurate than "same as last month" in past months. It reads low for a brand that keeps sending stock in.
- October to December costs about three times the rest of the year. Say when the rate is published, not measured.
- Name any product in `not_forecast`. It has stock but no posted size, so it is not in the total.
- The aged-stock surcharge is a rough estimate from wide age buckets. Say so.

Output:
- One line first: next month's storage bill in dollars and the change from this month.
- A table: product, units at Amazon now, average units next month, next month's fee, share of the bill, fee it could avoid.
- One line on the backtest error and whether each rate is measured or published.

Never:
- Never create a removal order or change a shipment. A person does that.
- Never guess a product's size or weight.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-storage-fee-forecast". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
