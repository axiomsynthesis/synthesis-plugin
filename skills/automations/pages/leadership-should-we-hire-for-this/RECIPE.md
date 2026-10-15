# Will this hire pay for itself?

Channel: Leadership · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Will this hire pay for itself?" (id: leadership-should-we-hire-for-this, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Works out whether a new hire pays for themselves. It finds the money the role would control, the improvement needed to cover the full cost, and the case for and against.

What to read: Channel results, costs
What to give me: The improvement the hire must deliver to pay back, how fast, and the case for and against

Synthesis tools to use:
- `monthly_pnl`
- `channel_revenue_mix`
- `amazon_metric metric=ppc_search_terms`
- `meta_metric metric=roas`
- `strategy_framework`

Steps:
1. Ask the owner for the role, the channel or area it owns, and the full yearly cost.
2. Call `monthly_pnl` for the last 3 closed months to get margin and spend, and `channel_revenue_mix` to size the channel the role would own.
3. Read the channel's own results. For Amazon ads, `amazon_metric` with `metric=ppc_search_terms` and `days=60`. For Meta, `meta_metric` with `metric=roas` for each of the last two closed months (`month=YYYY-MM`).
4. Work out break-even: the yearly cost divided by the monthly dollars the role controls, as the change needed.
5. Call `strategy_framework framework=pros_cons decision=<hire or not> options=[{name, pros, cons}]` with the numbers in each point, for the case for and against.

Checks before answering:
- Use the full cost of the hire, not only salary. Say what was included.
- The improvement needed must be compared with what is in reach, using the channel's own waste or gap.
- If the channel data is missing, say break-even cannot be set. Never guess it.

Output:
- One line first: the change the hire must deliver to pay back, and in how many months.
- A short table: cost a year, dollars the role controls, change needed, what is in reach.
- Three reasons for, three against, and one test to try before hiring.

Never:
- Never make the hiring call for the owner.
- Never use a revenue number as if it were profit.
- Nothing changes in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-should-we-hire-for-this". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
