# Stop paying for searches that never sell

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stop paying for searches that never sell" (id: amazon-cut-wasted-ad-searches, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds ad search terms that spend and never sell over 30 days.
It protects your brand searches and your best product searches.
It builds Amazon's bulk upload file with each negative at the right level, and a person uploads it in the ad console.
This is the safest first change because it can only lower spend.

What to read: Amazon Ads search term report, your break-even ad cost
What to give me: A ready-to-upload list of searches to block, with the money they burn, plus a list to check first

Synthesis tools to use:
- `amazon_metric metric=ppc_search_terms`
- `amazon_metric metric=ppc_branded_split`
- `breakeven_roas`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=ppc_search_terms`, `days=30` and `limit=500` to get spend, clicks and sales by search term and campaign.
2. Call `breakeven_roas` with each main product's `asin` to know how much a term may spend before it loses money.
3. Call `amazon_metric` with `metric=ppc_branded_split` and `days=30` to find brand searches, and remove them from the list.
4. Keep terms with no sales and spend above one break-even sale. Use negative exact for one exact phrase, and negative phrase when a word never sells.
5. Call `export_xlsx` with `filename=negatives_bulk.xlsx`: one sheet in Amazon's bulk format, one sheet listing term, campaign, spend, clicks and reason.

Checks before answering:
- If the search term report is empty, say it could not be read. Never say "nothing wasted".
- A term needs enough clicks to judge. Skip terms under about 10 clicks and say how many were skipped.
- Sales can land days after a click. Leave out the last 7 days of spend when judging.

Output:
- One line answer first: how many terms and how much spend a month they waste.
- A table: search term, campaign, spend, sales, action.
- The file negatives_bulk.xlsx. A person checks the list and uploads it in the Amazon ad console.

Never:
- Nothing goes live in any account. A person uploads the file.
- Never negate a brand search or a search that sold in the last 90 days.
- Never guess a break-even number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-cut-wasted-ad-searches". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
