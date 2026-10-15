# Who owes us money?

Channel: Money · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who owes us money?" (id: ops-receivables-chase-list, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns receivables into a short list someone can act on: which account owes what, how late, and a polite reminder ready to send. For brands selling to retailers and distributors, late payment is often the biggest swing in cash.

What to read: Open invoices and payments by retail and wholesale account
What to give me: Overdue invoices by account and age, with a reminder drafted for each

Synthesis tools to use:
- `netsuite_metric metric=ar_aging top_n=20`
- `netsuite_metric metric=customer_trend months=6 top=20`
- `export_docx`

Steps:
1. Call `netsuite_metric metric=ar_aging top_n=20` for balances by account and age bucket.
2. Call `netsuite_metric metric=customer_trend months=6 top=20` to see each account's recent buying, so a big buyer paying slowly is weighed differently from a lapsed one.
3. Once invoice-level balances land, list each invoice past terms with number, date, amount and days late.
4. Draft one short reminder per account with `export_docx`, naming invoices and amounts.

Checks before answering:
- Until the build lands, report only which accounts carry balances, never the dollar amounts, and say why.
- An empty current bucket on every account is the known matching problem, not a sign everyone is late.
- The customer list includes the brand's own storefronts. Leave them out.
- Payment terms differ per account. Ask for them; do not assume 30 days.

Output:
- Table: Account | Invoice | Amount | Days past terms | Recent buying.
- A Word file with one reminder per account, for a person to review and send.

Never:
- Never send a reminder. A person sends it.
- Never quote a receivables total from the current snapshot.
- Never threaten a hold or penalty in a draft.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-receivables-chase-list". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The receivables snapshot does not match payments to invoices, so every account shows an empty current bucket and the dollar balances are not reliable. Needs invoice-level open balances with payments applied before any amount can be quoted. Do the parts you can and say plainly what is missing.
