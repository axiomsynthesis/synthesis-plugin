---
description: "Does Meta grow your Amazon sales?: Amazon sales added per $1K on Meta, how sure we are, and the test that would settle it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Does Meta grow your Amazon sales?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does Meta grow your Amazon sales?" (id: meta-does-meta-grow-amazon-sales, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers whether your Meta spend lifts Amazon sales, even though Meta cannot see Amazon orders. It lines up Meta spend with searches for your brand on Amazon and with Amazon sales. Then it gives a dollar lift and says plainly how sure we are.

What to read: Meta spend, Amazon branded search, attribution
What to give me: Amazon sales added per $1K on Meta, how sure we are, and the test that would settle it

Synthesis tools to use:
- `meta_metric metric=weekly_trend`
- `amazon_metric metric=search_query_trend`
- `amazon_metric metric=attribution_sources`
- `amazon_metric metric=offamazon_share`
- `amazon_metric metric=daily_revenue`

Steps:
1. Call `meta_metric` with `metric=weekly_trend` and `weeks=26` for weekly Meta spend.
2. Call `amazon_metric` with `metric=search_query_trend`, `grain=week` and `periods=26`, with no keyword. Read `branded_series.query_volume` for weekly branded searches. Read every page of the result. A keyword returns one row per search with no weekly branded total.
3. Call `amazon_metric` with `metric=daily_revenue` and `days=180`, rolled up to weeks, for Amazon sales.
4. Call `amazon_metric` with `metric=attribution_sources` and `days=90` for sales Amazon tracked back to Meta links.
5. Call `amazon_metric` with `metric=offamazon_share` and `days=90` for how much of Amazon is driven from outside Amazon.
6. Compare weeks of high and low Meta spend, with a one to two week lag, and work out sales added per $1K.

Checks before answering:
- Deal weeks and holidays move both lines at once. Take them out before comparing.
- Fewer than about 12 weeks of spend changes is too little. Say low confidence.
- Tracked Meta links undercount the lift. Never treat them as the whole answer.
- If any series is empty, say which one. Never treat a failed read as no lift.

Output:
- One line first: Amazon sales added per $1K on Meta, and high, medium or low confidence.
- A short table: week, Meta spend, branded searches, Amazon sales.
- One move: usually a clean on and off test to firm up the number, and how we will know.

Never:
- Never change a Meta budget or campaign. A person does that.
- Never state the lift as proven without a test.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-does-meta-grow-amazon-sales". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
