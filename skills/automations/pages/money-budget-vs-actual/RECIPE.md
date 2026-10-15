# Budget vs actual, and why

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Budget vs actual, and why" (id: money-budget-vs-actual, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts this month against plan, line by line, and gives the reason for each gap. It points at the one gap worth acting on.

What to read: NetSuite or your plan sheet
What to give me: This month against plan, line by line, with the reason for each gap and the one worth acting on

Synthesis tools to use:
- `monthly_pnl`
- `netsuite_metric metric=opex_category`
- `amazon_metric metric=plan_vs_actual`
- `gsheets_metric metric=breakdown`

Steps:
1. Call `monthly_pnl` with the last closed `month` for actual sales, costs and profit.
2. Call `netsuite_metric` with `metric=opex_category` and `months=3` for spend by category.
3. Call `amazon_metric` with `metric=plan_vs_actual` for that month to compare Amazon to its plan.
4. If the plan lives in a sheet, call `gsheets_metric` with `metric=breakdown` on the plan tab.
5. For each line over or under by more than 5%, find the reason in the channel data.

Checks before answering:
- If no plan is found, say so and stop. Never invent a plan.
- Use the closed month. Bills arrive late and an open month looks under plan.
- A gap needs a reason from the data. If none is found, say "reason not found".

Output:
- One line first: how far over or under plan the month was, in dollars.
- A table: line, plan, actual, gap in dollars, gap in percent, reason.
- One move for next month.

Never:
- Never change the plan or the books. A person does that.
- Never guess a reason the data does not show.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-budget-vs-actual". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
