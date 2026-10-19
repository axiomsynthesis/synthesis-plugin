---
description: "Why subscribers cancel, and what to change: How fast paying subscriptions shrink, how often charges are skipped, and the changes that fix it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Why subscribers cancel, and what to change

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why subscribers cancel, and what to change" (id: grw-sub-cancel-reasons-fix, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how fast paying subscriptions shrink and how often charges are skipped, then groups the reasons subscribers give when they cancel and turns each into a change. Many skips and too much product are usually a plan-length problem, not a product problem.

What to read: Six months of subscription cancels, skips, cancel reasons, plan lengths and products
What to give me: How fast paying subscriptions shrink, how often charges are skipped, and the changes that fix it

Synthesis tools to use:
- `recharge_metric metric=cancellation_reasons months=6`
- `recharge_metric metric=churn months=6`
- `recharge_metric metric=interval_mix`
- `recharge_metric metric=product_subscriptions limit=60`
- `recharge_metric metric=rebill_health months=6`

Steps:
1. Pull `recharge_metric metric=churn months=6`. Report new and cancelled subscriptions per month and the net change. Split cancels into chosen and failed payment.
2. Pull `recharge_metric metric=interval_mix` and `recharge_metric metric=product_subscriptions limit=60`. Divide each month's cancels by `billing_active_subs` from the plan-length read, labelled share of paying subscriptions lost each month.
3. Pull `recharge_metric metric=rebill_health months=6`. Report `skip_rate` per closed month and failed charges on their own line. If skips are above 30%, put a longer default plan first among the changes, ahead of the cancel reasons.
4. Pull `recharge_metric metric=cancellation_reasons months=6`. Rank named reasons by count. Show other as a residual, not a driver.
5. Map each top reason to a change: too much product to a longer plan or a skip offer, too expensive to a smaller pack, stopped using to a pause offer and a how-to-use reminder, signed up by accident to a clearer sign-up step, dissatisfied to a product question.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Report how many cancellations had a named reason.
- Failed payments are a different problem from cancels. Give them on their own line as failed charges. Never count them as cancellations.
- Cancel reasons are six-month totals. They are not split by month or product, so never tie a reason to a plan length or a product. Show plan lengths beside them as their own read.
- A skip keeps the subscription. It is not a cancel, but many skips mean the plan ships too often.
- The share lost each month uses today's paying count as the base, so older months are rough. Say so.
- Plan-length lifespans cover cancelled subscriptions only, so they run short. Say so.
- Count only subscriptions that are billing now as active. The plan-length read also counts old ones that never formally ended. Say which number you use.

Output:
- Answer first: the net change in paying subscriptions per month, the skip rate, and the first change to make.
- Table by month: new, cancelled, net change, share lost, skip rate.
- Table: reason, cancellations, share, change to make.
- One test: the first change for new subscribers or at cancel time, read by save rate and how many are still paying after 90 days.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-cancel-reasons-fix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
