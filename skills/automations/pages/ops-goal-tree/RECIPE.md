# What it takes to hit the goal

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What it takes to hit the goal" (id: ops-goal-tree, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Breaks a revenue goal into the levers that produce it: shoppers, conversion, price per unit, new and repeat customers. It shows how much each lever must move and compares that with the best the business has ever done, so a goal is either backed by a plausible plan or reset.

What to read: Traffic, conversion, price per unit, repeat rate and new customers today
What to give me: Your revenue goal broken into its drivers, the lift each needs, and how realistic that lift is

Synthesis tools to use:
- `amazon_metric metric=conversion month=YYYY-MM`
- `new_vs_repeat`
- `metric_timeseries metric_keys=[revenue,customers,new_customers] start_month=YYYY-MM end_month=YYYY-MM`
- `funnel_decomposition`

Steps:
1. Ask for the goal, the channel and the deadline.
2. Call `metric_timeseries metric_keys=["revenue","customers","new_customers"]` for the last 24 months.
3. Call `amazon_metric metric=conversion month=YYYY-MM` for sessions, units ordered and sales, for each of the latest full months it holds. Amazon traffic history reaches back only about six months, so a month older than that comes back empty, not zero.
4. Call `new_vs_repeat` for the new and repeat split.
5. Write Amazon revenue as sessions times units per session times sales per unit, all three from the one read in step 3. Its conversion counts units, not orders, so never multiply it by an order value. Run `funnel_decomposition stages=[{name, count}]` with sessions then units.
6. Solve for the lift needed in each lever alone, then propose a mix.
7. Compare each lever's needed lift with the best gain in the history each read holds: 24 months for revenue and customers from step 2, about six months for sessions, conversion and price per unit from step 3. Say how far back each reaches.

Checks before answering:
- Use full months, and leave out event months from the base or say they are in.
- Units and orders are different. Keep every lever on units, the way the conversion read counts them.
- A lever with no history of the needed lift is a stretch. Say so plainly.

Output:
- Table: Lever | Today | Needed (alone) | Proposed mix | Best past gain and how far back it reaches.
- Two lines: whether the goal is realistic, and the lever to work on first.

Never:
- Never change the goal for the founder.
- Never assume all levers move together.
- Never make account changes.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-goal-tree". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
