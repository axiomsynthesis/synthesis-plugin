# Weekly operations red-amber-green

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Weekly operations red-amber-green" (id: ops-operations-scorecard, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Gives the operations lead one table every Monday: stock, Buy Box, refunds, support speed and data health. It is the operations slice of the business, not the whole-business brief, and each line has a threshold so red means something.

What to read: Stock cover, out-of-stock products, Buy Box share, refunds, support resolution times and data freshness
What to give me: One weekly table of operations health, each line red, amber or green against a limit you set

Synthesis tools to use:
- `amazon_metric metric=days_of_cover limit=100`
- `amazon_metric metric=buybox_health`
- `return_rate month=YYYY-MM`
- `gorgias_metric metric=resolution_sla months=3`
- `data_freshness`
- `metric_health_band`

Steps:
1. Call `amazon_metric metric=days_of_cover limit=100` for products out of stock and products under 30 days of cover.
2. Call `amazon_metric metric=buybox_health` for Buy Box share per product.
3. Call `return_rate month=YYYY-MM` for the last full month.
4. If support is connected, call `gorgias_metric metric=resolution_sla months=3`.
5. Call `data_freshness` so a stale source is a line on the card, not a hidden cause.
6. For each line call `metric_health_band` with the value and the thresholds the person set. Where none was set, show the value with no colour.

Checks before answering:
- A failed stock read is not zero stock. If the stock feed failed, the stock line is "not read", red.
- Sales lost to stockout use the product's pace before it ran out.
- Thresholds are the person's. Never colour a line with a made-up threshold.
- A source not connected is shown as "not connected", never green.

Output:
- Table: Area | This week | Last week | Threshold | Status.
- Two lines: the red items in dollars, and the owner who should act.

Never:
- Never change stock, listings or support settings.
- Never invent a threshold.
- Never hide a not-connected source.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-operations-scorecard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
