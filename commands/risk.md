---
description: "What if we lost our biggest one?: The profit at risk if your top channel, account, product or supplier failed"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What if we lost our biggest one?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What if we lost our biggest one?" (id: ops-concentration-risk, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures every single point of failure in one view: the channel, the retail account, the product and the supplier the business leans on most. For each it says what a failure would cost in profit, not only how big the share is. Buyers and lenders ask this first.

What to read: Revenue by channel, retail account and product, profit by product, and spend by supplier
What to give me: The profit at risk if your top channel, account, product or supplier failed

Synthesis tools to use:
- `cost_rules for=ops-concentration-risk`
- `netsuite_metric metric=customer_trend months=12 top=12`
- `customer_concentration`
- `top_products metric=revenue top_n=20 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM`
- `monthly_pnl month=YYYY-MM`
- `netsuite_metric metric=vendor_spend limit=20`
- `strategy_framework framework=hhi`
- `strategy_framework framework=power_law_analysis`
- `amazon_metric metric=inventory_position`

Steps:
1. Channels and accounts: call `netsuite_metric metric=customer_trend months=12 top=12` for invoiced revenue per account and `customer_concentration` for the account read.
2. Products: call `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM` for each of the last 3 settled months. If the result names a next `result_page`, call again with it until all are read. Take profit after ads by product and from `by_family`. Use `top_products metric=revenue top_n=20` over the last 12 closed months for revenue share.
3. Suppliers: call `netsuite_metric metric=vendor_spend limit=20`. Keep only product makers and packaging. Drop every ad platform, agency, marketplace, freight or shipping firm, customs broker, lender, payment firm and tax or government agency. List the vendors you dropped.
4. Size profit at risk for each:
   - Product: 30 days without the top product or family, at its monthly profit after ads.
   - Account: 30 days without the top retail account, at its revenue times the company gross margin rate from `monthly_pnl`.
   - Amazon: a 10% rise in Amazon fees, and a 14-day account suspension, both from Amazon's monthly profit in `totals.page_profit`.
   - Supplier: the monthly profit of the products that supplier makes, when the person can say which.
5. Run `strategy_framework framework=hhi shares=[...]` and `strategy_framework framework=power_law_analysis values=[...] metric_name=<dimension>` on each set of shares, as a footnote only.
6. Rank the four by profit at risk.

Checks before answering:
- The modelled channel split from the books can be unreliable. Its own flag says when. Use invoiced revenue by account instead and say so.
- Shares passed to the concentration score must all be percents or all fractions, never mixed.
- Profit share needs product costs. Products without cost are left out and named.
- Account profit at risk uses the company margin, not that account's own margin, which is not available yet. Say so.
- The supplier list covers one month and carries no account or vendor type, so the filter is by name. There is no product-to-supplier map yet, so supplier risk is not sized in dollars unless the person names what each maker supplies. Say so.
- Amazon is a marketplace, not one buyer. Its risk is fees, suspension and policy, not a concentration score.
- If the ledger is not connected, show products only and say channel, account and supplier need the books.

Rounds (relook before you answer):
1. **Ranked by profit, not share.** Fails when: the table is ordered by share instead of profit at risk. Fix: re-rank.
2. **Stock is the nearest failure.** Call `amazon_metric` with `metric=inventory_position`. Fails when: the top product has under 60 days of cover and the answer does not lead with it. Fix: lead with it and the date it runs out.
3. **Moving or steady.** Re-read product shares over the last 3 months against the 12. Fails when: the top product changes or its share moved more than 10 points. Fix: say the dependence is shifting and which way.
4. **Supplier sized honestly.** Fails when: supplier risk is given in dollars before the person said what that maker supplies. Fix: show share only and ask.
5. **The fix pays.** Fails when: the cheapest way to reduce the top risk has no cost named or loses money. Fix: price it, or say it is a trade-off.

Output:
- One line first: the dependence that would cost the most, in profit dollars, and the cheapest way to reduce it.
- Table: Dimension | Top item | Share | Profit at risk | How it was sized.
- Concentration scores as a footnote.

Never:
- Never treat the brand's own storefronts as outside accounts.
- Never present modelled channel shares as measured.
- Never act on the finding.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-concentration-risk". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
