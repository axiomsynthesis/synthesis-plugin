# Monday ad check with no fake drops

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Monday ad check with no fake drops" (id: mkt-amazon-ppc-honest-week-compare, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon keeps adding sales to a click for up to 30 days. So last week always looks worse than the week before in the console.
This compares the two weeks at the same age, so a fall is a real fall. It also lists what was changed in the account that week.

What to read: Sponsored Products results for last week and the week before, held at the same number of days since each click
What to give me: This week's ads against last week, without the fake drop that comes from last week's sales still landing

Synthesis tools to use:
- `amazon_metric metric=ppc_week_over_week`
- `amazon_metric metric=ppc_purchase_latency days=60 limit=10`
- `amazon_metric metric=ppc_account_changes days=14 limit=50`

Steps:
1. Call `amazon_metric metric=ppc_week_over_week` with no dates. It picks the last two closed weeks and holds them at the same age.
2. Call `amazon_metric metric=ppc_purchase_latency days=60 limit=10` and note what share of sales usually lands in the first 7 days. Say how much last week will still grow.
3. Call `amazon_metric metric=ppc_account_changes days=14 limit=50` to list bids, budgets and pauses changed in the two weeks.
4. Write the readout: spend, sales, return per dollar and orders, each with its change. Name any account change that lines up with a big move.

Checks before answering:
- Confirm the result reports the same attribution age for both weeks. If it does not, do not compare.
- If spend is zero for either week, check the ads connection is live before saying ads stopped.
- If the change list is empty, say whether an account snapshot exists. Empty can mean "no snapshot", not "no changes".
- Never put the console's raw week-over-week drop in the headline.

Output:
- Five lines or fewer: the headline change at equal age, spend, return per dollar, the one account change that matters, and the one move if any.
- A small table: metric, last week, week before, change.

Never:
- Never compare a just-closed week with an older week at face value.
- Never change anything in the ads account.
- Never send this anywhere the person has not set up and approved.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ppc-honest-week-compare". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
