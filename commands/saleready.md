---
description: "Get ready for the next big Amazon sale: A go or fix checklist three weeks before a big sale event, one line per product, with what to fix by when"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Get ready for the next big Amazon sale

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Get ready for the next big Amazon sale" (id: mkt-amazon-prime-event-readiness, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Most big sale event losses are set three weeks before: no stock, no buy box, a capped budget, or a deal price that is not low enough. This checks each product against each and gives a fix list with dates.

What to read: Stock cover, buy box, ratings, ad budget caps, deal prices against recent prices, and last year's event lift
What to give me: A go or fix checklist three weeks before a big sale event, one line per product, with what to fix by when

Synthesis tools to use:
- `amazon_metric metric=stockout_forecast limit=200`
- `amazon_metric metric=buybox_health days=30 limit=40`
- `amazon_metric metric=rating_watch days=60 limit=30`
- `amazon_metric metric=ppc_budget_utilisation days=30 limit=50`
- `amazon_metric metric=velocity_momentum weeks=52 asin=<asin>`
- `shelf_history marketplace=amazon days=30`

Steps:
1. Ask the person for the event date and the products in the event.
2. Call `amazon_metric metric=stockout_forecast limit=200` and read each product's `events` for this sale (`x_normal`, `extra_units`, `extra_units_high`) and `late_runs_out`. Use `amazon_metric metric=velocity_momentum weeks=52 asin=<asin>` only for a product with no event history.
3. Use the `late_runs_out` date from step 2, not days of cover, because days of cover does not include the event lift. Will each product cover the event at last year's lift plus two weeks after?
4. Call `amazon_metric metric=buybox_health days=30 limit=40` and `amazon_metric metric=rating_watch days=60 limit=30`. Flag products below 90% buy box or with a rating step down.
5. Call `amazon_metric metric=ppc_budget_utilisation days=30 limit=50`. Campaigns that cap out now will cap out by morning on event day.
6. Call `shelf_history marketplace=amazon days=30` for your own recent prices. A deal must beat the recent low Amazon checks against. Remind the person to confirm the exact rule in Seller Central. This history is weekly and misses deal days, so take the recent low from Seller Central.

Checks before answering:
- Stock is Amazon's live count. Quote Amazon's update time. Count inbound units only if they will be checked in before the event; stock moving between Amazon warehouses usually returns within days.
- A product with no event last year has no lift to borrow. Use the family's lift and say so.
- Never state Amazon's deal eligibility rules as fact. They change. Point to Seller Central.

Output:
- One line: how many products are ready.
- A table: product, stock ready, buy box, rating, budget, deal price check, fix and by when.

Never:
- Never create deals, shipments or budget changes.
- Never promise an event result.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-prime-event-readiness". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
