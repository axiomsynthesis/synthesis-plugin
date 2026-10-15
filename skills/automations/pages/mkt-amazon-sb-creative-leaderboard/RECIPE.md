# Rank your Sponsored Brands ads

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rank your Sponsored Brands ads" (id: mkt-amazon-sb-creative-leaderboard, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Campaign totals hide which single banner or video is doing the work. This ranks each Sponsored Brands ad on its own.
It ends with ads to pause, ads to give more budget, and a one-paragraph brief for the next video.

What to read: Sponsored Brands results at the single ad level, banner and video, over the last 60 days
What to give me: Which banner and video ads earn, which to pause, and what the winners share to brief the next one

Synthesis tools to use:
- `amazon_metric metric=ppc_sb_creatives days=60 limit=40`
- `amazon_metric metric=ppc_campaigns days=60 ad_product=SB limit=25`
- `amazon_metric metric=ppc_ntb days=60`

Steps:
1. Call `amazon_metric metric=ppc_sb_creatives days=60 limit=40`. Each row is one ad id.
2. Call `amazon_metric metric=ppc_campaigns days=60 ad_product=SB limit=25` to put each ad in its campaign and see the campaign's budget.
3. Call `amazon_metric metric=ppc_ntb days=60` for the share of buyers who are new to the brand. Sponsored Brands is where that number lives.
4. Rank ads by return per dollar, with spend and new-to-brand share beside it. Mark pause candidates: over $300 spent and return under the account's break-even.
5. Ask the person to open the top three ad ids in the ads console and describe them. Write the brief from what the winners share.

Checks before answering:
- The report carries ad ids, not names. Say the person must match the id in the console. Never invent an ad name.
- Sponsored Brands history only goes back about 60 days. Never claim a longer trend.
- An ad with under 1,000 impressions is too new to rank. List it separately.
- Ad spend here should add up to the Sponsored Brands campaign spend for the same window. Flag a big gap.

Output:
- One line: the best and worst ad with their return per dollar.
- A table: ad id, campaign, format if known, spend, sales, return per $1, new-to-brand share, verdict.
- A short brief for the next video, five bullets at most.

Never:
- Never pause or edit ads in the account.
- Never describe what an ad looks like without the person confirming it.
- Never compare Sponsored Brands return directly with Sponsored Products return without saying they count sales differently.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-sb-creative-leaderboard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
