# Find your best time to send email

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find your best time to send email" (id: grw-email-send-time, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Groups your campaigns by send day and hour and compares clicks and orders. It recommends a default send slot and says how sure it is.

What to read: Klaviyo campaign results by day and hour sent
What to give me: The day and hour your list clicks and buys most, and how sure that is

Synthesis tools to use:
- `klaviyo_metric metric=send_timing`

Steps:
1. Pull `klaviyo_metric metric=send_timing`.
2. Compute click rate and orders per thousand delivered for each day and hour group.
3. Keep groups with at least 5 campaigns.
4. Recommend the best slot and the runner-up.

Checks before answering:
- Open rates are inflated by Apple's privacy auto-opens. Judge on clicks and placed orders, never on opens alone.
- Most brands have under a year of sends. Say how many campaigns a finding rests on, and call anything under 10 a hint, not a result.
- Exclude seed and inbox-test sends. They go to tiny internal lists and drag every rate down.
- Sale emails cluster on certain days. Check the best slot is not only sale sends.

Output:
- Answer first. A short table: slot, campaigns, click rate, orders per thousand.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-send-time". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
