# Map your operating spreadsheets

Channel: Google Sheets · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Map your operating spreadsheets" (id: ops-workbook-map, Google Sheets).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes stock of the sheets a team runs on so Synthesis knows which columns are the team's own knowledge (targets, owners, plans, offline costs) and which only repeat source data. It is the first step before any sheet-based report.

What to read: Every connected Google Sheet tab, its columns and its row counts
What to give me: What each tab holds, which columns exist nowhere else, and which copy data we already measure

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=profile table=<table>`
- `list_documents`

Steps:
1. Call `gsheets_metric metric=tables` for every connected tab and its row count.
2. For each tab with rows, call `gsheets_metric metric=profile table=<table>` for column types, fill rates and cast failures.
3. Call `list_documents` to see which tabs are also stored as documents.
4. Sort each tab into: TEAM KNOWLEDGE (targets, budgets, owners, plans, offline costs), DUPLICATES MEASURED DATA (sales, ad spend, stock), FORM RESPONSES OR PEOPLE DATA, EMPTY.
5. For team-knowledge tabs, note the date column and value columns a report would use.

Checks before answering:
- A tab with no row count is not empty until a live read confirms it.
- Decide meaning from the columns and a definition row, never from the tab name alone.
- Tabs holding people's details are listed by name only. Never show their contents.

Output:
- Table: Tab | Rows | Category | Useful columns | Date column.
- Two lines: the tabs worth wiring into reports, and any tab that looks stale (no new rows in 30 days).

Never:
- Never write to a sheet.
- Never copy names, phone numbers, emails or addresses out of a tab.
- Never treat a form-response tab as a source of definitions.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-workbook-map". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
