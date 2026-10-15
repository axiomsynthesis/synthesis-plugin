# Sales hiding behind promo codes and tags

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Sales hiding behind promo codes and tags" (id: grw-code-attribution, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Many creator and podcast sales show up only as a code or a tag on the order. This adds them up so those partners get credit next to paid ads.

What to read: Shopify order tags such as influencer, promo, marketplace and subscription
What to give me: Sales tied to codes and order tags that no ad platform reports

Synthesis tools to use:
- `shopify_metric metric=order_tags months=3 limit=50`

Steps:
1. Pull `shopify_metric metric=order_tags months=3 limit=50`.
2. Group tags by category: influencer, promo, marketplace, subscription.
3. Rank influencer and promo tags by revenue and orders.
4. Ask for the cost of each partner if known and compute revenue per dollar.

Checks before answering:
- Untagged orders are not zero partner sales. Say tagging may be incomplete.
- One order can carry several tags. Never add tag totals into one sum.

Output:
- Answer first. Table: tag, category, orders, revenue, cost if known.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-code-attribution". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
