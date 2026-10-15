# Warn me before email lands in spam

Channel: Email · Level: On a schedule · Status: Ready now
Schedule: weekly Tuesday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Warn me before email lands in spam" (id: grw-email-deliverability-watch, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every week, checks bounces, spam complaints and unsubscribes on your recent sends. It warns when any crosses a safe line, because inbox providers punish the whole list long before revenue shows the damage.

What to read: Klaviyo bounce, spam complaint and unsubscribe rates by send
What to give me: A warning before inbox placement slips, with the likely cause

Synthesis tools to use:
- `klaviyo_metric metric=deliverability days=90`
- `klaviyo_metric metric=campaign_scorecard limit=30`

Steps:
1. Pull `klaviyo_metric metric=deliverability days=90`.
2. Pull `klaviyo_metric metric=campaign_scorecard limit=30` to tie spikes to a specific send.
3. Flag spam complaints above 0.1% of delivered, bounces above 2%, or unsubscribes above 0.5% on any send.
4. For each flagged send, note the audience size and segment, since sends to old unengaged profiles cause most spikes.

Checks before answering:
- Exclude seed and inbox-test sends. They go to tiny internal lists and drag every rate down.
- Compute rates from summed counts, never by averaging send rates.
- If no sends happened in the window, say so. Never report healthy on zero sends.

Output:
- One line when healthy. Otherwise: send, date, audience, rate, safe line, likely cause, fix.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-deliverability-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Tuesday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
