---
description: "Amazon daily check: A short numbered list of what needs a person today, biggest dollars first, with what could not be checked said out loud"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Amazon daily check

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: every weekday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon daily check" (id: amazon-morning-checklist, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs the brand's daily Amazon checks and returns one short numbered list of what needs a person today, with yesterday's profit on top and the core searches below.

What to read: Amazon stock, Buy Box, money owed, ad waste, rank, ratings, yesterday's sales, ad budgets and month pace
What to give me: A short numbered list of what needs a person today, biggest dollars first, with what could not be checked said out loud

Synthesis tools to use:
- `amazon_metric metric=stockout_forecast limit=200`
- `amazon_metric metric=buybox_watch limit=50`
- `amazon_metric metric=fba_ship_plan transit_days=20`
- `amazon_metric metric=money_found`
- `amazon_metric metric=organic_rank days=21 limit=60`
- `amazon_metric metric=review_velocity days=30 limit=40`
- `amazon_metric metric=daily_revenue days=10`
- `amazon_metric metric=cancellations`
- `amazon_metric metric=ppc_budget_utilisation days=7 limit=50`
- `amazon_metric metric=keyword_spend_drops`
- `amazon_metric metric=goal_pacing`
- `amazon_metric metric=daily_ads_check`
- `business_profit`

Steps:
1. `metric=stockout_forecast`, `limit=200`. Already out with usual sales and nothing landing is "out of stock now", not a run-out date. A run-out inside the lead time with nothing landing is a line. Use 30 days if none is set, and say so.
2. `metric=buybox_watch`, `limit=50`. List a top-10 seller off the Buy Box for a day or more.
3. Until Nov 30, `metric=fba_ship_plan`, `transit_days=20`. List products that run out by Nov 30 with units to send above 0, and the date to ship by.
4. `metric=money_found`. List money Amazon may owe, ad waste, avoidable storage, fee rises and units never received, with amounts.
5. `metric=organic_rank`, `days=21`, `limit=60`. A drop of 3+ places gets a line only on a search with 10+ purchases a week, 5 at most. Summarize the rest in one line.
6. `metric=review_velocity`, `days=30`, `limit=40`: a rating down 0.1 or more.
7. `metric=daily_revenue`, `days=10`: yesterday, only if down 20% and $200 on the same weekday a week before.
8. `metric=cancellations`, `metric=ppc_budget_utilisation` (`days=7`, `limit=50`), `metric=keyword_spend_drops`, `metric=goal_pacing`: a cancelled share up 3 points, campaigns capped 5 of 7 days, main keywords down 20% from $100 a week, a month behind goal.
9. `metric=daily_ads_check`: ad spend drops by product, the hour budgets stop, and core searches.
10. `business_profit` for yesterday. Open with it, and say what share of product cost is missing.
11. If stock, the Buy Box, sales or ad spend is urgent, also read `metric=ppc_account_changes` (`days=3`), `metric=listing_takedowns` and `metric=days_of_cover`, and say what they show.

Steps 1 to 9 and 11 all use the combined Amazon tool named at the top.

Checks before answering:
- A check that could not run is listed under "Could not check". It is never a clean result.
- A check that needs setup, such as a lead time, ad budget or goal, is listed under "Needs setup".
- The newest day can still fill in. Say so on any drop in yesterday's sales.

Output:
- One line first: how many things to look at today.
- A short message, never a report or a file. Three groups in this order, numbered straight through, 5 lines each at most: "Do today" (anything urgent), "Money to chase" (each line leads with its dollars) and "Keep an eye on" (everything else). Each line has the finding, its number and the next step.
- If a group had more than 5 lines, say how many were left out and offer them.
- Then "Could not check" and "Needs setup", if any.

Never:
- Never change anything in any account. Hand over the step; a person makes it.
- Never say all clear when a check could not run.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Inputs only I know: supplier lead time in days. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Then tell me to save the lead time on the Costs (COGS) page, Lead times & rivals tab. On a scheduled run, name what is missing instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-morning-checklist". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: amazon-morning-checklist".
- This is meant to repeat (every weekday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
