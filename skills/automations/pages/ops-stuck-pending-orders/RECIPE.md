# Catch orders stuck at pending

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Catch orders stuck at pending" (id: ops-stuck-pending-orders, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Watches for one quiet data failure: orders that never move from pending to shipped because the order sync stopped updating old rows. When that happens, revenue, units and customers for closed months are all wrong while every dashboard still looks normal.

What to read: The share of Amazon orders still marked pending in months that have already closed
What to give me: An alert when finished months still carry pending orders, which means the order data stopped updating

Synthesis tools to use:
- `amazon_metric metric=pending_monitor`
- `data_freshness`

Steps:
1. Call `amazon_metric metric=pending_monitor` for the pending share per closed month and its alarm state.
2. Call `data_freshness` to confirm the Amazon order source synced in the last day.
3. If any closed month is above 2% pending, or any month older than 60 days above 0.5%, raise an alert.
4. Name the affected months and the order count involved.

Checks before answering:
- The running month always has pending orders. Never alarm on it.
- A source that has not synced at all makes the share look frozen. Check freshness first.
- A clean result must show the actual shares, not just "fine", so a monitor that silently returned nothing is visible.

Output:
- All clear: one line with the highest closed-month pending share.
- Alert: table Month | Orders | Pending | Share, then one line saying which reports to distrust until fixed.

Never:
- Never edit order data.
- Never call the running month a problem.
- Never report all clear when the monitor returned no rows.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-stuck-pending-orders". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
