# Why products come back

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why products come back" (id: inventory-returns-reasons-digest, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Groups why people send products back, ties it to what reviews say, and names the fix for the top reason.

What to read: Amazon returns, reviews
What to give me: The top return reasons by product, what they cost a month, and the fix for the biggest one

Synthesis tools to use:
- `amazon_metric metric=return_reasons`
- `amazon_metric metric=review_voice`
- `amazon_metric metric=rating_watch`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=return_reasons` and `months=3` for return counts and reasons by product.
2. Call `amazon_metric` with `metric=review_voice` and `sentiment=negative` for what buyers complain about in reviews. It has no date setting, so say the dates the reviews cover.
3. Call `amazon_metric` with `metric=rating_watch` to see whether star ratings are slipping.
4. Name each product with `find_product`, group reasons, and match each top reason to a fix.

Checks before answering:
- A product with fewer than 20 returns is not a pattern. Say so.
- If the returns read is empty or fails, say so. Never call it "no returns".
- Recent weeks are still filling in. Returns arrive weeks after the sale.

Output:
- One line first: the top reason and what it costs a month.
- A table: product, returns, return rate, top reason, share, suggested fix.

Never:
- Never change a listing or a product. A person does that.
- Never guess a reason the data does not show.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-returns-reasons-digest". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
