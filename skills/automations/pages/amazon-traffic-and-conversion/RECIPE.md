# Visits and conversion, product by product

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Visits and conversion, product by product" (id: amazon-traffic-and-conversion, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows sessions, page views and conversion by product for the last 4 weeks, and what changed.
It flags products where traffic rose but orders did not.
It separates a real change from Amazon's reporting lag.

What to read: Amazon sales and traffic report
What to give me: Visits and conversion for every product over four weeks, what changed, and three things to watch

Synthesis tools to use:
- `amazon_metric metric=conversion`
- `amazon_metric metric=conversion_funnel`
- `amazon_metric metric=listing_details`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=conversion` to get sessions, page views and conversion by product for the latest month, then again with `month=` set to the month before. This read is monthly only.
2. Call `amazon_metric` with `metric=conversion_funnel` and `days=56` to see where shoppers drop off for the products that moved most.
3. For any product whose conversion fell, call `amazon_metric` with `metric=listing_details` and its `asin` to check price, rating and buy box.
4. Use `find_product` to name each product the way the brand does, and rank the products by sessions.

Checks before answering:
- Amazon's traffic report lands a few days late. Leave out the newest days if they look short, and say so.
- If the traffic read is empty, say the report could not be read. Never show zero sessions as real.
- A conversion change on a product with few sessions is noise. Say when the sample is too small.

Output:
- A table: product, sessions, page views, conversion, change in points against the prior 4 weeks.
- Three things to watch, one line each, with the likely reason.
- Under 20 lines.

Never:
- Never edit a listing or a price. A person does that.
- Never guess sessions or conversion the tools did not return.
- Never call a one-week dip a trend.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-traffic-and-conversion". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
