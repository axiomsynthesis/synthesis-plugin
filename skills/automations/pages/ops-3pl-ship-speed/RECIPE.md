# Is your warehouse shipping on time?

Channel: Inventory · Level: On a schedule · Status: Ready after we build it
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your warehouse shipping on time?" (id: ops-3pl-ship-speed, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks every week whether your warehouse ships on time. Late shipping drives support tickets, refunds and bad reviews, and the warehouse's own report rarely shows it by day of week.

What to read: Order and shipment timestamps from your third-party warehouse
What to give me: How fast your warehouse ships against its promise, and which days or sites slip

Synthesis tools to use:
- `shopify_metric metric=daily_revenue days=30`

Steps:
1. Once connected, read orders received and shipped times by warehouse for the last 7 and 28 days.
2. Compute the share shipped within the promised window, by warehouse and by day the order arrived.
3. Call `shopify_metric metric=daily_revenue days=30` to check order counts match the website so no orders are missing from the warehouse feed.
4. Flag any day or warehouse below the promised rate.

Checks before answering:
- Use business days and the warehouse's cut-off time, which the person should give.
- A shipment table with fewer orders than the website means a feed gap, not fast shipping.
- An empty pull replaces the table. Check the sync before believing zero.

Output:
- Table: Warehouse | Orders | Shipped on time | Rate | Worst day.
- Two lines: late orders this week and the pattern behind them.

Never:
- Never contact the warehouse or change its settings.
- Never count a missing shipment as on time.
- Never handle the warehouse key.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-3pl-ship-speed". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): The ShipHero connector exists but no brand has connected one and there is no reader tool. Needs a connected account and a fulfilment tool returning order-received and shipped times by warehouse. Runs from Claude Code, so it only runs while your computer is on. Do the parts you can and say plainly what is missing.
