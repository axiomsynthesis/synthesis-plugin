# What's wrong on Amazon right now?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What's wrong on Amazon right now?" (id: amazon-diagnose-whats-wrong, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds why Amazon sales, conversion or rank moved, and names the one fix.
It compares the latest closed week with the brand's own last 8 weeks.
It checks stock, buy box and price first, because they explain most drops.
Each possible cause gets a dollar size, and the answer ends with one move and the number that proves it worked.

What to read: Amazon orders, sessions, conversion, ads, stock, buy box, search share
What to give me: A short diagnosis in plain English, what the problem costs, and the one move to make

Synthesis tools to use:
- `amazon_metric metric=daily_revenue`
- `amazon_metric metric=inventory_position`
- `amazon_metric metric=buybox_health`
- `amazon_metric metric=conversion`
- `amazon_metric metric=ppc_week_over_week`
- `amazon_metric metric=search_query_trend`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=daily_revenue` and `days=63` to get the last 9 weeks of sales and find which products drove the change.
2. Call `amazon_metric` with `metric=inventory_position`, then `metric=buybox_health` with `days=63`, to see if any of those products ran out of stock or lost the buy box.
3. Call `amazon_metric` with `metric=conversion` for the latest month, then again with `month=` set to the month before, to split the change into fewer visits or fewer visits turning into orders, by product.
4. Call `amazon_metric` with `metric=ppc_week_over_week`, then `metric=search_query_trend` with `grain=week` and `periods=9`, to check ad spend changes and lost search share.
5. Use `find_product` to name each product the way the brand does, then size every cause in dollars and rank them.

Checks before answering:
- Use closed days only. Today's orders are still coming in and make any week look worse.
- If a tool returns nothing or an error, say that part could not be read. Never call it "no problem found".
- One bad week on one product is not a trend. Say so when the drop is inside the brand's normal week-to-week swing.
- The causes should add up to roughly the total drop. If they do not, say how much is still unexplained.

Output:
- One line answer first: how much sales moved and the main cause.
- A table: cause, product, lost or gained sales in dollars.
- One move, and the number to watch that shows it worked, with a date.
- Under 15 lines in total.

Never:
- Never change anything in Seller Central or the ad console. A person does that.
- Never guess a number the tools did not return.
- Never blame ads or price before stock and buy box have been checked.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-diagnose-whats-wrong". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
