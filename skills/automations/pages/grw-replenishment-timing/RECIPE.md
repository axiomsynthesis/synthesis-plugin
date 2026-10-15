# When to remind customers to reorder

Channel: Email · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "When to remind customers to reorder" (id: grw-replenishment-timing, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds how many days customers usually wait before buying a product again. It sets the reorder reminder a few days before that point and drafts the flow, so you do not nag too early or arrive after they bought elsewhere.

What to read: Days between first and second order, by product
What to give me: The right reminder day for each product, and a reminder flow outline

Synthesis tools to use:
- `shopify_metric metric=time_to_repeat`
- `shopify_metric metric=product_attach limit=20`
- `klaviyo_metric metric=flow_step_performance limit=60`

Steps:
1. Pull `shopify_metric metric=time_to_repeat` and read the median and spread of days to second order.
2. Pull `shopify_metric metric=product_attach limit=20` to see which products come back together.
3. Pull `klaviyo_metric metric=flow_step_performance limit=60` to check if a post-purchase or reorder flow exists and when it sends.
4. Set the reminder at about 85% of the median gap per product, with a second nudge at the median plus 10 days.
5. Draft subject and angle for each step.

Checks before answering:
- Use only customers with a second order. Say how many that is.
- A product with under 50 repeat customers gets the brand-wide timing, labelled as such.

Output:
- Table: product, median days to reorder, reminder day, second nudge day, current flow day.
- Two to three email drafts in plain text.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- A person builds the flow in Klaviyo.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-replenishment-timing". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
