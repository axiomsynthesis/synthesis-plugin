# Save subscribers before they cancel

Channel: Subscriptions · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Save subscribers before they cancel" (id: subscriptions-save-list, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds subscribers who are likely to cancel soon and says what to offer each group to keep them. The offer comes from why people actually cancel, so a price worry gets a different offer than too much product.

What to read: Recharge
What to give me: Subscribers likely to cancel soon, the revenue at stake, and the offer for each group

Synthesis tools to use:
- `recharge_metric metric=subscriber_rfm`
- `recharge_metric metric=churn`
- `recharge_metric metric=cancellation_reasons`
- `recharge_metric metric=upcoming_charges`
- `export_xlsx`

Steps:
1. Call `recharge_metric` with `metric=subscriber_rfm` for subscribers in the at risk and slipping groups.
2. Call `recharge_metric` with `metric=churn` and `months=6` for the cancel rate, split into chosen cancels and failed payments.
3. Call `recharge_metric` with `metric=cancellation_reasons` and `months=6` for why people leave.
4. Call `recharge_metric` with `metric=upcoming_charges` to see who renews in the next 30 days.
5. Match each group to an offer: skip a month, a smaller box, a swap, or a card update for failed payments. Call `export_xlsx` with `filename=subscription_save_list.xlsx`.

Checks before answering:
- Failed payments are not a choice. Give them a card update, never a discount.
- If the Recharge read is empty, say it could not be read. Never call that zero at risk.
- Say how many subscribers each offer rests on. A tiny group is a guess.

Output:
- One line first: how many are at risk and the monthly revenue at stake.
- A file named `subscription_save_list.xlsx`: subscriber ID, group, next charge date, monthly value, reason, offer.
- A person loads the list into the email or SMS tool and sends.

Never:
- Never change, pause or discount a subscription. A person does that.
- Never guess a cancel reason the data did not give.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: subscriptions-save-list". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
