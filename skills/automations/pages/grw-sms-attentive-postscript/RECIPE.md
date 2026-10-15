# How your SMS is doing (Attentive or Postscript)

Channel: SMS · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How your SMS is doing (Attentive or Postscript)" (id: grw-sms-attentive-postscript, SMS).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Gives the same SMS read for brands that send through Attentive or Postscript instead of Klaviyo. The connectors exist, but no reading tool has been built on them yet.

What to read: Attentive or Postscript campaigns, flows, subscribers and opt-outs
What to give me: Revenue per message, list growth and opt-out trend for brands not on Klaviyo SMS

Synthesis tools to use:
- `klaviyo_metric metric=channel_monthly months=6`

Steps:
1. Confirm which SMS tool the brand uses.
2. When a reader exists: pull campaigns and flows by month, revenue per thousand messages, opt-out rate and subscriber growth.
3. Compare with email from `klaviyo_metric metric=channel_monthly months=6`.

Checks before answering:
- An empty SMS dataset means not connected, never zero sends.

Output:
- Table by month: messages, revenue per thousand, opt-outs, net new subscribers.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sms-attentive-postscript". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Connectors for Attentive and Postscript exist but no governed reading tool does. No governed customer tool reads this yet. The raw warehouse query is founder-only, so customers cannot run it. Do the parts you can and say plainly what is missing.
