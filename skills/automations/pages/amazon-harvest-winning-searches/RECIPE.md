# Turn winning searches into keywords

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn winning searches into keywords" (id: amazon-harvest-winning-searches, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the search terms that already make sales through broad or phrase match but have no exact keyword of their own. It builds a bulk file that moves them into exact campaigns with a starting bid, so you stop renting traffic you already own.

What to read: Search term report
What to give me: Searches already selling through broad match, moved into their own exact keywords in an upload file

Synthesis tools to use:
- `amazon_metric metric=ppc_match_type_coverage`
- `amazon_metric metric=ppc_search_terms`
- `amazon_metric metric=ppc_keyword_bids`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=ppc_match_type_coverage`, `days=60`, `min_orders=6` and `limit=50` for proven terms with no exact keyword.
2. Call `amazon_metric` with `metric=ppc_search_terms`, `days=60` and `min_clicks=20` for each term's clicks, cost per click, sales and return.
3. Call `amazon_metric` with `metric=ppc_keyword_bids` and `days=30` for your current bids on the same products.
4. Set a starting exact bid from each term's cost per click and your target return.
5. Call `export_xlsx` with `filename=harvest_exact_keywords.xlsx`: one sheet in Amazon bulk upload shape, one sheet with the reasons.

Checks before answering:
- Use settled days. Ad sales take a few days to attribute.
- A term needs enough orders to be real. Do not harvest on two or three sales.
- If a term is already exact somewhere, leave it out.
- If the search term read is empty, say it could not be read. Never ship an empty file as "nothing to harvest".

Output:
- One line first: how many terms to move and the sales they made in the last 60 days.
- A file named `harvest_exact_keywords.xlsx`: campaign, ad group, keyword, match type exact, starting bid, plus a reasons sheet.
- A person reviews it and uploads it in Amazon Ads bulk operations.

Never:
- Never upload the file or change a campaign. A person does that.
- Never set a bid without showing where it came from.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-harvest-winning-searches". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
