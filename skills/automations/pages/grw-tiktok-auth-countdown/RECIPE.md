# Warn me before TikTok disconnects

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: daily 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Warn me before TikTok disconnects" (id: grw-tiktok-auth-countdown, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok makes you re-approve access every 30 days. If nobody does, ad data quietly stops. This checks the days left each morning and warns a week ahead.

What to read: Days left on TikTok's 30-day ad authorization and which ad accounts sync
What to give me: A warning a week before TikTok data stops, with the reconnect step

Synthesis tools to use:
- `tiktok_metric metric=coverage`

Steps:
1. Run `tiktok_metric metric=coverage`.
2. Read days left on the authorization and the ad accounts not selected.
3. Warn when 7 or fewer days are left, or when an authorized ad account is not syncing.

Checks before answering:
- If coverage returns no TikTok connection, say TikTok ads are not connected. Never say spend is zero.

Output:
- One line when fine. When not: days left, what stops, and the reconnect step on the Connections page.

Never:
- Never reconnect or change the connection for the person.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tiktok-auth-countdown". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (daily 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
