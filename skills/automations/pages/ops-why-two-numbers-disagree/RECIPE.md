# Why don't these two revenue numbers match?

Channel: Data · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why don't these two revenue numbers match?" (id: ops-why-two-numbers-disagree, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
When the founder, a report and the books show different revenue for the same month, this walks from one to the other line by line. Most gaps are definitions: when a sale is counted, before or after discounts and fees, and which channels are included.

What to read: Amazon revenue on order basis, Amazon settled revenue, company revenue in the ledger, and the number someone quoted
What to give me: A walk from one revenue figure to the other, naming each difference in dollars

Synthesis tools to use:
- `net_revenue month=YYYY-MM`
- `gross_revenue month=YYYY-MM`
- `amazon_metric metric=pnl month=YYYY-MM`
- `total_net_revenue month=YYYY-MM`
- `monthly_pnl month=YYYY-MM`

Steps:
1. Ask which two figures disagree and where each came from.
2. Pull the candidates for the month: `net_revenue` (Amazon, when ordered, after promos), `gross_revenue` (before promos), `amazon_metric metric=pnl` (Amazon, when settled), `total_net_revenue` (Amazon plus website), `monthly_pnl` (whole company, from the books).
3. Match each quoted figure to one of these by value and definition.
4. Build the bridge: channels included, gross or net of promos, order date or settlement date, refunds, and cancelled orders.
5. Report any residual left after the named differences.

Checks before answering:
- A part month cannot be compared with a settled month. Check both are full.
- The books' Amazon revenue is net of Amazon's deductions. Do not compare it with gross Amazon sales.
- If the residual is more than 2% after the bridge, say the figures do not reconcile and stop guessing.

Output:
- Bridge table: Starting figure | Each difference with dollars | Ending figure | Residual.
- One line: which figure to use for which question.

Never:
- Never average two figures.
- Never call a definitional difference an error.
- Never change any report's definition.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-why-two-numbers-disagree". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
