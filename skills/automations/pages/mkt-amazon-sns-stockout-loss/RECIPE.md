# Subscribers lost when you ran out

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Subscribers lost when you ran out" (id: mkt-amazon-sns-stockout-loss, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
When a subscribed product is out of stock, Amazon skips the delivery and some subscribers cancel. This sizes the loss and flags the next product at risk.

What to read: Amazon's weekly Subscribe and Save results including units lost to out of stock, its 90-day subscription forecast, and days of stock cover
What to give me: Subscription deliveries missed because you ran out, what that cost, and which products are at risk next

Synthesis tools to use:
- `amazon_metric metric=sns_program weeks=12`
- `amazon_metric metric=days_of_cover limit=40`

Steps:
1. Call `amazon_metric metric=sns_program weeks=12`. Read weekly out-of-stock losses and the 30, 60 and 90-day forecast.
2. Call `amazon_metric metric=days_of_cover limit=40`.
3. For each subscribed product: compare its forecast subscription units with stock on hand. Flag any that will run short before the next shipment can arrive.

Checks before answering:
- Weeks are closed Sunday to Saturday. Never include the open week.
- Stock is Amazon's live count. Quote Amazon's update time.
- Amazon's lifetime subscriber versus non-subscriber spend comparison is biased toward subscribers. Never present it as the value of subscribing.

Output:
- One line: units and dollars lost to stockouts in 12 weeks.
- A table: product, units lost, dollars lost, days of cover, 30-day subscription forecast, at risk yes or no.

Never:
- Never create shipments.
- Never treat Amazon's forecast as a promise.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-sns-stockout-loss". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
