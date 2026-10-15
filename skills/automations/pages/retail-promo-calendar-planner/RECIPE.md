# Plan retail promos that pay

Channel: Retail · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan retail promos that pay" (id: retail-promo-calendar-planner, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks back at every retail promo you ran, sizes the lift in units and in dollars of profit, and ranks them. Then it lays out next quarter's promo plan using the ones that paid.

What to read: Retail POS, promo history
What to give me: Every past retail promo ranked by profit, and next quarter's promo plan

Synthesis tools to use:
- `list_files`
- `search_file_content`
- `read_file`
- `gsheets_metric metric=breakdown`
- `export_xlsx`

Steps:
1. Call `list_files` with `limit=50` and `search_file_content` with `query="promo calendar offers"` and `k=8` to find the promo history and weekly store sales files.
2. Open them with `read_file` and line up each promo's weeks against 4 weeks before and 4 weeks after.
3. If the brand tracks promos in a sheet, call `gsheets_metric` with `metric=breakdown` on that table by promo.
4. For each promo, work out unit lift, the discount cost, and profit after the discount using the costs in the files.
5. Rank promos by profit gained, then build next quarter's calendar with `export_xlsx`, `filename="retail-promo-plan.xlsx"`.

Checks before answering:
- A promo that did not run is not a promo that failed. Drop any marked as not run.
- Compare the promo weeks with a clean baseline, not with another promo week.
- If cost per unit is missing, say profit is unknown. Never count unit lift as a win.
- If no promo history is found, say so plainly.

Output:
- One line first: the best and the worst promo, with dollars made or lost.
- A table: retailer, promo, weeks, unit lift, discount cost, profit after discount.
- File: retail-promo-plan.xlsx with next quarter's plan by week.

Never:
- Never book or change a promo with a retailer. A person does that.
- Never guess a lift when the baseline weeks are missing.
- Never call a promo profitable without its cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: retail-promo-calendar-planner". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Store sales and the retail promo calendar sit in our warehouse, but no customer tool reads them yet, so a retail promo tool has to be built. Until then it works from uploaded retailer files or a connected sheet. Do the parts you can and say plainly what is missing.
