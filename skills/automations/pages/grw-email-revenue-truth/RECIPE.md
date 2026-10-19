# What Klaviyo credits email with

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What Klaviyo credits email with" (id: grw-email-revenue-truth, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what Klaviyo says email made, next to total website sales, split into campaigns and flows. It is Klaviyo's own last-touch credit. It does not yet match that credit to real orders or measure what email adds.

What to read: Klaviyo-credited revenue against website sales, campaigns against flows
What to give me: The revenue Klaviyo credits to email, as a share of website sales, and how much of it rests on flows. Not yet matched to real orders

Synthesis tools to use:
- `klaviyo_metric metric=email_revenue_reconciliation months=6`
- `klaviyo_metric metric=campaign_vs_flow_mix`
- `klaviyo_metric metric=channel_monthly months=6`

Steps:
1. Pull `klaviyo_metric metric=email_revenue_reconciliation months=6`.
2. Pull `klaviyo_metric metric=campaign_vs_flow_mix`.
3. Pull `klaviyo_metric metric=channel_monthly months=6` to split email and SMS.
4. Show Klaviyo-credited revenue and its share of website sales, by month.

Checks before answering:
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- This cannot match Klaviyo's credit to real orders yet, net refunds, or split new and returning buyers. Say so.
- This cannot say what email really adds. That needs a holdout: a group that gets no email. Say so.
- Flow revenue has no send date, so it cannot enter a monthly number directly. Say how the tool handles it.
- Check the latest month in the result. If it is more than one closed month old, say the email data is stale and stop at that month.
- Use closed months only.

Output:
- Answer first, labelled as Klaviyo's credit. Table by month: Klaviyo credited, share of website sales, campaign share, flow share.
- One line on what this cannot show yet.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never add email revenue to total revenue. It is already inside it.
- Never call Klaviyo's credit what email really makes.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-revenue-truth". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
