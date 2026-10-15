# Move ad money to campaigns that run out

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Move ad money to campaigns that run out" (id: mkt-amazon-budget-reallocation, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A campaign that runs out of budget every day is turning shoppers away. A campaign that never runs out and returns little is wasting money.
This finds both and drafts a budget move that keeps the account total the same.

What to read: How often each campaign spends its whole daily budget, and each campaign's return per dollar
What to give me: A budget move list that takes money from weak campaigns and gives it to profitable ones that run dry every day

Synthesis tools to use:
- `amazon_metric metric=ppc_budget_utilisation days=30 limit=50`
- `amazon_metric metric=ppc_campaigns days=30 limit=50`
- `amazon_metric metric=ppc_rollups days=30 limit=30`

Steps:
1. Call `amazon_metric metric=ppc_budget_utilisation days=30 limit=50`. Note each campaign's cap-out days.
2. Call `amazon_metric metric=ppc_campaigns days=30 limit=50` for spend, sales and return per dollar across all three ad types.
3. Call `amazon_metric metric=ppc_rollups days=30 limit=30` to see portfolio budget caps. A portfolio cap can block a campaign raise.
4. Donors: campaigns below the account's break-even return with no cap-outs. Receivers: campaigns above break-even that cap out on more than half the days.
5. Draft moves in whole dollars a day. Keep the account total flat.

Checks before answering:
- The cap-out read shows how often the cap binds, not how many sales were lost. Never print a "lost sales" dollar figure.
- Leave branded campaigns out of the donors unless the person asks. Their job is defense.
- A receiver whose portfolio is already at its cap needs the portfolio raised too. Say so.
- If no campaign caps out, say so plainly. That is a real answer.

Output:
- One line: total dollars a day to move and the expected direction.
- A table: campaign, role (give or receive), daily budget now, suggested, return per dollar, cap-out days.

Never:
- Never change budgets in the account.
- Never raise the account's total budget here. That is a separate decision.
- Never claim a dollar figure for lost impressions. The data does not hold it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-budget-reallocation". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
