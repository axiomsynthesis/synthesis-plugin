# Know when website tracking breaks

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: daily 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know when website tracking breaks" (id: grw-ga4-tracking-health, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every morning, compares the purchases GA4 recorded with the orders Shopify actually took. A sudden gap means a tag broke, and every ad platform fed by that tag will start making bad decisions.

What to read: GA4 purchase events against real Shopify orders, day by day
What to give me: A morning alert when site tracking stops counting sales, before your ad platforms start guessing

Synthesis tools to use:
- `ga4_metric metric=events days=14 limit=50`
- `shopify_metric metric=daily_revenue days=14`

Steps:
1. Pull `ga4_metric metric=events days=14 limit=50` and read the purchase event count per day.
2. Pull `shopify_metric metric=daily_revenue days=14` for orders per day.
3. Compute GA4 purchases over Shopify orders per day.
4. Alert when yesterday's ratio is below 70% of its 14-day median.

Checks before answering:
- Shopify days are UTC and GA4 days follow the property's time zone. Compare 7-day sums too, so a time zone shift is not an alert.
- Subscription renewals do not fire a purchase event. A steady gap is normal. Only a change in the gap is an alert.
- Never alert on today.

Output:
- When healthy: one line. When not: the day, the ratio, the normal ratio, and where to look.

Never:
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-ga4-tracking-health". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (daily 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
