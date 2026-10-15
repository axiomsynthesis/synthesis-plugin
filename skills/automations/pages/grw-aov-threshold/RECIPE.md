# Set the free shipping line to grow basket size

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Set the free shipping line to grow basket size" (id: grw-aov-threshold, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how order values cluster and what drives them. It suggests a free shipping line just above the most common order size and the add-on that gets people there.

What to read: Order value spread and its parts: units per order, price per unit, products per order
What to give me: Where to set free shipping, and which lever lifts order value

Synthesis tools to use:
- `shopify_metric metric=aov_distribution`
- `shopify_metric metric=aov_levers months=12`
- `shopify_metric metric=product_attach limit=20`

Steps:
1. Pull `shopify_metric metric=aov_distribution`.
2. Pull `shopify_metric metric=aov_levers months=12`.
3. Pull `shopify_metric metric=product_attach limit=20` for natural add-ons.
4. Find the order-value band with the most orders. Suggest a line 15 to 25% above it and the add-on that fills the gap.

Checks before answering:
- Subscription renewals sit at fixed values. Exclude them or show them apart.
- Ask for the current free shipping line and shipping cost before advising.

Output:
- Answer first. A short band table and the suggested line, with the expected order value change.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-aov-threshold". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
