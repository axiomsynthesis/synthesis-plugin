# When to remind customers to reorder

Channel: Email · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "When to remind customers to reorder" (id: grw-replenishment-timing, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads how long customers usually wait between orders across the whole store. It checks when your reminder flow sends now, and suggests a store-wide reminder day to test. It cannot yet set a day for each product.

What to read: Store-wide days between repeat orders, products bought together, current flow timing
What to give me: A store-wide reminder window from the repeat-order gaps, checked against the current reminder flow. Per-product timing is not ready yet

Synthesis tools to use:
- `shopify_metric metric=time_to_repeat`
- `shopify_metric metric=product_attach limit=20`
- `klaviyo_metric metric=flow_step_performance limit=60`

Steps:
1. Pull `shopify_metric metric=time_to_repeat`. Read the buckets of days between orders and the average.
2. Find the bucket where the running share of repeat orders passes 25% and 50%. The reminder goes near the 25% point, the nudge near the 50% point plus a few days.
3. Pull `shopify_metric metric=product_attach limit=20` to see which products come back together, for the email angle.
4. Pull `klaviyo_metric metric=flow_step_performance limit=60` to check if a reorder flow exists and when it sends.
5. Draft subject and angle for each step.

Checks before answering:
- The gap table is store-wide and all-time, with subscription orders mixed in. It has no per-product median. Never give a per-product reminder day. Say so.
- It counts every gap between orders, not only first to second. Customers who never reordered are not in it. Say the timing leans early.
- Bucket edges are wide. Give the reminder as a range, not one exact day.
- When per-product timing ships, a product with under 50 repeat customers keeps the store-wide timing, labelled as such.
- Suggest a split test of the new day against the current day in the flow.

Output:
- Answer first: the store-wide reminder range, the nudge range, and the current flow day.
- Table: bucket, share of repeat orders, running share.
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
