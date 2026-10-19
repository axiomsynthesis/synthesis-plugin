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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-concentration-risk". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
