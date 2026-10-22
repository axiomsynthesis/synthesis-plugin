---
description: "Run my Amazon ads each morning: One numbered morning list (block, harvest, capped budgets, low stock), approved blocks made and read back, every move logged"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Run my Amazon ads each morning

Channel: Amazon · Level: Does it for you · Status: Ready now
Schedule: Every morning

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run my Amazon ads each morning" (id: do-amazon-morning-operator, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each morning it judges yesterday's Amazon ad moves, builds today's list by the brand's ad rules, and makes the blocks you approve.
It remembers each move in the decision log, so the next morning says which worked.

What to read: Logged moves and how each did since, 30 days of ad searches against each product's break-even, capped campaigns, stock cover
What to give me: One numbered morning list (block, harvest, capped budgets, low stock), approved blocks made and read back, every move logged

Synthesis tools to use:
- `cost_rules for=do-amazon-morning-operator`
- `recall_decisions`
- `amazon_metric metric=ppc_search_terms min_clicks=10 limit=50`
- `breakeven_roas months=1`
- `amazon_metric metric=ppc_budget_utilisation`
- `amazon_metric metric=stockout_forecast`
- `amazon_metric metric=ppc_account_changes days=3`
- `log_decision kind=campaign`

Steps:
1. Call `recall_decisions`. Find this brand's Amazon moves from the last 14 days and any line starting "STANDING YES". Call `amazon_metric` with `metric=daily_actions limit=60`: use its recent_moves block too.
2. Judge each move: a blocked search spends nothing since, a harvested one keeps selling. Say worked, did not, or too soon.
3. Build today's list from daily_actions when it ran. Else call `amazon_metric` with `metric=ppc_search_terms`, `start_date` 33 days ago, `end_date` 3 days ago, `min_clicks=10` and `limit=50`, every page. Call `breakeven_roas` with each main product's `asin` and `months=1`.
4. The rules, the same for every brand, overridable per brand: block a search with no order after 2 divided by its product's conversion rate in clicks (at least 10, 25 if unknown), or after spending 2x the product's break-even cost per order. Harvest a search with 2 or more orders at or under break-even ad cost that is not yet a keyword. Skip your own brand name and anything changed in 3 days.
5. Call `amazon_metric` with `metric=ppc_budget_utilisation` for campaigns out of budget. A capped one earns a 20% raise only with 5 or more orders at 0.75x break-even ad cost or less, never above the ceiling. Call `amazon_metric` with `metric=stockout_forecast` and flag ads on products about to run out.
6. Show ONE numbered list: blocks with spend a month, harvests, capped raises with old and new budget and 30-day dollars, ads on products running out. End with "Reply yes, or yes except 2".
7. Blocks on yes: if `ad_change` is in your tools and offers Amazon blocks, call it with `action=propose` for Amazon, naming the searches. Show the plan, then call `ad_change_apply`.
8. Otherwise follow "Block Amazon searches that cost money and never sell" in the console, or its bulk file.
9. Harvests and budget raises are a change list the person makes.
10. Call `log_decision` per move with `kind=campaign`, the search or campaign, the dollars, `made_on` today and the measure.
11. Call `amazon_metric` with `metric=ppc_account_changes` and `days=3` to see changes made since yesterday.
12. Standing yes: if the person says "always block inside my rules", log it with `log_decision` as "STANDING YES: blocks inside the ad rules". Then blocks apply without asking. "Stop the standing yes" withdraws it.

Checks before answering:
- Anything that raises spend is shown with dollars and waits for a yes, every time.
- The standing yes covers blocks only. On a scheduled run without it, apply nothing.
- Sales land up to 30 days after a click. Never judge the last 3 days.
- A read error is a failure, not zero orders. Never block from missing data.

Rounds (relook before you answer):
1. **Did yesterday's moves hold?** Re-read step 2 against `ppc_account_changes`. Fails when: a search blocked 3 or more days ago still shows spend in that ad group. Fix: mark the block failed, find why, and never count its savings.
2. **Late orders.** Re-read each block on the 30 days ending 3 days ago. Fails when: a block row has an order that landed since the first read. Fix: drop it from blocks and offer it as a harvest if it meets that rule.
3. **Sale days.** Fails when: the window holds a big sale event, such as Prime Day or Black Friday, and a rule fired on those days alone. Fix: drop that row and judge it again a week after the event.
4. **Profit before a raise.** For each capped raise, compare the last 7 days' profit per order on that product after ads. Fails when: profit per order is $0 or less, or the product has under 30 days of stock. Fix: drop the raise and say why.
5. **Total spend.** Add up every raise. Fails when: today's list lifts total daily ad spend more than 20% (default, change it to your own). Fix: keep the raises with the most orders per dollar and hold the rest.

Output:
- One line first: yesterday's moves and what they did, then today's dollars at stake.
- The numbered list.
- After applying: one row per block, campaign, ad group, done or skipped.
- What this run did not see: each product's own margin, repeat buyers.

Never:
- Never block your own brand, a product name, or a search that sold.
- Never change a bid, budget or placement from this list without a yes to the dollars.
- Never apply a move the person excluded with "except".

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-amazon-morning-operator". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every morning). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due. On a repeat run nobody is there to say yes: change only what I gave a standing yes to, which can only lower spend, and send everything else as the list.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
