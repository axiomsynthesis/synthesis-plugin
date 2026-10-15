# Find ads that run out of budget by lunch

Channel: Amazon · Level: On a schedule · Status: Ready after we build it
Schedule: every weekday 3pm

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find ads that run out of budget by lunch" (id: amazon-ad-budget-pacing-check, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks each afternoon which ad campaigns ran out of budget early. It sizes the sales you likely missed after the cap hit, and flags Meta campaigns that are spending too fast or too slow.

What to read: Amazon Ads, Meta
What to give me: Campaigns that hit their cap early each day, and the sales you missed after they went dark

Synthesis tools to use:
- `amazon_metric metric=ppc_budget_utilisation`
- `amazon_metric metric=ppc_campaigns`
- `meta_metric metric=pacing_anomaly`

Steps:
1. Call `amazon_metric` with `metric=ppc_budget_utilisation`, `days=7` and `limit=20` for campaigns that spent their whole daily budget and how often.
2. Call `amazon_metric` with `metric=ppc_campaigns` and `days=7` for each capped campaign's return on ad spend and sales.
3. Estimate missed sales: the capped hours times the campaign's normal sales per hour.
4. Call `meta_metric` with `metric=pacing_anomaly` and `days=7` for Meta campaigns pacing off plan.
5. Rank by missed sales, and keep only campaigns that make money at their current return.

Checks before answering:
- Today's ad data is still landing. Judge yesterday and earlier only.
- A campaign that caps once is not a pattern. Say how many of the last seven days it capped.
- Only suggest more budget for campaigns that are profitable. A capped losing campaign is fine capped.
- If a read returns nothing, say it could not be read. Never say "nothing capped" from an empty result.

Output:
- One line first: how many campaigns capped and the sales missed in dollars.
- A table: campaign, days capped, time it capped, return on ad spend, sales missed.
- One move: which budget to raise first and by how much, and how we will know.

Never:
- Never change a budget or bid in Amazon Ads or Meta. A person does that.
- Never guess missed sales without showing the math.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-ad-budget-pacing-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 3pm). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. The data is ready, but the daily run still needs to be set up. Do the parts you can and say plainly what is missing.
