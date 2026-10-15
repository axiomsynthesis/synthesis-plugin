# Does your sheet match the real numbers?

Channel: Google Sheets · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does your sheet match the real numbers?" (id: ops-sheet-vs-warehouse-drift, Google Sheets).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Many teams run on a sheet where someone types last week's numbers. This checks those typed numbers against the measured source, so a formula error or a definition mismatch is found before it reaches a board deck.

What to read: A metric your team types into a Google Sheet and the same metric measured from the source
What to give me: Week by week, where your sheet and the measured figure disagree, and by how much

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=profile table=<table>`
- `gsheets_metric metric=trend table=<table> date_column=<col> value_column=<col> grain=week`
- `query_series metric=net_revenue grain=week`

Steps:
1. Call `gsheets_metric metric=tables` to list connected tabs.
2. Call `gsheets_metric metric=profile table=<table>` and read each column's type, cast failures and example values. Pick the date and value columns from the profile, never from the column name alone.
3. Call `gsheets_metric metric=trend table=<table> date_column=<col> value_column=<col> grain=week`.
4. Pull the measured figure on the same definition, for example `query_series metric=net_revenue grain=week`.
5. Compare week by week. Flag weeks off by more than 3%.
6. Look for a pattern in flagged weeks (deal weeks, month ends, one person's entries).

Checks before answering:
- If more than a tenth of a column fails to read as numbers, the trend is capped. Say so.
- Rates cannot be summed into a coarser period. Compare rates at their own grain.
- A week the operator has not filled yet is not a zero.
- When they disagree, show both. Settlement wins for money tied to the bank; the measured source wins for operational metrics; the sheet wins for targets and plans.

Output:
- Table: Week | Sheet | Measured | Gap.
- Two lines: whether the tab can be trusted, and the likely cause of any pattern.

Never:
- Never write to the sheet.
- Never surface people's names, phone numbers or addresses from a tab.
- Never average the sheet and the source.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-sheet-vs-warehouse-drift". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
