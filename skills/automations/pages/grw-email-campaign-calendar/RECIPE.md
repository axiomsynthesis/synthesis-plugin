# Plan next month's emails

Channel: Email · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan next month's emails" (id: grw-email-campaign-calendar, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds next month's send plan from what has worked: which campaign types earned, when your customers usually reorder, and the season. Each send gets a date, an audience, a goal and an angle.

What to read: Past campaign results, your sales seasonality and buying cycle
What to give me: A dated email and SMS calendar for next month, with the goal of each send

Synthesis tools to use:
- `klaviyo_metric metric=campaign_scorecard limit=40`
- `shopify_metric metric=seasonality`
- `shopify_metric metric=time_to_repeat`
- `klaviyo_metric metric=send_timing`

Steps:
1. Pull `klaviyo_metric metric=campaign_scorecard limit=40` and group by campaign type: product, education, sale, launch, social proof.
2. Pull `shopify_metric metric=seasonality` for next month's usual weight.
3. Pull `shopify_metric metric=time_to_repeat` for the typical gap to a second order.
4. Pull `klaviyo_metric metric=send_timing` for the default slot.
5. Ask for launches, sales and stock limits next month, then lay out 6 to 10 sends.

Checks before answering:
- Most brands have under a year of sends. Say how many campaigns a finding rests on, and call anything under 10 a hint, not a result.
- Never plan a sale send on a product the person says is short on stock.
- Open rates are inflated by Apple's privacy auto-opens. Judge on clicks and placed orders, never on opens alone.

Output:
- A table: date, channel, audience, type, goal, angle, subject idea. Also a spreadsheet via `export_xlsx` named email-calendar-<month>.xlsx when asked.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Nothing is scheduled in Klaviyo. A person builds the sends.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-campaign-calendar". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
