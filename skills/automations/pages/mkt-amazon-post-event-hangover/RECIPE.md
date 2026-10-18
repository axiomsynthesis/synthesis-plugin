# Did the sale event leave a hangover?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did the sale event leave a hangover?" (id: mkt-amazon-post-event-hangover, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A big sale event often borrows from the weeks after. This measures the dip after the event and nets it against the spike.

What to read: Daily sales and units for the four weeks before, during and after a big sale event, plus new customers won during it
What to give me: Whether the event pulled future sales forward, left a lasting lift, or neither, net of the dip afterwards

Synthesis tools to use:
- `cost_rules for=mkt-amazon-post-event-hangover`
- `amazon_metric metric=daily_revenue`
- `amazon_metric metric=velocity_momentum weeks=12 limit=30`
- `amazon_metric metric=pnl_by_customer_type days=60`

Steps:
1. Ask for the event dates. Call `amazon_metric metric=daily_revenue` from 4 weeks before to 4 weeks after, with the brand's local time zone.
2. Baseline = average daily sales over the 4 weeks before, excluding any other promo days.
3. Event gain = event sales minus baseline days. Dip = baseline minus each day after, summed until sales return to baseline.
4. Call `amazon_metric metric=velocity_momentum weeks=12 limit=30` to split by product.
5. Call `amazon_metric metric=pnl_by_customer_type days=60` to see how many event buyers were new.

Checks before answering:
- Use local days. The default is UTC, which shifts an event day by several hours.
- Wait until at least 3 weeks after the event before calling the dip finished.
- Season moves the baseline. If the event sits in a seasonal climb, say so.

Output:
- Three lines: event gain, dip after, net.
- A table: product, event gain, dip after, net, held higher after yes or no.

Never:
- Never call the spike the result without netting the dip.
- Never compare against a baseline that contains another promotion.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-post-event-hangover". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
