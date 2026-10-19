# Build customer groups for email and ads

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build customer groups for email and ads" (id: grw-rfm-audiences, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sorts customers into groups like champions, loyal, at risk and lost by how recently, how often and how much they buy. Each group gets a size, its value and the message to send it.

What to read: Website customers grouped by recency, frequency and spend
What to give me: Customer groups with size, value and the message for each, with groups made mostly of long-gone customers flagged

Synthesis tools to use:
- `shopify_metric metric=rfm_segments`
- `shopify_metric metric=time_to_repeat`

Steps:
1. Pull `shopify_metric metric=rfm_segments`. Read each group's average days since last order.
2. Pull `shopify_metric metric=time_to_repeat` for the usual reorder gap.
3. Compare each group's average days since last order with the reorder gap. A group whose average is past two years is mostly lost customers, whatever its name says. Relabel it in the table and say why.
4. For each group: customers, share of revenue, average days since last order, the message and channel.

Checks before answering:
- The groups cover every customer back to the store's first order. This cannot limit them to the last 24 months yet. Say so, and say the counts include long-gone customers.
- Recency lines are fixed at 30, 60, 90 and 180 days, not set from this brand's reorder gap. Anyone past 180 days scores lowest. Say so.
- Group counts must add up to total customers. Show the check.
- This gives counts, not a list to send. The list is built in the email or ad platform from the same rules.
- Keep customer emails out of chat.

Output:
- Answer first: which groups are worth a message now.
- Table: group, customers, revenue share, average days since last order, message, channel.
- The rules to rebuild each group in Klaviyo and Meta.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never upload a list to any ad or email account. A person does.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-rfm-audiences". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
