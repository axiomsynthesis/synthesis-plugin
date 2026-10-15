# When can you judge a new campaign?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "When can you judge a new campaign?" (id: mkt-amazon-when-to-judge-a-campaign, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
People kill new campaigns too early because sales are still landing. This measures your own account's lag and gives a judging date.

What to read: How many days your ad sales take to land after a click, measured on your own account
What to give me: The earliest fair date to judge a new campaign or bid change, and how much last week's numbers will still grow

Synthesis tools to use:
- `amazon_metric metric=ppc_purchase_latency days=90 limit=20`
- `amazon_metric metric=ppc_campaigns days=14 limit=20`

Steps:
1. Call `amazon_metric metric=ppc_purchase_latency days=90 limit=20`. Read the share landed at 1, 7, 14 and 30 days.
2. For the campaign the person names, call `amazon_metric metric=ppc_campaigns days=14 limit=20` to get its launch date and results so far.
3. Gross up its sales so far using the lag curve. Give the earliest date by which 95% will have landed.

Checks before answering:
- The lag is Sponsored Products only. Say Sponsored Brands and Display may differ.
- Products bought on a long think cycle lag more. If the product is expensive, use its own row, not the account average.

Output:
- Three lines: lag at 7 and 14 days, the campaign's grossed-up result so far, and the judging date.

Never:
- Never call a campaign a failure before its judging date.
- Never change anything in the account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-when-to-judge-a-campaign". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
