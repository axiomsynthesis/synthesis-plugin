# This week's Meta to-do list

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "This week's Meta to-do list" (id: meta-change-list, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists the exact pauses, budget changes and new ad sets to make this week.
Each change has its reason, and the list is ordered by money at stake.
A person applies them in Ads Manager.

What to read: Meta ads
What to give me: The exact pauses, budget changes and new ad sets to make, ordered by money at stake

Synthesis tools to use:
- `meta_metric metric=adset_performance`
- `meta_metric metric=pacing_anomaly`
- `meta_metric metric=frequency`
- `export_xlsx`

Steps:
1. Call `meta_metric` with `metric=adset_performance` to get spend, sales and cost per sale by ad set. This read has no date setting, so say the dates the result covers.
2. Call `meta_metric` with `metric=pacing_anomaly` and `days=14` to find ad sets that hit their budget early or stopped spending.
3. Call `meta_metric` with `metric=frequency` for the latest month to find audiences that are seeing the same ads too often.
4. Turn each finding into one change with a reason and a dollar effect, then rank by money at stake.
5. Call `export_xlsx` with `filename=meta_change_list.xlsx` holding the checklist.

Checks before answering:
- Meta's last few days are still filling in. Judge on closed days.
- If a read is empty, say it could not be read. Never pause something because data was missing.
- An ad set with tiny spend cannot be judged. Leave it off and say how many were skipped.

Output:
- A checklist table: change, ad set, why, money at stake a week, done box.
- The file meta_change_list.xlsx, about 5 to 10 rows.

Never:
- Nothing goes live in any account. A person applies the changes in Ads Manager.
- Never raise a budget past what the brand has set as its cap.
- Never guess a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-change-list". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
