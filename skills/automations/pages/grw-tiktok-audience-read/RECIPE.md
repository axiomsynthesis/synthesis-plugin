# Who buys from your TikTok ads

Channel: TikTok Ads · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who buys from your TikTok ads" (id: grw-tiktok-audience-read, TikTok Ads).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Breaks TikTok auction ads down by audience segment, such as age and interest, to find where purchases come cheap and where spend leaks.

What to read: TikTok ad results by audience segment
What to give me: The audiences worth more budget and the ones to drop

Synthesis tools to use:
- `tiktok_metric metric=coverage`
- `tiktok_metric metric=audience_performance months=3`

Steps:
1. Run `tiktok_metric metric=coverage`.
2. Pull `tiktok_metric metric=audience_performance months=3`.
3. Flag segments with at least $300 spend and cost per purchase 40% better or worse than the account.

Checks before answering:
- Run `tiktok_metric metric=coverage` first. If any authorized ad account is not selected or the authorization is near its 30-day end, say so before reading spend.
- This covers auction ads only. Shop ads do not report by audience. Say so.

Output:
- Answer first. Table with columns segment, spend, purchases, cost per purchase, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tiktok-audience-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
