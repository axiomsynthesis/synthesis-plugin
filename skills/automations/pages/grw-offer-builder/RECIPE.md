# Build an offer that sells

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build an offer that sells" (id: grw-offer-builder, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
An offer is more than a discount. It is the bundle, the bonus, the guarantee, the reason to act now and the price. This designs three offers from what your customers already buy together and checks the margin each one leaves.

What to read: Order values, products bought together, subscription value and margin
What to give me: Three offer designs with the margin left after each, ready to test

Synthesis tools to use:
- `shopify_metric metric=market_basket limit=20`
- `shopify_metric metric=aov_levers months=12`
- `subscription_economics`
- `shopify_metric metric=top_products limit=20`

Steps:
1. Pull `shopify_metric metric=market_basket limit=20` and `shopify_metric metric=top_products limit=20`.
2. Pull `shopify_metric metric=aov_levers months=12`.
3. Ask for unit cost and shipping cost per product.
4. Design three offers: a bundle at a set price, a gift-with-purchase above a basket line, and a subscribe offer using `subscription_economics`.
5. For each, compute margin per order and the extra orders needed to beat today's margin.

Checks before answering:
- Never design an offer without unit costs. Ask for them.
- A bonus product's cost counts in full.

Output:
- Table: offer, what is in it, price, margin per order, break-even lift. One line on which to test first.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-offer-builder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
