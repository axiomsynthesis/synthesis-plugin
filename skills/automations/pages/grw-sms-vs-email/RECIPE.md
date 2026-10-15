# Is SMS paying for itself?

Channel: SMS · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is SMS paying for itself?" (id: grw-sms-vs-email, SMS).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
SMS costs money per message and annoys people faster than email. This compares SMS and email on revenue per message and unsubscribes so you know whether to grow or trim SMS.

What to read: Klaviyo results split by email and SMS by month
What to give me: SMS revenue per send and per subscriber against email, and whether to send more or less

Synthesis tools to use:
- `klaviyo_metric metric=channel_monthly months=6`
- `klaviyo_metric metric=campaign_scorecard limit=40`

Steps:
1. Pull `klaviyo_metric metric=channel_monthly months=6` and split by send channel.
2. Pull `klaviyo_metric metric=campaign_scorecard limit=40` for per-send SMS results.
3. Compute revenue per thousand messages and unsubscribe rate for each channel.
4. Ask for the SMS cost per message if not known, and net it off.

Checks before answering:
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- If the brand has no SMS sends in Klaviyo, say SMS is not on Klaviyo. Never say SMS earns zero.
- SMS sent through another tool is not in this data. Say so.

Output:
- Answer first. Table by channel: messages, revenue per thousand, unsubscribe rate, cost per thousand, net.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sms-vs-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
