# Your best and worst landing pages

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your best and worst landing pages" (id: grw-ga4-landing-leaderboard, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks the pages where visits start by how many turn into purchases. It points paid traffic at the winners and lists the losing pages worth fixing first.

What to read: GA4 landing pages with sessions, engagement and conversion
What to give me: The pages that turn visitors into buyers, and the ones that lose them

Synthesis tools to use:
- `ga4_metric metric=landing_pages days=28 limit=50`
- `ga4_metric metric=traffic_sources days=28 limit=20`

Steps:
1. Pull `ga4_metric metric=landing_pages days=28 limit=50`.
2. Keep pages with at least 300 sessions.
3. Rank by purchase rate computed from summed purchases over summed sessions.
4. Pull `ga4_metric metric=traffic_sources days=28 limit=20` to note which source feeds each big page.

Checks before answering:
- GA4 is behaviour only. Never quote its revenue as sales; sales come from the order data.
- A landing page is where the visit started, not every page seen. Say so.
- Pages under 300 sessions are listed apart.

Output:
- Answer first. Table with columns page, sessions, purchase rate, main source, verdict.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-ga4-landing-leaderboard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
