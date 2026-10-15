# What email should send next

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What email should send next" (id: email-strategy-review, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which flows and campaigns earn money, and what to send next.
It ranks flows by revenue per recipient and finds gaps, like no win-back flow.
It plans the next month of sends.

What to read: Klaviyo flows and campaigns, orders
What to give me: Which flows and campaigns earn, the flow to fix first, and a 30-day sending plan

Synthesis tools to use:
- `klaviyo_metric metric=flow_funnel`
- `klaviyo_metric metric=campaign_scorecard`
- `klaviyo_metric metric=campaign_vs_flow_mix`
- `klaviyo_metric metric=email_revenue_reconciliation`

Steps:
1. Call `klaviyo_metric` with `metric=flow_funnel` to rank flows by revenue per recipient and find where people drop off. Flow numbers are Klaviyo's running totals, with no date setting, so say so.
2. Call `klaviyo_metric` with `metric=campaign_scorecard` to rank campaigns the same way. This read has no date setting, so say the dates the result covers.
3. Call `klaviyo_metric` with `metric=campaign_vs_flow_mix` to see how much email revenue comes from flows against campaigns. It is an all-time split, not a recent one.
4. Call `klaviyo_metric` with `metric=email_revenue_reconciliation` and `months=3` to check Klaviyo's revenue against real orders.
5. List missing flows, the weakest flow to fix, and a 30-day send plan.

Checks before answering:
- If Klaviyo is not connected or a read is empty, say so. Never say "no revenue from email".
- Klaviyo credits revenue generously. Use the order check before quoting email revenue as real.
- A flow with a few hundred recipients cannot be ranked with confidence. Say so.

Output:
- One line answer first: the flow to fix first and what it is worth a month.
- A table: flow, recipients, revenue per recipient, call.
- A 30-day plan: date, send, goal.

Never:
- Nothing goes live in any account. A person changes flows in Klaviyo.
- Never guess revenue the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: email-strategy-review". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
