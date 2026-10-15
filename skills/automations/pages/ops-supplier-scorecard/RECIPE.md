# Score your suppliers

Channel: Inventory · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Score your suppliers" (id: ops-supplier-scorecard, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Scores each supplier the same way every quarter so rankings are repeatable, and puts spend beside the score so dependence on one supplier is visible. The tool makes a judgement repeatable; the ratings still come from people.

What to read: Supplier spend from the ledger and your ratings of each supplier's quality, delivery, price, flexibility and relationship
What to give me: A ranked scorecard with a tier for each supplier, the spend behind it, and where you depend on just one

Synthesis tools to use:
- `netsuite_metric metric=vendor_spend limit=25`
- `tier_suppliers suppliers=[...]`
- `score_supplier quality=<0-10> delivery=<0-10> price=<0-10>`
- `export_xlsx filename=supplier-scorecard.xlsx`

Steps:
1. Call `netsuite_metric metric=vendor_spend limit=25` for spend per supplier. Use bill rows, not the open-balance field.
2. Ask the person to rate each product supplier 0 to 10 on quality, delivery, price, flexibility and relationship, with one line of evidence per rating (late shipments, defect rate, quotes).
3. Run `tier_suppliers suppliers=[{name, quality, delivery, price, flexibility, relationship}]`.
4. For any supplier near a tier line, run `score_supplier` alone to see the components.
5. Compute each supplier's share of product spend.
6. Write it with `export_xlsx filename=supplier-scorecard.xlsx`.

Checks before answering:
- A rating left out becomes 0 for quality, delivery or price and 5 for the others. Never let a blank stand. Mark the supplier unscored.
- Only compare suppliers rated by the same person in the same week.
- The open-balance field is a payable, and its top line can be a tax agency. Use spend.
- If the ledger is not connected, rank without spend and say so.

Output:
- Spreadsheet: Supplier | Spend last 12 months | Share | Five ratings with evidence | Score | Tier.
- Two lines in chat: the biggest dependence risk and the one action to reduce it.

Never:
- Never contact or rate a supplier on the person's behalf.
- Never present a tier as measured. It is a structured opinion.
- Never move volume between suppliers.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-supplier-scorecard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
