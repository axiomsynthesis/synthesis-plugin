---
description: "What if we lost our biggest one?: How much rides on one channel, account, product or supplier, and how exposed that leaves you"
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
Measures every single point of failure in one view: the channel, the retail account, the product and the supplier the business leans on most. Buyers and lenders ask this first, and founders often know three of the four and miss the fourth.

What to read: Revenue by channel, retail account and product, profit by product, and spend by supplier
What to give me: How much rides on one channel, account, product or supplier, and how exposed that leaves you

Synthesis tools to use:
- `cost_rules for=ops-concentration-risk`
- `netsuite_metric metric=customer_trend months=12 top=12`
- `customer_concentration`
- `top_products metric=revenue top_n=20 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `amazon_metric metric=contribution_by_asin months=6`
- `netsuite_metric metric=vendor_spend limit=20`
- `strategy_framework framework=hhi`
- `strategy_framework framework=power_law_analysis`

Steps:
1. Channels and accounts: call `netsuite_metric metric=customer_trend months=12 top=12` for invoiced revenue per account and `customer_concentration` for the account read.
2. Products: call `top_products metric=revenue top_n=20` with `start_month` and `end_month` spanning the last 12 closed months for revenue share (it covers Amazon products) and `amazon_metric metric=contribution_by_asin months=6` for profit share. That result comes in several pages. Call it again with the next `result_page` until all pages are read, and sum them, leaving out the month flagged `in_flight`, before taking profit shares. Or use the latest closed month only and say so.
3. Suppliers: call `netsuite_metric metric=vendor_spend limit=20` for product spend by supplier. Keep only product makers and packaging. Drop ad platforms, agencies, freight, duties, lenders and tax agencies. It covers one month only, so say the supplier share is a single month.
4. For each dimension, run `strategy_framework framework=hhi shares=[...]` on the shares and `strategy_framework framework=power_law_analysis values=[...] metric_name=<dimension>` on the dollar values.
5. Rank the four by how much revenue or profit a failure of the top item would put at risk.

Checks before answering:
- The modelled channel split from the books can be unreliable; its own flag says when. Use invoiced revenue by account instead and say so.
- Shares passed to the concentration score must all be percents or all fractions, never mixed.
- Profit share needs product costs. Products without cost are excluded and named.
- If the ledger is not connected, show products only and say channel, account and supplier need the books.

Output:
- Table: Dimension | Top item share | Top three share | Concentration band | Revenue or profit at risk.
- Two lines: the dependence that matters most and the cheapest way to reduce it.

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
