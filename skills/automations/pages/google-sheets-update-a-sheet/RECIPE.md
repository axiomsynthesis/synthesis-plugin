# Fill in my Google Sheet

Channel: Google Sheets · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fill in my Google Sheet" (id: google-sheets-update-a-sheet, Google Sheets).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads a sheet you already use, like your forecast or reorder sheet, and fills the numbers from Synthesis. It lists every cell it changed. Until Google allows writing, it hands back an updated copy.

What to read: The sheet you pick, your Synthesis numbers
What to give me: Your sheet filled with fresh numbers, and a list of every cell that changed

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=profile`
- `amazon_metric metric=daily_revenue`
- `export_xlsx`

Steps:
1. Call `gsheets_metric` with `metric=tables` to find the sheet and tab you named.
2. Call `gsheets_metric` with `metric=profile` and that `table` to read its columns and which cells are blank.
3. Pull each needed number from Synthesis, for example `amazon_metric` with `metric=daily_revenue` and `days=30` for sales.
4. Use `export_xlsx` with `filename=updated-sheet.xlsx`: one tab with the updated sheet and one tab listing cell, was, now, source.

Checks before answering:
- Only fill a cell when the source number came back. A failed read leaves the cell as it was and is listed.
- Match the sheet's own units and dates. A monthly cell never gets a weekly figure.
- If the sheet cannot be read, say so and stop.

Output:
- One line first: how many cells changed.
- An Excel file, updated-sheet.xlsx, with the sheet and a change list: cell, was, now, where the number came from.

Never:
- Never overwrite a cell a person typed by hand without listing it.
- Never guess a number to fill a blank.
- Never write to the live sheet. A person pastes the copy in.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: google-sheets-update-a-sheet". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): We can read sheets you pick. Writing back needs a broader Google permission that Google reviews, so for now it makes a new copy for you to paste in. Do the parts you can and say plainly what is missing.
