# What Amazon's new fees will cost you

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What Amazon's new fees will cost you" (id: ops-fee-change-impact, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
When Amazon announces new fees, this works out what the change costs you before it takes effect, product by product. It also shows how the change lowers the most you can afford to pay for ads on each product.

What to read: Each product's current Amazon fees, price, size tier and units, plus the announced new fee rates
What to give me: What an announced Amazon fee change costs each product and the whole account a year, and where it bites hardest

Synthesis tools to use:
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=fee_breakdown month=YYYY-MM`
- `unit_economics_waterfall asp=<price> amazon_fees=<new_fees> cogs=<cost>`
- `breakeven_roas asin=<asin>`

Steps:
1. Ask for the new fee rates by size tier and category, and the start date.
2. Call `amazon_metric metric=contribution_by_asin months=3` for units, price, current fees and product cost.
3. Call `amazon_metric metric=fee_breakdown month=YYYY-MM` for the latest settled month's fee lines.
4. For each product, compute new fees per unit and the change. Yearly cost = change times units a year.
5. Run `unit_economics_waterfall` with the new fees for the top products to show the margin after.
6. Run `breakeven_roas asin=<asin>` with the new fees for products with ad spend.

Checks before answering:
- The fee rates must come from Amazon's announcement as the person supplies it. Do not use remembered rates.
- Size tier per product comes from what Amazon charges today. A product near a tier edge may move tier; flag it.
- Use settled months for current fees.

Output:
- Table: Product | Units a year | Fee per unit now | Fee per unit new | Yearly cost | Margin after | Ad ceiling after.
- Two lines: the total yearly cost and the products to reprice or repack first.

Never:
- Never change prices, packaging or bids.
- Never guess the new fee rates.
- Never count a part-settled month's fees as the current rate.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-fee-change-impact". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
