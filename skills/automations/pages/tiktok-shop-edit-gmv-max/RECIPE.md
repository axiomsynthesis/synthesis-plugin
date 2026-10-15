# Change TikTok's GMV Max campaigns for me

Channel: TikTok Shop · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Change TikTok's GMV Max campaigns for me" (id: tiktok-shop-edit-gmv-max, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reviews your GMV Max campaigns and writes a change list: budgets to raise or cut and return targets to move. It shows each change first. Nothing is pushed, because our TikTok access cannot write yet.

What to read: TikTok Ads
What to give me: Budget and target changes for each campaign, with the expected effect in dollars

Synthesis tools to use:
- `tiktok_metric metric=campaign_leaderboard`
- `tiktok_metric metric=shop_ad_efficiency`
- `tiktok_metric metric=spend_trend`

Steps:
1. Call `tiktok_metric` with `metric=campaign_leaderboard` and `months=1` to rank campaigns by spend and return.
2. Call `tiktok_metric` with `metric=shop_ad_efficiency` and `months=3` to compare GMV Max return with shop sales.
3. Call `tiktok_metric` with `metric=spend_trend` and `months=2` to see whether spend is rising or falling.
4. Build the change list: campaign, current budget, new budget, current return target, new target, and why.

Checks before answering:
- Use at least 14 days of spend before moving a target. A few days is noise.
- If a campaign returns no data, say so. Never treat it as zero spend.
- Spend is split across auction and GMV Max reports. Say if one is missing.

Output:
- One line first: the single change worth the most money.
- A table: campaign, budget now, budget new, target now, target new, reason, expected effect in dollars.

Never:
- Never push a change. The access does not exist yet, and a person applies every change in TikTok.
- Never guess a return the tools did not show.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: tiktok-shop-edit-gmv-max". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Our TikTok access is read-only and has to be renewed every 30 days, so nothing can be pushed yet. The change list is ready today and a person applies it in TikTok. Do the parts you can and say plainly what is missing.
