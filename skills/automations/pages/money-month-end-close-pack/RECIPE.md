# Close the month faster

Channel: Money · Level: On a schedule · Status: Ready after we build it
Schedule: monthly, on the 5th at 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Close the month faster" (id: money-month-end-close-pack, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Once a month, ties Amazon payouts, website sales and the books for the month just closed. It hands back a tie-out sheet and a short list of gaps for your bookkeeper.

What to read: Settlements, Shopify payouts, NetSuite
What to give me: Amazon payouts, website sales and the books tied out for the month, with a short list of gaps

Synthesis tools to use:
- `cost_rules for=money-month-end-close-pack`
- `amazon_metric metric=daily_settled_revenue`
- `amazon_metric metric=fee_breakdown`
- `shopify_metric metric=monthly_revenue`
- `monthly_pnl`
- `netsuite_metric metric=gross_to_net_bridge`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=daily_settled_revenue` and `days=45` for what Amazon paid out in the closed month.
2. Call `amazon_metric` with `metric=fee_breakdown` and that `month` for fees taken before payout.
3. Call `shopify_metric` with `metric=monthly_revenue` and `months=2` for website sales.
4. Call `monthly_pnl` with that `month`, and `netsuite_metric` with `metric=gross_to_net_bridge` and `months=2`, for what the books show.
5. Line each source up against the books and use `export_xlsx` with `filename=close-pack.xlsx`.

Checks before answering:
- Only close a month once Amazon's settlement for it has landed. A month still settling shows a false gap.
- If any source fails to read, the pack says so at the top. Never show a source as $0.
- Show both numbers for every gap, not only the difference.

Output:
- One line first: how far off the books are, in dollars and percent.
- An Excel file, close-pack.xlsx: source, amount from source, amount in books, gap, note. A second tab lists unmatched payouts.

Never:
- Never post an entry to NetSuite. Your bookkeeper does that.
- Never force a tie by guessing a missing payout.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-month-end-close-pack". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (monthly, on the 5th at 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. The data is connected for brands with NetSuite, but the pack layout and a Shopify payouts read still need building. Do the parts you can and say plainly what is missing.
