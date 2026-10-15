# What customers write in about

Channel: Support · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What customers write in about" (id: support-ticket-themes, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what customers write in about, ranked by how often. For each top theme it gives the count, the trend and a fix in the product, the site or the emails, so fewer people need to write in at all.

What to read: Gorgias tickets
What to give me: The top ticket themes with counts, trends and the fix that removes the most tickets

Synthesis tools to use:
- `gorgias_metric metric=contact_reasons`
- `gorgias_metric metric=topic_trends`
- `gorgias_metric metric=ticket_volume`
- `gorgias_metric metric=customer_cx`

Steps:
1. Call `gorgias_metric` with `metric=contact_reasons` and `months=3` for why customers contact you, by category.
2. Call `gorgias_metric` with `metric=topic_trends` and `months=6` for topics that are rising.
3. Call `gorgias_metric` with `metric=ticket_volume` and `months=6` for the total and the trend.
4. Call `gorgias_metric` with `metric=customer_cx` for how each theme is resolved and how fast. This read has no date setting, so say the dates the result covers.
5. For each top theme, name one fix that would remove the reason to write in.

Checks before answering:
- Topic reads cover only tickets with a clear subject. Say what share of tickets that is.
- If ticket volume is empty, say Gorgias could not be read. Never say "no tickets".
- A theme that rose in one month is not yet a trend. Say so.

Output:
- One line first: the top theme and its share of tickets.
- A table: theme, tickets, share, trend, example subject line, fix.
- One move: the fix that removes the most tickets, and how we will know.

Never:
- Never reply to or close a ticket. A person does that.
- Never quote a customer's name, email or order number.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: support-ticket-themes". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
