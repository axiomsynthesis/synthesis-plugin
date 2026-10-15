# Draft the investor update

Channel: Money · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Draft the investor update" (id: money-investor-or-board-update, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Drafts a one-page monthly update for investors or a board with the numbers already in it. It keeps to two wins, one problem and one ask.

What to read: All channels
What to give me: A one-page monthly update with the numbers in: two wins, one problem, one ask, and cash

Synthesis tools to use:
- `monthly_pnl`
- `channel_revenue_mix`
- `yoy_comparison`
- `working_capital`
- `export_docx`

Steps:
1. Call `monthly_pnl` for the last closed `month` for revenue, margin and profit.
2. Call `channel_revenue_mix` for the split across Amazon, retail and website.
3. Call `yoy_comparison` for growth against the same period last year.
4. Call `working_capital` for cash and runway.
5. Write the page and save it with `export_docx` as board-update.docx.

Checks before answering:
- Use the last closed month only.
- If a number fails to read, the draft says "not available" in its place. Never fill it in.
- A one-month jump is not a trend. Say so if growth rests on one month.

Output:
- A Word file, board-update.docx, one page: headline numbers, two wins, one problem, one ask, cash.

Never:
- Never send the update. A person edits and sends it.
- Never round a number up to make it look better.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-investor-or-board-update". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
