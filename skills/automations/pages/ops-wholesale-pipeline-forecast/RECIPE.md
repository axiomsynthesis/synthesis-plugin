# Wholesale deals likely to close

Channel: Retail · Level: Advise · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Wholesale deals likely to close" (id: ops-wholesale-pipeline-forecast, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns the CRM's open pipeline into a revenue estimate using your own track record, not the stage percentages in the CRM. It also checks whether you are building new pipeline as fast as you close it.

What to read: Open sales opportunities by stage, win rates and time to close from the CRM
What to give me: Wholesale revenue likely to close over the next two quarters, weighted by your own win rates

Synthesis tools to use:
- `salesforce_metric metric=pipeline_by_stage`
- `salesforce_metric metric=win_rate days_back=365`
- `salesforce_metric metric=sales_cycle_length days_back=365`
- `salesforce_metric metric=pipeline_trend months=12`

Steps:
1. Call `salesforce_metric metric=pipeline_by_stage` for open opportunities by stage and amount.
2. Call `salesforce_metric metric=win_rate days_back=365` for win rate by count and by value.
3. Call `salesforce_metric metric=sales_cycle_length days_back=365` for days from creation to close.
4. Weight open pipeline by the value-based win rate. Place it in quarters using each opportunity's age plus the average cycle.
5. Call `salesforce_metric metric=pipeline_trend months=12` and compare pipeline created with pipeline won per month.

Checks before answering:
- If the CRM is not connected, say so and stop.
- Win rate by count and by value can differ a lot when a few big deals decide it. Show both and use value.
- Stale opportunities older than twice the average cycle are unlikely. List them separately.
- Fewer than 20 closed opportunities makes the win rate a rough guide. Say so.

Output:
- Table: Quarter | Open pipeline | Weighted estimate.
- Three lines: the weighted total, whether pipeline creation keeps up, and the stale deals to clean up.

Never:
- Never edit or close an opportunity.
- Never use the CRM's stage probabilities as if measured.
- Never add pipeline to booked revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-wholesale-pipeline-forecast". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): A connected CRM with synced deals. No brand has one connected yet, so these reads have never run on real data and do not appear in Claude until one is connected. Do the parts you can and say plainly what is missing.
