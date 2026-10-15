# Tell me when a new ad starts winning on Amazon

Channel: Meta · Level: On a schedule · Status: Ready now
Schedule: every Tuesday, from our server

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Tell me when a new ad starts winning on Amazon" (id: meta-new-winning-ad-alert, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every Tuesday, looks at last week's ads that first ran in the past few weeks. Any that already earn more on Amazon per dollar than your account as a whole, with enough spend and orders to mean something, are emailed to you while there is still time to give them more budget.

What to read: Last week's Meta spend and Amazon Attribution sales for every Meta ad that sends shoppers to Amazon
What to give me: An email on Tuesday when a new ad is already selling better on Amazon than your account, with its return, spend and orders

Synthesis tools to use:
- `meta_metric metric=ad_performance limit=50`

Steps:
1. Call `meta_metric metric=ad_performance limit=50` for last week's spend, clicks and first-run dates per ad.
2. Keep ads whose creative first ran in the last 21 days, with real spend, Amazon clicks and Amazon orders.
3. Compare each one's Amazon return with the account's return for the same week.

Checks before answering:
- Use closed weeks only. Amazon keeps crediting orders for 14 days after a click, so say last week is still settling.
- A copy of an older ad is not new. Judge the creative, not the copy.
- If there are no Amazon sales to compare, say so and stop. Never call an ad a winner on Meta's own numbers.

Output:
- One line first: how many new ads are winning, and the best one with its return.
- Each winner with its return, spend, Amazon orders and a link to watch it.

Never:
- Never change a budget, pause or launch an ad. A person decides.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-new-winning-ad-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This one runs on the Synthesis server (every Tuesday, from our server). Do not set up a repeat yourself; read the latest copy instead.
