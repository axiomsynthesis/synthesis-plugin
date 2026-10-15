# Has your Meta audience seen enough?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Has your Meta audience seen enough?" (id: grw-meta-frequency-ceiling, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds campaigns showing the same people the same ads too often. It ties rising frequency to rising cost per purchase, week by week, so you can see when a campaign hit its ceiling. It ends with one move per worn-out campaign.

What to read: Meta frequency, reach and cost per purchase by campaign
What to give me: Campaigns whose audience is worn out, and what that is costing you

Synthesis tools to use:
- `meta_metric metric=account_daily`
- `meta_metric metric=reach_frequency`
- `meta_metric metric=frequency`
- `meta_metric metric=campaign_performance limit=25`
- `meta_metric metric=weekly_trend weeks=8`

Steps:
1. Run `meta_metric metric=account_daily` and stop if any account is stale.
2. Pull `meta_metric metric=reach_frequency` and `meta_metric metric=frequency` for frequency and new reach by campaign.
3. Pull `meta_metric metric=weekly_trend weeks=8` and put cost per purchase beside frequency for each of the last eight closed weeks.
4. Flag a campaign when 7-day frequency is above 3 for prospecting (above 6 for retargeting) and cost per purchase rose for two closed weeks in a row.
5. Pull `meta_metric metric=campaign_performance limit=25` to size each flagged campaign's spend.
6. For each flagged campaign, name one move: widen the audience, rotate new creative in, or cap the budget.

Checks before answering:
- Run `meta_metric metric=account_daily` first. An ACCOUNT STALE flag means recent zero spend is missing data, not a pause. Stop and say so before reading any trend.
- Use closed Monday-to-Sunday weeks only. Never compare this week so far.
- A rising frequency with flat cost per purchase is not saturation. Do not flag it.
- If reach is falling while spend is flat, say the audience is shrinking. Check the campaign was not narrowed by a targeting change before blaming fatigue.
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.

Output:
- One line answer first. Then a table with columns campaign, type, weekly spend, 7-day frequency, cost per purchase now vs 4 weeks ago, extra cost per week, move.
- At most 10 rows, ranked by extra cost per week.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never add frequency across campaigns. Frequency does not add up.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-frequency-ceiling". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
