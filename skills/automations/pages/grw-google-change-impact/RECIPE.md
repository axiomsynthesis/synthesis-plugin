# What changed in Google Ads, and did it work?

Channel: Google · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What changed in Google Ads, and did it work?" (id: grw-google-change-impact, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists every change made in your Google Ads account in the last month, with who made it. It sets each big change beside cost and return in the days before and after, so you can see whether your agency's edits helped.

What to read: The Google Ads change history and daily results around each change
What to give me: Every change made in the account, who made it and what happened after

Synthesis tools to use:
- `google_ads_metric metric=changes days=30 limit=100`
- `google_ads_metric metric=efficiency_trend weeks=8`

Steps:
1. Pull `google_ads_metric metric=changes days=30 limit=100`.
2. Group changes by day and by who made them.
3. Pull `google_ads_metric metric=efficiency_trend weeks=8`.
4. For bid, budget and keyword changes, compare cost per conversion for 7 days before and 7 days after.
5. List changes followed by a clear worsening, and periods with no changes at all.

Checks before answering:
- Google Ads campaign and keyword data holds at most 90 days. A short history is the age of the connection, not a business fact. Never compare year over year here.
- Before-and-after is not proof. A change during a promotion or a holiday is confounded. Say so.
- Fewer than 20 conversions in either window is too few to judge.

Output:
- Answer first. Table with columns date, who, what changed, cost per conversion before, after, note.
- A count of changes per person.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never accuse a person of a mistake. Describe what changed and what followed.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-change-impact". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
