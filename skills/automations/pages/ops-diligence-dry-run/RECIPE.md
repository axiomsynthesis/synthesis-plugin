# Pass a buyer's diligence before they look

Channel: Money · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Pass a buyer's diligence before they look" (id: ops-diligence-dry-run, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs the checks a buyer's accountants run in a quality of earnings review, before they do. It ties revenue across sources, finds one-off items that flatter profit, and lists what cannot be tested. Finding these first is cheaper than explaining them in a negotiation.

What to read: Revenue from every source, closed-book profit, one-off items, refunds, stock and customer concentration
What to give me: The checks a buyer's accountants will run, each passed, failed or not testable, before they find them

Synthesis tools to use:
- `cost_rules for=ops-diligence-dry-run`
- `net_revenue month=YYYY-MM`
- `amazon_metric metric=pnl month=YYYY-MM`
- `monthly_pnl month=YYYY-MM`
- `netsuite_metric metric=gross_to_net_bridge months=12`
- `netsuite_metric metric=adjusted_ebitda months=12`
- `export_xlsx filename=diligence-dry-run.xlsx`

Steps:
1. For each of the last 12 months, compare Amazon revenue three ways: when ordered (`net_revenue`), when settled (`amazon_metric metric=pnl`), and as booked (`monthly_pnl` and the Amazon account in invoiced revenue).
2. Call `netsuite_metric metric=gross_to_net_bridge months=12` for discount and refund dollars by month.
3. Call `netsuite_metric metric=adjusted_ebitda months=12` and list any month with a one-off item over $25,000 (tariff refunds, write-offs, inventory credits).
4. List which months have closed books.
5. Record each test as PASS, FAIL (with dollars) or NOT TESTABLE (with where the answer lives).
6. Write it with `export_xlsx filename=diligence-dry-run.xlsx`: Tests, Revenue tie-out, One-off items, Closed months.

Checks before answering:
- Amazon revenue in the books is net of Amazon's deductions. Compare like with like or the tie-out fails for the wrong reason.
- One-off items that post back into closed months change those months. Re-pull before quoting.
- Adjusted EBITDA equals reported EBITDA when no add-backs are booked.
- No balance sheet is held. Balance tests are NOT TESTABLE here.

Output:
- Spreadsheet with the four tabs above.
- In chat: pass count, the three most expensive fails, and who fixes each.

Never:
- Never adjust the books.
- Never call a definitional difference a failure without trying the like-for-like version.
- Never share the file with anyone outside.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-diligence-dry-run". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
