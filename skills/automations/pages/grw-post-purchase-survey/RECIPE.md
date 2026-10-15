# Where customers say they found you

Channel: Customers · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where customers say they found you" (id: grw-post-purchase-survey, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts customers' own answer to how they heard about you beside what each ad platform takes credit for. It shows channels no tag sees, like podcasts, word of mouth and stores.

What to read: Post-purchase survey answers by month and channel
What to give me: What customers say brought them in, next to what the ad platforms claim

Synthesis tools to use:
- `meta_metric metric=spend month=<YYYY-MM>`
- `google_ads_metric metric=campaign_performance days=30`

Steps:
1. When a reader exists: pull survey answers by month with response count.
2. Set each channel's share of answers beside its share of ad spend from `meta_metric` and `google_ads_metric`.

Checks before answering:
- A survey is a signal, never revenue. Never multiply answer shares by sales and call it attribution.
- Report the response rate. Under 15% is a thin read.
- An empty dataset means not connected.

Output:
- Table: channel, share of answers, share of spend, gap.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-post-purchase-survey". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The Fairing connector exists but holds no rows and no governed reading tool exists. A sync and a reader are needed. Do the parts you can and say plainly what is missing.
