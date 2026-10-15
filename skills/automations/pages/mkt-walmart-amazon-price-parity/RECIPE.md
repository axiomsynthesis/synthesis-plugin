# Same product, different price: fix it

Channel: Walmart · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Same product, different price: fix it" (id: mkt-walmart-amazon-price-parity, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Both marketplaces check prices elsewhere. A lower price on one can cost you the buy box or a listing on the other.
This lines up your prices on both and flags gaps.

What to read: Your live prices on walmart.com and on Amazon for the same products, from the daily shelf watch
What to give me: Products priced differently on Amazon and Walmart, which risks a pricing penalty, and the price to align on

Synthesis tools to use:
- `shelf_history marketplace=walmart days=14`
- `shelf_history marketplace=amazon days=14`
- `scrape_walmart k=10`

Steps:
1. Call `shelf_history marketplace=walmart days=14` and `shelf_history marketplace=amazon days=14` for your tracked items.
2. Match the same product on both by your own code or the person's mapping. Never by title.
3. For products not tracked on Walmart, call `scrape_walmart query=<product name> k=10` once each, up to five, and confirm the match with the person.
4. Flag gaps over 3%. Say which side is lower and the risk on the other side.

Checks before answering:
- Walmart prices can come from other sellers of your product. Check the seller before blaming your own price.
- Scraped data is third-party and dated. Label it. Scrapes use a shared monthly allowance.
- Shelf history only exists for items being tracked. Say which products are not tracked.

Output:
- One line: products with a gap and the biggest one.
- A table: product, Walmart price, Amazon price, gap, seller on Walmart, suggested price.

Never:
- Never change prices on either marketplace.
- Never match products by title alone.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-amazon-price-parity". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
