# Did the price or bid change make money?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did the price or bid change make money?" (id: mkt-amazon-change-daily-profit, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Monthly profit hides a change made mid-month. This reads profit per day and compares the days before and after a change.

What to read: Daily Amazon profit before and after a change you made, on the products it touched
What to give me: Profit per day before and after a price, bid or coupon change, so you know in two weeks, not at month end

Synthesis tools to use:
- `cost_rules for=mkt-amazon-change-daily-profit`
- `amazon_metric metric=pnl_daily days=42 grain=day`
- `amazon_metric metric=ppc_account_changes days=42 limit=50`
- `log_decision`

Steps:
1. Ask what changed, on which products, and on what date.
2. Call `amazon_metric metric=pnl_daily days=42 grain=day`. Compare equal-length windows before and after, excluding the change day.
3. If the change was in ads, call `amazon_metric metric=ppc_account_changes days=42 limit=50` to confirm the date and look for overlapping changes.
4. If the person decides to keep or reverse, record it with `log_decision`, with the number to watch and the date to check.

Checks before answering:
- The headline is the measured line. Fee and cost lines on recent days are modelled. Say which you used.
- Under 7 days after the change is too early. Say so.
- Another change or a promotion in either window makes the comparison unfair. Name it.

Output:
- One line: keep, reverse or too early.
- A table: window, units per day, sales per day, profit per day.

Never:
- Never change prices or bids.
- Never present modelled daily fees as settled.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-change-daily-profit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
