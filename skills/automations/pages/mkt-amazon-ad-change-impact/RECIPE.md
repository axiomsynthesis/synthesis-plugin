# Did that ad change actually work?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did that ad change actually work?" (id: mkt-amazon-ad-change-impact, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Agencies and teams make many changes and rarely check them. This lists each change and compares the campaign before and after.

What to read: Every bid, budget, pause and new keyword between daily ads snapshots, and campaign results before and after each change
What to give me: Every ad change from the last month, and what happened to spend and sales after it, on a fair comparison

Synthesis tools to use:
- `amazon_metric metric=ppc_account_changes days=45 limit=100`
- `amazon_metric metric=ppc_campaigns limit=50`
- `amazon_metric metric=ppc_purchase_latency days=60 limit=10`

Steps:
1. Call `amazon_metric metric=ppc_account_changes days=45 limit=100`. Use `by_campaign_day` for each campaign's changes by date and `by_date` for the whole account. Each change is dated to the first day it was seen, so the after window starts the day after that date.
2. Call `amazon_metric metric=ppc_purchase_latency days=60 limit=10`. Only judge changes old enough that their after-window has mostly collected its sales.
3. For each campaign with a change, call `amazon_metric metric=ppc_campaigns` for the 14 days before and the 14 days after (same length both sides).
4. Report the change in spend, sales and return per dollar. Mark each change worked, did not work, or too early.

Checks before answering:
- Two changes to one campaign inside one window cannot be separated. Say so instead of crediting one.
- Season and promotions move everything. If a deal ran in either window, say the comparison is unfair.
- If the change list is empty, check a snapshot exists before saying nothing changed.

Output:
- One line: how many changes paid off.
- A table: date, campaign, change, spend before and after, sales before and after, verdict.

Never:
- Never reverse a change in the account.
- Never credit a result to a change when several changes overlap.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-change-impact". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
