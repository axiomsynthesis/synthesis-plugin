---
description: "What happens if you change the price?: How much volume a price change can lose and still pay, and the odds once buyer reaction is known"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What happens if you change the price?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What happens if you change the price?" (id: money-price-change-simulator, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs thousands of what-ifs on a price change before you make it. It gives the likely range of profit change and the odds that profit goes up.

What to read: Sales history, price changes, conversion
What to give me: How much volume a price change can lose and still pay, and the odds once buyer reaction is known

Synthesis tools to use:
- `cost_rules for=money-price-change-simulator`
- `amazon_metric metric=contribution_by_asin months=3`
- `brand_brain action=moves kind=price_change page=<page-id>`
- `query_series metric=units grain=week asin=<asin>`
- `operator_inputs`
- `run_scenario scenario_type=price_change`
- `find_product`
- `amazon_metric metric=ppc_profit_by_asin`
- `amazon_metric metric=shelf_position`

Steps:
1. Use `find_product` to pin the exact product the person means.
2. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3`. From the last fully settled month take that product's price per unit, units, Amazon fees per unit and product cost per unit. Split the fees into the share of price Amazon keeps and the fixed fees per unit. The referral share is `referral_fee` over `settled_principal`. The fixed fee is `fba_fee` over units.
3. If the product cost is missing there, call `operator_inputs` with `section=cogs`.
4. Do not estimate how buyers react to price (the elasticity) by hand from one move. The weeks around a single move also carry ads, deals and season, so the number comes out wrong. List past price changes on this product with `brand_brain` with `action=moves`, `kind=price_change` and the product's page, and show units around them with `query_series` with `metric=units`, `grain=week` and the `asin`, as context only. Pass an elasticity only when the person gives one that was measured, and say where it came from. Otherwise give the break-even and propose a 4-week price test on one pack size.
5. Call `run_scenario` with `scenario_type=price_change`, the `price_change_pct`, `unit_price`, `unit_cogs`, `fee_pct` (the referral share), `unit_fees` (fixed fees per unit), `units_per_month` and `months=6`. Always pass `unit_price` and `units_per_month` from the last settled month. If they are left out, the tool works them out from a longer window and they will not match that month. Pass `elasticity` and an `elasticity_sigma` at least half its size only for a measured elasticity from step 4.

Checks before answering:
- If product cost is missing, stop and say so. A price test without cost is not a profit test.
- Always pass the fees. Without them the tool's margin is price minus product cost only, which on Amazon overstates it by a third or more.
- There is no tool yet that measures elasticity from past price moves. So the answer cannot give odds unless the person supplies a measured one. Say so.
- The break-even is on profit before ads. A higher price can lower conversion and raise ad cost per unit, which this does not include. Say so.
- With no measured elasticity the tool returns the break-even (how much volume the change can lose and still pay) and a table of what-ifs, not odds. Give those, say plainly that the odds need a short price test, and never invent an elasticity.
- Never state a single profit number. Give the break-even, and the range and odds when an elasticity exists.

Rounds (relook before you answer):
1. **Cost and fees passed.** Fails when: `unit_cogs`, `fee_pct` or `unit_fees` was left out, or came from a different month than the price. Fix: re-run with all of them from the last settled month.
2. **Argue the losing case.** Fails when: the volume the change can lose is smaller than the biggest unit drop seen around a past price move on this product. Fix: call it risky and lead with a 4-week test.
3. **Profit after ads.** Call `amazon_metric` with `metric=ppc_profit_by_asin`. Fails when: the product loses money after ads today, or ad cost is over 10% of its sales and the answer gives only the before-ads break-even. Fix: show profit after ads per unit before and after the change.
4. **Shelf check.** Call `amazon_metric` with `metric=shelf_position`. Fails when: the new price moves the product from below the nearest rival on its main search to above it, or no rivals are set up and the answer calls the price safe. Fix: say so beside the break-even.
5. **Other channels.** Fails when: the product sells on the website or another store and the new Amazon price would sit below the website price. Fix: ask whether the website price moves too.
6. **A test that can be read.** Fails when: the proposed test is under 4 weeks, runs into a sale event, or changes more than one pack. Fix: one pack, 4 weeks, outside sale events.

Output:
- One line first: how much volume the change can lose and still pay, then the odds and likely range a month if an elasticity exists.
- A table: price, units a month, profit a month, for low, likely and high cases.
- One move, and how we will know it worked: units and profit after four weeks.

Never:
- Never change a price in any account. A person does that.
- Never recommend a change that lowers profit after ads, even if it adds units.
- Never invent a past price change, an elasticity or a cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-price-change-simulator". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
