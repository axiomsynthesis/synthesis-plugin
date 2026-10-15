# Is Meta riding on one ad?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is Meta riding on one ad?" (id: grw-meta-spend-concentration, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how much of your Meta budget depends on a handful of ads. When one ad carries a big share and starts to tire, the whole account drops at once. It names the ads you lean on and what to have ready behind them.

What to read: Meta spend share by ad and campaign
What to give me: How much of Meta rides on one or two ads, and the backup plan

Synthesis tools to use:
- `meta_metric metric=spend_concentration`
- `meta_metric metric=creative_leaderboard limit=20`
- `meta_metric metric=creative_fatigue_curve limit=10`

Steps:
1. Pull `meta_metric metric=spend_concentration` for the share of spend in the top 1, 3 and 5 ads.
2. Pull `meta_metric metric=creative_leaderboard limit=20` and match the top ads by ad id.
3. For each ad above 20% of spend, pull `meta_metric metric=creative_fatigue_curve ad_id=<id>` to see whether its click rate or cost per purchase is already slipping.
4. Count how many ads below the top five have at least 10 purchases at a cost per purchase within 20% of the account. Those are the ready backups.

Checks before answering:
- Match ads by ad id, never by name. Ad names repeat.
- Run `meta_metric metric=account_daily` first. An ACCOUNT STALE flag means recent zero spend is missing data, not a pause. Stop and say so before reading any trend.
- If fewer than five ads spent in the window, say the account is too small for a concentration read.
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.

Output:
- Answer first: top-ad share and whether it is a risk.
- Table with columns ad id, short name, share of spend, cost per purchase, fatigue sign (yes or no).
- One line on how many proven backups exist and the next creative to brief.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never call an ad a backup on fewer than 10 purchases.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-spend-concentration". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
