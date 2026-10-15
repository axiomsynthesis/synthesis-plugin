# Catch discount codes leaking online

Channel: Customers · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Catch discount codes leaking online" (id: grw-code-leak-check, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Spots private codes, like one for a single creator or a staff code, being used far beyond their audience. It sizes the discount given away and lists codes to retire.

What to read: Discount codes used on Shopify orders, by code and by day
What to give me: Private codes spreading to coupon sites, with the money they are costing

Synthesis tools to use:
- `shopify_metric metric=order_tags months=3 limit=50`

Steps:
1. When a discount-code reader exists: pull orders and discount dollars by code by day for 90 days.
2. Flag codes whose daily use jumped more than 5 times their first-month rate, and codes used by mostly new customers outside the expected channel.

Checks before answering:
- A code used on a launch day spikes for a good reason. Check dates against the calendar.

Output:
- Table: code, owner, orders, discount dollars, spike date, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never disable a code. A person does.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-code-leak-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Discount codes per order are not exposed by a governed tool. A Shopify discount-code reader is needed. Do the parts you can and say plainly what is missing.
