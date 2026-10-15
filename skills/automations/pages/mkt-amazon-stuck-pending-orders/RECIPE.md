# Catch Amazon orders stuck at pending

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Catch Amazon orders stuck at pending" (id: mkt-amazon-stuck-pending-orders, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
An order should not still be pending weeks after its month closed. If many are, the sync stopped updating them and every sales number for that month is off.
This checks once a week and raises the alarm only when something is wrong.

What to read: The share of orders in each closed month still marked pending
What to give me: An alarm when a finished month still has Amazon orders stuck at pending, which means that month's sales are wrong

Synthesis tools to use:
- `amazon_metric metric=pending_monitor months=6`
- `data_freshness`

Steps:
1. Call `amazon_metric metric=pending_monitor months=6`.
2. If any closed month shows an alarm, call `data_freshness` to see when Amazon orders last synced.
3. Report the month, the pending share, and the dollars sitting in pending.

Checks before answering:
- The current month always has pending orders. Never alarm on it.
- A clean result with no months in it is not clean. Check the tool returned closed months.

Output:
- One line if clean.
- If not: month, pending share, pending dollars, last sync time, and "sales for this month cannot be trusted until fixed".

Never:
- Never adjust order data.
- Never report a month as clean when the check returned nothing.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-stuck-pending-orders". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
