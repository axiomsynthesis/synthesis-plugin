# What email really makes

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What email really makes" (id: grw-email-revenue-truth, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Klaviyo's revenue number is generous. This ties it to real website orders, splits campaigns from flows, and gives the share of website sales email can fairly claim.

What to read: Klaviyo-credited revenue against Shopify orders, campaigns against flows
What to give me: Email's honest revenue, its share of website sales, and how much rests on flows

Synthesis tools to use:
- `klaviyo_metric metric=email_revenue_reconciliation months=6`
- `klaviyo_metric metric=campaign_vs_flow_mix`
- `klaviyo_metric metric=channel_monthly months=6`

Steps:
1. Pull `klaviyo_metric metric=email_revenue_reconciliation months=6`.
2. Pull `klaviyo_metric metric=campaign_vs_flow_mix`.
3. Pull `klaviyo_metric metric=channel_monthly months=6` to split email and SMS.
4. Show Klaviyo-credited revenue, matched website order revenue, and the share of website sales, by month.

Checks before answering:
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- Flow revenue has no send date, so it cannot enter a monthly number directly. Say how the tool handles it.
- Use closed months only.

Output:
- Answer first. Table by month: Klaviyo credited, matched to orders, share of website sales, campaign share, flow share.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never add email revenue to total revenue. It is already inside it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-revenue-truth". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
