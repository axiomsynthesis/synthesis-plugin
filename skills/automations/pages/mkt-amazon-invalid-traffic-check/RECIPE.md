# Spot bot clicks eating your ad budget

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Spot bot clicks eating your ad budget" (id: mkt-amazon-invalid-traffic-check, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon removes bot and duplicate clicks before it bills you. A campaign with a high filtered share is buying in a low-quality auction.
This flags those campaigns so you can check whether the clicks you do pay for are any good.

What to read: Amazon's own count of filtered bot and duplicate impressions and clicks per campaign
What to give me: Campaigns whose traffic looks unusually low quality next to the rest of the account

Synthesis tools to use:
- `amazon_metric metric=ppc_invalid_traffic days=30 limit=30`
- `amazon_metric metric=ppc_campaigns days=30 limit=30`

Steps:
1. Call `amazon_metric metric=ppc_invalid_traffic days=30 limit=30`.
2. Find the account's normal filtered share. Flag campaigns at three times that or more.
3. Call `amazon_metric metric=ppc_campaigns days=30 limit=30` and compare flagged campaigns' conversion rates to the account.

Checks before answering:
- Filtered clicks are already excluded from billing. Never call them wasted spend or a refund due.
- A campaign with very few clicks can show a high share by chance. Require at least 500 clicks.

Output:
- One line: the account's filtered share and any campaign far above it.
- A table: campaign, ad type, clicks, filtered share, conversion rate against the account.

Never:
- Never claim money is owed back.
- Never change campaigns in the account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-invalid-traffic-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
