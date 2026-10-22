---
description: "Size an Amazon price or Subscribe and Save change: What a new price or Subscribe and Save discount does to profit per unit, a check against your Walmart floor, and a logged decision with a read date"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Size an Amazon price or Subscribe and Save change

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Size an Amazon price or Subscribe and Save change" (id: do-amazon-price-move, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sizes an Amazon price or Subscribe and Save change before your team makes it. It shows profit per unit before and after, checks your Walmart floor and the fee line, and logs the move with a read date.

What to read: The product's Amazon price, fees, profit per unit, Subscribe and Save signups, your Walmart price, booked deals
What to give me: What a new price or Subscribe and Save discount does to profit per unit, a check against your Walmart floor, and a logged decision with a read date

Synthesis tools to use:
- `cost_rules for=do-amazon-price-move`
- `amazon_metric metric=listing_details`
- `amazon_metric metric=contribution_by_asin months=1`
- `breakeven_roas months=1`
- `amazon_metric metric=sns_program weeks=12`
- `walmart_metric metric=top_skus limit=50`
- `record_amazon_deal action=list`
- `log_decision kind=price`
- `run_scenario scenario_type=price_change`

Steps:
1. Ask the product, the new price, the new Subscribe and Save discount and the date it goes live.
2. Call `amazon_metric` with `metric=listing_details` and the product's `asin` for today's price. If Amazon refuses it, say so and use the price from step 4.
3. Call `amazon_metric` with `metric=contribution_by_asin`, the `asin` and `months=1` for profit per unit today. This is the Profit page's own row.
4. Call `breakeven_roas` with the `asin` and `months=1` for today. Again with `price` set to the new price, and at the Subscribe and Save price. The 3-month default can time out.
5. Amazon charges a lower sales fee at or under $10 in some categories. If the new price is over $10 and today's fee is under 10% of price, run `breakeven_roas` again with `referral_fee_pct=0.15`. Show both.
6. Ask the floor. Call `walmart_metric` with `metric=top_skus` and `limit=50` if you sell on Walmart. Default your lowest Walmart price for this same product. If it is not on Walmart Marketplace, ask the store price. Never use another product's price. The price after Subscribe and Save must stay at or above the floor. If it would not, say the list price must rise first.
7. Call `amazon_metric` with `metric=sns_program` and `weeks=12`. It covers the whole brand, not this product. Say so. Count Subscribe and Save from this report, not from order flags.
8. Call `record_amazon_deal` with `action=list`. It only reads. A booked deal in the read weeks will cloud the result. Say so.
9. Pick a read date at least 6 weeks out that avoids Black Friday to Cyber Monday and Prime events. Show the plan and wait for yes. Then call `log_decision` with `kind=price`, the decision, `measure` (units a week or profit a week for that product), `made_on` (the go-live date), `expected` and `window_weeks` set to reach that date.
10. The day after it goes live, call `amazon_metric` with `metric=listing_details` and the same `asin`. The price must match the logged one. If Amazon refuses it, ask the person to read the live price and say the check was by eye.

Checks before answering:
- Safe test: when the person asks for a test run, size the move and show the decision text without logging it. No account is touched.
- Spend: this changes no ad budget. Say that other ad tests on this product should pause while the price reads, or the read is mixed.
- Read the result at 6 weeks or more, against a normal month. Never against the weeks right after a big sale event.
- A price just under $10 sits on the fee line. Say a later move over $10 can raise the sales fee.
- If profit per unit or fees came back empty, say they could not be read. Never call the move safe.

Rounds (relook before you answer):
1. **Units you can lose.** Call `run_scenario` with `scenario_type=price_change`, `price_change_pct`, `unit_cogs`, `fee_pct` and `unit_fees` from steps 3 to 5. Fails when: the units you can lose before the move stops paying is under 10%. Fix: say a small drop in buyers wipes out the gain, and suggest a smaller step.
2. **Say why in one line.** Fails when: the draft cannot say in one plain sentence what the move earns a week at today's units. Fix: rewrite the first line as dollars a week, before and after.
3. **Every floor.** Re-read step 6. Fails when: the price after Subscribe and Save, or after any coupon or deal stacked on it, is under the lowest price this product holds on any channel. Fix: raise the list price first or drop the discount.
4. **Clean read window.** Re-read step 8. Fails when: a booked deal, a big sale event, or a price move on another size of the same product falls inside the read weeks. Fix: move the go-live or the read date.
5. **Six weeks later.** On the read date, call `amazon_metric` with `metric=contribution_by_asin`, the `asin` and `months=1`. Fails when: units a week fell more than the round 1 line. Fix: say the move lost money and give the step back to the old price.

Output:
- One line first: profit per unit before and after, and whether the floor holds.
- A table: price, Subscribe and Save price, fee, profit per unit, Walmart floor, pass or fail.
- The logged decision and its read date.
- The steps for your team in Seller Central. Synthesis does not change the price.

Never:
- Never change a price in Seller Central. Your team does it.
- Never propose a price under the Walmart floor.
- Never guess a cost or fee the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-amazon-price-move". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
