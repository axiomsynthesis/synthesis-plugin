---
description: "Repeat buying and lifetime value, product by product: Per first product: profit and sales per customer at 30 to 365 days, the repeat ladder, timing, payback, monthly same-product repeat buyers and their heading, and levers to raise it in dollars"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Repeat buying and lifetime value, product by product

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Repeat buying and lifetime value, product by product" (id: customers-repeat-and-ltv-breakdown, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Repeat and lifetime value, one first product at a time: profit and sales at each age, who comes back, how fast, for which product, the monthly same-product repeat count and its heading, then levers in dollars. /payback and /returning stay the website reads.

What to read: Orders by customer and first product, product profit, cost to win a customer, website and subscription cohorts
What to give me: Per first product: profit and sales per customer at 30 to 365 days, the repeat ladder, timing, payback, monthly same-product repeat buyers and their heading, and levers to raise it in dollars

Synthesis tools to use:
- `cost_rules for=customers-repeat-and-ltv-breakdown`
- `recall_decisions`
- `brand_brain action=moves`
- `top_products metric=revenue top_n=10 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `find_product query=<name>`
- `product_ltv_windowed asin=<family> windows=[30,60,90,180,365]`
- `amazon_metric metric=contribution_by_asin months=3`
- `cohort_metrics asin=<family> cohort_start=<YYYY-MM-DD> cohort_end=<YYYY-MM-DD>`
- `gateway_repeat asin=<family> grain=month start=<YYYY-MM-DD>`
- `order_repeat asin=<family> grain=month start=<YYYY-MM-DD>`
- `sequenced_cross_sell age_weeks=13`
- `brand_time_to_repeat`
- `ltv_drivers channel=amazon dimension=multipack_first window_days=365`
- `first_order_contribution_margin`
- `amazon_metric metric=subscription_ladder limit=24`
- `shopify_metric metric=product_ltv`
- `shopify_metric metric=cohort_ltv_censor_safe basis=contribution limit=24`
- `shopify_metric metric=time_to_repeat`
- `recharge_metric metric=survival limit=24`
- `measurable_test direction=higher_is_better`

Steps:
1. Pick products: `top_products` over the last 12 closed months, then `find_product` for each family. Read every pack in a family together. What is already running: `recall_decisions` and `brand_brain action=moves`.
2. Email check: read `orders_no_email_pct` on every month row of `gateway_repeat` and `order_repeat` (step 5). A closed month above 2% is a floor: mark it.
3. Value: `product_ltv_windowed` per family with `asin=family:<id>`. Profit = sales x margin from `amazon_metric metric=contribution_by_asin months=3`. Print each window's `cohort_n`. Blank = unfinished, not low. Buyers here start at their first brand order.
4. Repeat: `cohort_metrics` per family for the newest closed month whose 90 days are complete, and the month 6 earlier (or the launch month, if younger). Buyers here start at their first purchase of the product. Read `product_repeat_by_age`, `brand_repeat_pct`, `avg_orders`. Brand minus product repeat = came back for another.
5. Strict monthly count: `gateway_repeat` and `order_repeat` per family, `grain=month`, 13 months back. Same-product repeat buyers = `all_buyers` minus `new_orders`. Project the month from closed days, with the share of orders still missing an email. Label a month holding a big sale (Prime, Black Friday). Heading: repeat buyers over the last 6 months' first-time buyers, grown at the new-buyer trend.
6. Timing: `brand_time_to_repeat`, `shopify_metric metric=time_to_repeat`. Next product: `sequenced_cross_sell`.
7. Pack size: `product_ltv_windowed` per pack, and `ltv_drivers` with `multipack_first`. It misses packs sized by count of uses: compare those per pack.
8. Payback: cost per new customer = the family's month `advertising` (contribution_by_asin) over that month's `new_orders` (order_repeat), labelled "all ads over all new buyers, a ceiling", as `cac` in `first_order_contribution_margin`. Never `ppc_ntb`: it covers about 1% of ad spend. Website payback is /payback.
9. Website and subscriptions, each on its own rows: `shopify_metric metric=product_ltv`, `metric=cohort_ltv_censor_safe basis=contribution`, `recharge_metric metric=survival`, `amazon_metric metric=subscription_ladder`.
10. Levers: subscribe at first checkout (/subcheck), bigger default pack (/splittest), run-out email (/emailflow), win-back at the reorder gap (/winback), cross-sell the next product (/bundles, /addon), first-order code (/codes). A lever already running is read, not proposed. Size each: buyers reached x repeat lift x profit per repeat order. Close the top one with `measurable_test`.

Checks before answering:
- Lead with profit. With product cost missing, say so and show sales only.
- Amazon, website and subscriptions never add up into one.
- No tool counts past the 2nd order yet: show orders per buyer, and say so.
- Time to repeat is brand-wide and counts every gap, so it reads short.
- Under 100 buyers is too few to rank.

Rounds (relook before you answer):
1. **Same age.** Fails when: two products are compared at different windows, or a window is under 60% filled. Fix: compare at the longest window both fill.
2. **Profit, not sales.** Fails when: the lead product changes between the sales and the profit ranking, or a row has no cost. Fix: rank on profit, blank uncosted rows.
3. **Same product or another?** Fails when: any product's brand repeat is over 1.3x its product repeat. Fix: name where buyers go next.
4. **Second window.** Step 4's older cohort. Fails when: 90-day repeat moves over 3 points. Fix: show both and the heading; a younger product says how many months apart.
5. **Email gap.** Fails when: a closed month's `orders_no_email_pct` is over 2%, or this month's over 10%. Fix: mark it a floor.
6. **Levers sized and testable.** Fails when: a lever's reach or profit per order is not the brand's own number, or it has no test or shortcut. The lift is always assumed (default 1 point): say so. Fix: size it or drop it.

Output:
- First line: the best first product on profit at the longest fair window, and last month's same-product repeat buyers and heading.
- Grid per product: days (30, 60, 90, 180, 365) by profit and sales per customer, buyers counted, unfinished cells marked.
- Repeat line per product: 2nd order at 60, 90, 180 days, same product or another, orders per buyer, payback.
- Monthly count: 13 months and this month's run-rate.
- The 3 findings, each in dollars a month.
- Levers ranked by dollars a month, each with its test and shortcut.

Never:
- Never change an offer, email or ad: the named shortcut does, after a yes.
- Never project from a cohort younger than the window.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-repeat-and-ltv-breakdown". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
