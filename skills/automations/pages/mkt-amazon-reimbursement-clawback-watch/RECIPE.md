# Reimbursements Amazon took back

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Reimbursements Amazon took back" (id: mkt-amazon-reimbursement-clawback-watch, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon pays reimbursements and then often takes them back. The gross figure can overstate what you really recovered several times over.
This shows the net, by reason and product, and flags take-backs that look wrong.

What to read: What Amazon paid back for lost, damaged and returned stock over the last 90 days, and what it reversed
What to give me: What you really kept after Amazon's take-backs, by reason and product, and where take-backs run high

Synthesis tools to use:
- `cost_rules for=mkt-amazon-reimbursement-clawback-watch`
- `amazon_metric metric=reimbursements limit=40`
- `amazon_metric metric=return_reasons months=3`

Steps:
1. Call `amazon_metric metric=reimbursements limit=40`. Read gross credits, reversals and net, by reason and product.
2. Flag products where reversals exceed 70% of credits, and "found" reversals on products whose stock did not rise.
3. Call `amazon_metric metric=return_reasons months=3` to check whether customer-return reversals match real returns.

Checks before answering:
- This is what Amazon paid, not what it owes. Never call any figure here a recoverable balance.
- The report covers a rolling 90 days only.
- Always lead with the net figure, never the gross.

Output:
- Three lines: gross credited, reversed, net recovered.
- A table: reason, credited, reversed, net.
- A short list of products with suspect reversals.

Never:
- Never file claims or cases.
- Never present gross credits as money recovered.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-reimbursement-clawback-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
