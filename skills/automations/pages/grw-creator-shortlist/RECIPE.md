# Score a creator shortlist

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Score a creator shortlist" (id: grw-creator-shortlist, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes a list of creators you are considering and tiers them by audience size. It sets them against the size and engagement of the creators who already sell for you, so you pick the ones most like your winners.

What to read: A list of creator candidates you paste, with followers and engagement
What to give me: Your candidates tiered by size, scored against your past creators, ranked for outreach

Synthesis tools to use:
- `tier_creators`
- `growi_top_creators limit=25`
- `tiktok_metric metric=shop_video_performance days=120 limit=25`

Steps:
1. Ask for the list with name, followers and engagement rate.
2. Run `tier_creators candidates=[...]`.
3. Pull `growi_top_creators limit=25` and `tiktok_metric metric=shop_video_performance days=120 limit=25` for the creators who sell for you now. TikTok's bestseller lists rank the whole US market, not your shop, so never use them for this.
4. Find the tiers and engagement bands where your winners sit.
5. Rank candidates by fit with that band.

Checks before answering:
- Engagement rates must be on one basis. Ask whether they are percents or fractions.
- If no current creator data exists, tier only and say fit cannot be scored.

Output:
- Answer first. Table: candidate, tier, followers, engagement, fit, reason. Top 10 for outreach.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never contact a creator. A person does.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creator-shortlist". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
