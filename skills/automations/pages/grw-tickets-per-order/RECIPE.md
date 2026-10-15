# Is support load growing faster than sales?

Channel: Support · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is support load growing faster than sales?" (id: grw-tickets-per-order, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Divides tickets by orders each week. A rising rate means something in the product, shipping or site is getting worse, even when total tickets look fine because sales grew.

What to read: Gorgias ticket volume and Shopify orders by week
What to give me: Tickets per 100 orders over time, and which topic drives the rise

Synthesis tools to use:
- `gorgias_metric metric=ticket_volume months=6`
- `shopify_metric metric=weekly_revenue weeks=26`
- `gorgias_metric metric=contact_reasons months=6`

Steps:
1. Pull `gorgias_metric metric=ticket_volume months=6`.
2. Pull `shopify_metric metric=weekly_revenue weeks=26` for orders.
3. Compute tickets per 100 orders by week.
4. Pull `gorgias_metric metric=contact_reasons months=6` to see which reason grew most.

Checks before answering:
- If Gorgias is not connected, say the helpdesk is not connected. Never say zero tickets.
- Amazon orders do not create website support tickets. Use website orders only, and say so.
- Read tag categories, never raw tag counts. Raw tags mix real reasons with spam and auto-replies.
- Exclude the current week.

Output:
- Answer first. A weekly table: orders, tickets, tickets per 100 orders. One line on the reason that grew.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tickets-per-order". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
