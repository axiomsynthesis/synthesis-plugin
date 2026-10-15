# Prove whether a channel drives sales

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Prove whether a channel drives sales" (id: strategy-test-plan-for-a-channel, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Designs a clean on and off test that proves whether a channel really drives sales. It picks matched regions or weeks, sets the dates, and writes down the result that would count as success before the test starts.

What to read: Channel spend and sales by region or week
What to give me: An on-and-off test with matched regions or weeks, dates, the success number and the cost

Synthesis tools to use:
- `meta_metric metric=creative_geo`
- `shopify_metric metric=state_revenue`
- `amazon_metric metric=geo_penetration`
- `meta_metric metric=weekly_trend`
- `measurable_test`
- `export_docx`

Steps:
1. Call `meta_metric` with `metric=creative_geo` and `days=90` for spend by state.
2. Call `shopify_metric` with `metric=state_revenue` (lifetime totals; it takes no time window, so say so) and `amazon_metric` with `metric=geo_penetration` and `months=6`, for sales by state.
3. Pick test and control states that look alike in size and trend over the past 12 weeks.
4. Call `meta_metric` with `metric=weekly_trend` and `weeks=26` to pick test weeks clear of deals and holidays.
5. Call `measurable_test` with the claim, the metric, the check date, and the success and warning thresholds.
6. Call `export_docx` with `filename=channel_test_plan.docx`.

Checks before answering:
- Test and control must match before the test. Show the past 12 weeks side by side.
- The test must be long enough to see a change bigger than normal week to week noise. Say the size of that noise.
- If state sales are missing for a channel, say so and fall back to a test by weeks.

Output:
- A Word file named `channel_test_plan.docx`, one page.
- It holds: the question, test and control regions, start and end dates, the success number, the warning number, and the cost of the test in dollars.
- A person approves it and makes the change in the ad account.

Never:
- Never pause or change any campaign. A person does that.
- Never move the success number after the test starts.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: strategy-test-plan-for-a-channel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
