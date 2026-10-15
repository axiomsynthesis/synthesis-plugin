# Draft a new product listing

Channel: Amazon · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Draft a new product listing" (id: amazon-draft-new-product-listing, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes everything Amazon needs to list a new product.
It asks for the product facts you have, writes in your brand voice, and fills Amazon's category template.
A person uploads it. Nothing goes live on its own.

What to read: Your product facts, rival listings, category searches
What to give me: Title, bullets, description, keywords and the category file, ready to upload

Synthesis tools to use:
- `brand_facts`
- `scrape_amazon_search`
- `scrape_amazon_product`
- `export_xlsx`

Steps:
1. Ask the person for the product facts: name, size, price, what it does, barcode, case size and weight.
2. Call `brand_facts` with `query` set to the product type to pull the claims and proof points the brand already uses.
3. Call `scrape_amazon_search` with the main category search and `k=10` to see the top rivals and their prices.
4. Call `scrape_amazon_product` on the two or three closest rivals to read how they word their titles and bullets.
5. Write the title, bullets, description and backend terms, then call `export_xlsx` with `filename=new_listing.xlsx`, listing every template field and marking the ones that need the person.

Checks before answering:
- Every field the person did not give is marked "needs you". Never fill a barcode, weight or size with a guess.
- Count characters against Amazon's limits.
- Every claim must come from the brand's own facts.

Output:
- The listing copy: title, five bullets, description, backend terms.
- The file new_listing.xlsx, with a count of filled and missing fields. A person uploads it in Seller Central.

Never:
- Nothing goes live in any account. A person uploads the file.
- Never invent a product fact, barcode or measurement.
- Never copy a rival's wording.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-draft-new-product-listing". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The writing is ready. Filling Amazon's category template still needs to be built. Do the parts you can and say plainly what is missing.
