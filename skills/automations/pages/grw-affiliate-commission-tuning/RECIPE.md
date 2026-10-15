# Set the right commission per product

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Set the right commission per product" (id: grw-affiliate-commission-tuning, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads what you pay affiliates per product against the sales and conversion each product gets. It suggests where to raise a rate to win more creators and where you are paying for sales that would happen anyway.

What to read: Affiliate commission paid, sales and conversion by product
What to give me: Products where the commission is too rich or too thin, and the rate to try

Synthesis tools to use:
- `levanta_metric metric=commission_economics months=6`
- `levanta_metric metric=product_performance months=6 limit=30`
- `levanta_metric metric=conversion_detail months=3 limit=30`
- `amazon_metric metric=contribution_by_asin months=6`

Steps:
1. Pull `levanta_metric metric=commission_economics months=6`.
2. Pull `levanta_metric metric=product_performance months=6 limit=30`.
3. Pull `levanta_metric metric=conversion_detail months=3 limit=30`.
4. Call `amazon_metric metric=contribution_by_asin months=6` for each product's profit after Amazon fees and product cost. A product with no entered cost has no margin. Leave its rate alone and say so.
5. For each product, compute effective commission as paid over attributed sales and creators actively promoting it.
6. Flag high-margin products with few creators (raise) and products with commission above the target share of price with flat sales (trim).

Checks before answering:
- Creator sales are the platform's own attribution. They will not tie to your order records, and they are a slice of the shop, not all of it.
- Recent days keep changing as attribution settles. Drop the platform's lag days before reading the latest month.
- A blank or zero cost field means the cost is not stored there, never that nothing was paid.
- Use the margin from step 4. Never set a rate for a product without one.

Output:
- Answer first. Table: product, attributed sales, commission paid, effective rate, active creators, suggested rate, reason.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Rates change only when a person edits them on the platform.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-affiliate-commission-tuning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
