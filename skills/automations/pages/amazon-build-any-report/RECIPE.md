# Build any Amazon report you need

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build any Amazon report you need" (id: amazon-build-any-report, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
You ask for the Amazon report you need and get a finished file.
It pulls the numbers, checks they add up, and saves a spreadsheet or an HTML page you can send.

What to read: All Amazon data
What to give me: A finished spreadsheet or HTML report, numbers checked to add up, ready to send

Synthesis tools to use:
- `amazon_metric metric=contribution_by_asin`
- `amazon_metric metric=fee_breakdown`
- `amazon_metric metric=return_reasons`
- `find_product`
- `export_xlsx`

Steps:
1. Ask what the report is for, which products and which dates, if the request does not say.
2. Pick the right `amazon_metric` reads for the ask. For example `metric=contribution_by_asin` with `months` for profit by product and month, `metric=fee_breakdown` for fees, `metric=return_reasons` with `months=3` for returns.
3. Use `find_product` to name products the way the brand does and group pack sizes.
4. Check that product rows add up to the total the tools report, and note any gap.
5. Call `export_xlsx` with a plain `filename` like `amazon_fees_q3.xlsx`, or, if the person wants a page, write an HTML page. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- Use settled months for money. Say when a month is still settling.
- If a read is empty or fails, say which part is missing. Never fill it with zeros.
- A total that does not match the product rows is called out, with both numbers.

Output:
- One line answer first: the headline the report shows.
- The file, with one sheet per table and a notes sheet listing the dates covered and anything missing.

Never:
- Never change anything in Seller Central.
- Never guess a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-build-any-report". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
