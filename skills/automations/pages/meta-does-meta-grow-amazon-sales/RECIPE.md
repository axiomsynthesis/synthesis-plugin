# Does Meta grow your Amazon sales?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does Meta grow your Amazon sales?" (id: meta-does-meta-grow-amazon-sales, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers whether your Meta spend lifts Amazon sales, even though Meta cannot see Amazon orders. It lines up Meta spend with searches for your brand on Amazon and with Amazon sales. Then it gives a rough range for the lift in sales and in profit, says plainly how sure we are, and designs the state test that would settle it. Only that test gives a firm number.

What to read: Meta spend, Amazon branded search, attribution, Amazon sales by state and Amazon margin per product
What to give me: A rough range for Amazon profit per $1K on Meta, and the state test that settles it

Synthesis tools to use:
- `cost_rules for=meta-does-meta-grow-amazon-sales`
- `meta_metric metric=weekly_trend`
- `amazon_metric metric=search_query_trend`
- `amazon_metric metric=attribution_sources`
- `amazon_metric metric=offamazon_share`
- `amazon_metric metric=daily_revenue`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=geo_penetration months=3 limit=51`

Steps:
1. Call `meta_metric` with `metric=weekly_trend` and `weeks=26` for weekly Meta spend.
2. Call `amazon_metric` with `metric=search_query_trend`, `grain=week` and `periods=26`, with no keyword. Read `branded_series.query_volume` for weekly branded searches. Read every page of the result. A keyword returns one row per search with no weekly branded total.
3. Call `amazon_metric` with `metric=daily_revenue` and `days=180`, rolled up to weeks, for Amazon sales.
4. Call `amazon_metric` with `metric=attribution_sources` and `days=90` for sales Amazon tracked back to Meta links.
5. Call `amazon_metric` with `metric=offamazon_share` and `days=90` for how much of Amazon is driven from outside Amazon.
6. Compare weeks of high and low Meta spend, with a one to two week lag, and work out a low and a high figure for sales added per $1K.
7. Call `amazon_metric metric=contribution_by_asin months=3` for the margin of the products the ads point to. Turn added sales into added profit. A lift that earns less profit than the $1K it cost is a loss, even if it is positive.
8. Propose a state holdout. Call `amazon_metric metric=geo_penetration months=3 limit=51`. Pick about 20% of states matched on Amazon sales and customers. Switch Meta off there for 4 to 6 weeks, then compare Amazon sales by state against the rest.

Checks before answering:
- Deal weeks and holidays move both lines at once. Take them out before comparing.
- Fewer than about 12 weeks of spend changes is too little. Say low confidence.
- Tracked Meta links undercount the lift. Never treat them as the whole answer.
- If any series is empty, say which one. Never treat a failed read as no lift.
- Amazon sales credited to Meta links can include creator and agency links that share the same publisher. Say when one week's credited sales are far above what its Meta spend could buy, and leave it out.
- There is no model here with controls or a confidence range. The range from step 6 is a by-eye read. Always say low confidence until the state test runs.
- If a product has no cost entered, its margin is blank. Give the lift in sales only for it and say why.

Output:
- One line first: whether to keep, cut or test Meta spend aimed at Amazon, with the range of Amazon profit added per $1K and the confidence.
- A short table: week, Meta spend, branded searches, Amazon sales.
- The state test: which states go dark, for how long, and what result would mean keep or cut.

Never:
- Never change a Meta budget or campaign. A person does that.
- Never state the lift as proven without a test.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-does-meta-grow-amazon-sales". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
