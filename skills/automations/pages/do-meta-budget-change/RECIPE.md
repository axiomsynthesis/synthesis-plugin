# Change a Meta budget for me

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Change a Meta budget for me" (id: do-meta-budget-change, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Raises or cuts the daily budget on the Meta ad sets you name, or moves their end date.
It works in your own signed-in Ads Manager, because no Meta connection can change a budget today.
It also puts back budgets Meta raised on its own when an ad set was published.

What to read: Each named ad set's daily budget, end date, last 7 closed days of spend, sales and cost per sale, then the same ad set read back live after the change
What to give me: The new daily budget or end date set on each ad set you named, with Meta's own budget bumps undone and the live figure read back

Synthesis tools to use:
- `cost_rules for=do-meta-budget-change`
- `meta_metric metric=ad_returns`
- `meta_metric metric=pacing_anomaly`
- `ad_health_check`
- `log_decision kind=budget`

Steps:
1. Ask which ad sets and the exact new dollar figure for each, or the new end date. A phrase like "150 a day each" gets one question back to confirm it.
2. Call `meta_metric` with `metric=ad_returns` and `limit=50` for 7-day spend, sales and cost per sale of each named ad set. Call `meta_metric` with `metric=pacing_anomaly`. If a named ad set's campaign spiked or stalled in the last 3 days, say so first.
3. Call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","schedule_budget"]` for each one to read its live budget, end date and switches. If it ends within 7 days, say so. A raise on an ad set that stops tomorrow needs an end-date yes too, with the added spend shown.
4. Show one line per ad set: name, budget now, budget asked, 7-day spend, sales, cost per sale.
5. Ask the brand's raise rule. Default: raise only when cost per sale sits under the keep line after at least 4 sales, in steps of about 20%. Default cut: any ad set over the keep line after 4 more sales.
6. Prefer raising a winner's own ad set over copying the winner into a bigger one.
7. In Ads Manager, open the Ad sets tab and filter to the named ad sets only. Check the row name before typing, because a mis-click on the biggest ad set costs the most. Click the budget cell, type the agreed figure and use that cell's own Publish.
8. For an end date, open the ad set, change only Schedule, End, and publish that ad set alone.
9. Never use the global Review and publish. It bundles every draft in the account.
10. If the inline editor shows someone else's pending draft on that ad set, stop and ask. Leave it alone.
11. Meta may offer to raise the budget further. Decline it every time.
12. Reload the page and read the budget cell again. Meta can round a budget up on publish, for example $10 to $15 or $100 to $134. If it moved, set it back to the agreed figure.
13. Call `ad_health_check` again the same way. It reads the budget and end date from Meta, so it is the final read-back, not the page.
14. Call `log_decision` with `kind=budget`, the old and new figure as `decision`, and `measure` set to cost per sale over the next 7 days.

Checks before answering:
- Every new figure was named in chat by the person, per ad set. A raise with no number is not done.
- Spend check: the new daily total across the changed ad sets is stated next to the old total. Never above what was approved.
- The read-back budget equals the agreed figure on every ad set. If not, say so plainly.
- The person sometimes changes budgets too. Re-read right before reporting.
- Safe test, when asked for one: change a paused test ad set by $1 and back, then read both values.
- Use closed days. A Meta read error is a failure, not zero sales.

Output:
- One line first: how many ad sets changed and the new daily total against the old.
- One row per ad set: name, before, after, read back, 7-day cost per sale.
- Anything that differs from the plan, and any draft left untouched.
- Next look: tomorrow, check spend tracks the new level.

Never:
- Never change a budget the person did not name with a number.
- Never accept a Meta suggestion to raise a budget.
- Never touch another person's pending draft.
- Never share one campaign budget across pages with very different order sizes without saying the risk.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-budget-change". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
