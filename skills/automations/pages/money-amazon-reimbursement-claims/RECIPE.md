# Find money Amazon owes you

Channel: Money · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find money Amazon owes you" (id: money-amazon-reimbursement-claims, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks in four places where Amazon may have kept money it owes you: stock it lost or damaged in its warehouses, units missing from shipments it is still receiving, refunds where the item never came back, and take-backs larger than what it paid. Each possible case comes with case text ready to paste. Nothing is filed. A person checks each case and opens it. Our server can also run this once a month and email the list: ask us to add the addresses.

What to read: Amazon inventory ledger, reimbursements, settlements, customer returns and open inbound shipments
What to give me: A monthly list of possible cases, each with case text ready to paste. Nothing is filed for you.

Synthesis tools to use:
- `amazon_metric metric=money_owed_check limit=200`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=money_owed_check` and `limit=200`. It returns a `headline`, four pots, and for each pot its status, dollars, cases and the case text for each one.
2. If the owner wants a file, use `export_xlsx` with `filename=amazon-claims.xlsx`: one row per case, with the case text.

Checks before answering:
- Read each pot's `status`. `empty` means the check ran and found nothing. `could_not_check` means it could not run, and its dollars are blank, not zero. Say which pots could not be checked and why.
- Say plainly that the claim windows are estimates and not checked against Amazon. Tell the owner to check Amazon's current window before filing.
- Anything that already has a reimbursement or a case id is left out. Say so, so nobody files a case twice.
- Refunds younger than about 60 days are not judged yet, and refunds past about 120 days are dropped. Say how many fell each way.
- Take-backs are the least certain pot. A take-back may undo a payment from before the history held. Say that before its dollars.
- If one product is most of the refund dollars, say so. Amazon sometimes refunds without asking for the item back, and those refunds are not owed.
- Say what each value is based on: Amazon's own payout for that product, or the selling price where Amazon paid nothing.

Output:
- One line first: the candidate dollars this month, how many cases, and that nothing is filed.
- A short table: each of the four pots with its status, cases and dollars.
- The case text for each case, ready to paste, largest dollars first.
- If asked, an Excel file, amazon-claims.xlsx: pot, product, dates, units, value and its basis, case text.

Never:
- Never open a case in Seller Central or file anything. A person does that.
- Never guess a unit value. Use the value the check gives, or say it is missing.
- Never call a pot that could not be checked zero.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-amazon-reimbursement-claims". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
