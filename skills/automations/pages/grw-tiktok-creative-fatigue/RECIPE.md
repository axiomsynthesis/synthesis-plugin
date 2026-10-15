# Replace tired TikTok ads

Channel: TikTok Ads · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Replace tired TikTok ads" (id: grw-tiktok-creative-fatigue, TikTok Ads).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok ads tire faster than Meta ads. This finds ads whose click rate or cost has slipped from their peak, and sets the monthly number of new ads you need to keep spend steady.

What to read: TikTok ad results over each ad's life
What to give me: TikTok ads past their best, and how many fresh ones you need each month

Synthesis tools to use:
- `tiktok_metric metric=coverage`
- `tiktok_metric metric=creative_fatigue limit=30`
- `tiktok_metric metric=campaign_leaderboard limit=20`

Steps:
1. Run `tiktok_metric metric=coverage`.
2. Pull `tiktok_metric metric=creative_fatigue limit=30`.
3. Flag ads whose recent click rate is under 70% of their peak or cost per purchase up more than 30%.
4. Pull `tiktok_metric metric=campaign_leaderboard limit=20` for spend context.
5. Estimate a typical ad's useful life in weeks from the fatigued ads, and the new ads per month needed.

Checks before answering:
- Run `tiktok_metric metric=coverage` first. If any authorized ad account is not selected or the authorization is near its 30-day end, say so before reading spend.
- Ads under $100 spend are listed, not judged.
- TikTok spend lives in two places that never overlap: auction ads and shop ads (GMV Max). Always name which you quote, and add them only for total spend.

Output:
- Answer first. Table with columns ad, spend, peak click rate, recent click rate, weeks live, verdict.
- One line: new ads needed per month.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tiktok-creative-fatigue". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
