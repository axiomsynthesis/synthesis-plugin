# Do your books match Amazon's stock count?

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Do your books match Amazon's stock count?" (id: ops-book-stock-vs-amazon-stock, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares the stock your books think is at Amazon with what Amazon actually counts. A gap means either the books carry stock that is gone, which overstates assets and margin, or Amazon lost units it should pay for.

What to read: Units at the Amazon location in the accounting ledger and Amazon's own stock counts per product
What to give me: Products where your books and Amazon disagree on units, with the dollar value of the gap

Synthesis tools to use:
- `netsuite_metric metric=inventory_position limit=100`
- `amazon_metric metric=inventory_position limit=100`
- `amazon_metric metric=reimbursements`

Steps:
1. Call `netsuite_metric metric=inventory_position limit=100` and keep the Amazon locations per product.
2. Call `amazon_metric metric=inventory_position limit=100` for Amazon's nine stock buckets per product.
3. Compare Amazon's `total` (the first eight buckets) with book units per product. Show units being researched beside it: Amazon keeps them outside its total.
4. Value each gap at cost per unit.
5. Call `amazon_metric metric=reimbursements` to see whether Amazon already paid for lost or damaged units on the gap products.
6. Flag gaps above 2% of units and above $1,000.

Checks before answering:
- The stock metric already counts each physical pile once across listings and checks it adds up to Amazon's total. Use its numbers as returned; never add listings together again.
- Units sold and waiting to ship, and inbound not yet shipped, may already be off the books or still at your warehouse in the ledger, depending on how the books record them. Check those two buckets before calling a gap.
- A product the answer left out because its numbers did not add up is unknown, not zero. Name it.
- The two counts are from different times. Shipments in flight between them explain small gaps.
- If the ledger is not connected, say so and stop.

Output:
- Table: Product | Book units at Amazon | Amazon units | Gap | Gap value | Reimbursed already.
- Two lines: the total gap value and the next step for the largest one.

Never:
- Never adjust the books or file a claim.
- Never treat a failed Amazon read as zero units.
- Never net gaps across products.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-book-stock-vs-amazon-stock". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
