# How fast each product pays back its new customers

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How fast each product pays back its new customers" (id: ops-cac-payback-by-product, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows, per gateway product, whether winning a new customer pays back and how long it takes. A first order that loses money is normal for a product people rebuy. This says whether the rebuying actually covers it, and when.

What to read: First-order profit, cost to acquire a new customer and repeat value over time, per gateway product
What to give me: For each product that brings in new customers, the months until the cost to win them is earned back

Synthesis tools to use:
- `amazon_metric metric=ppc_ntb`
- `first_order_contribution_margin asin=<asin> cac=<cost>`
- `product_ltv_windowed asin=<asin> windows=[60,90,180]`
- `amazon_metric metric=pnl_by_customer_type`

Steps:
1. Call `amazon_metric metric=ppc_ntb` for cost per new-to-brand order by product.
2. For each gateway product, run `first_order_contribution_margin asin=<asin> cac=<cost>` for profit on order one after acquisition cost.
3. Run `product_ltv_windowed asin=<asin> windows=[60,90,180]` for value earned by those customers over time.
4. Convert later revenue to profit with the same product margin.
5. Payback month = the first window where cumulative profit covers the acquisition cost.
6. Call `amazon_metric metric=pnl_by_customer_type` to show the new versus repeat split overall.

Checks before answering:
- A young cohort has not had time to rebuy. Only use windows the cohort has fully lived through, and say how many customers are in it.
- Ad cost per new-to-brand order covers ad-driven buyers only. Say so.
- A product with no entered cost cannot be assessed.
- Ad-attributed sales are still moving for about two weeks after a period closes. Leave the last two weeks out.

Output:
- Table: Product | Cost to acquire | First-order profit | Profit by day 60 / 90 / 180 | Payback month | Customers in cohort.
- Two lines: the product that pays back fastest, and the one that does not pay back.

Never:
- Never treat repeat rate as lifetime value.
- Never extend a cohort beyond what it has lived.
- Never change bids or budgets.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-cac-payback-by-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
