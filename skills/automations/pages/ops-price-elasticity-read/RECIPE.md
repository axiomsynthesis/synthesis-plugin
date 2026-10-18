# How shoppers react to your price

Channel: Money · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How shoppers react to your price" (id: ops-price-elasticity-read, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures how your own shoppers have reacted to your own price changes, product by product. Every pricing scenario today runs on an assumed reaction; this replaces the assumption with your history, or says honestly that there is not enough history.

What to read: Your past price changes per product and the units sold before and after each one
What to give me: How much unit sales move when each product's price moves, and how sure we are

Synthesis tools to use:
- `cost_rules for=ops-price-elasticity-read`
- `shelf_history marketplace=amazon days=365 asin=<asin>`
- `query_series metric=units grain=week asin=<asin>`
- `amazon_metric metric=promotion_performance months=12 limit=20`
- `run_bayesian`

Steps:
1. Call `shelf_history marketplace=amazon days=365 asin=<asin>` for the product's daily price.
2. Find each lasting price change: a move of 5% or more held for at least 14 days.
3. Call `query_series metric=units grain=week asin=<asin>` for weekly units around each change.
4. Call `amazon_metric metric=promotion_performance months=12 limit=20` to drop windows that overlap a deal or coupon.
5. Once the estimator lands, compare 4 weeks before with 4 weeks after each clean change, adjusted for season, and combine the changes into one estimate with a range. `run_bayesian` can combine clean changes counted as successes and trials if a simple read is wanted.
6. Feed the result to pricing scenarios as the measured elasticity.

Checks before answering:
- Until the estimator exists, say elasticity is not measured and show the raw before-and-after only, labelled unadjusted.
- A window with a stockout, a deal, a big ad change or a rival's price cut is not clean. Drop it and say how many were dropped.
- Fewer than three clean changes is too few. Say so.
- A price change on one pack size moves shoppers to other pack sizes. Read the product family together.

Output:
- Table: Product | Clean price changes | Units change per 10% price change | Range | Confidence.
- One line per product on what the estimate means for the next price decision.

Never:
- Never present a single before-and-after as the elasticity.
- Never change a price to test this.
- Never borrow an elasticity from another product.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-price-elasticity-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Price history (daily shelf snapshots) and weekly units are both held, but nothing joins them into clean before-and-after windows that exclude deals, stockouts and ad changes. Needs an elasticity estimator tool that finds each price change, controls for those events, and returns an estimate with a range. Do the parts you can and say plainly what is missing.
