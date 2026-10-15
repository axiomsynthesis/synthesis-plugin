# How healthy is Subscribe and Save, really?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How healthy is Subscribe and Save, really?" (id: amazon-subscribe-and-save-health, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how healthy your Subscribe and Save program really is. It counts active subscribers, how many sign-ups never get a second delivery, and how long real subscribers stay. Then it names the fix.

What to read: Subscribe and Save reports
What to give me: Active subscribers, how many never get a second delivery, how long real ones stay, and the fix

Synthesis tools to use:
- `amazon_metric metric=sns_program`
- `amazon_metric metric=sns_fake_rate`
- `amazon_metric metric=subscription_ladder`
- `sns_cohorts`
- `subscribe_save_attach_rate`

Steps:
1. Call `amazon_metric` with `metric=sns_program` and `weeks=12` for active subscriptions and Amazon's forecast.
2. Call `amazon_metric` with `metric=sns_fake_rate` and `months=6` for the share of sign-ups that never got a second delivery.
3. Call `sns_cohorts` for how subscribers stay month by month.
4. Call `amazon_metric` with `metric=subscription_ladder` and `limit=10` to see which products hold subscribers best.
5. Call `subscribe_save_attach_rate` with the `asin` of each top product for the share of its orders on Subscribe and Save.

Checks before answering:
- Recent sign-ups have not had time for a second delivery. Only judge sign-ups old enough to have one.
- If a tool says the number is gated, explain why and do not state it.
- If the program data is empty, say it could not be read. Never call that zero subscribers.

Output:
- One line first: active subscribers, the share that never repeat, and the dollar cost of that discount.
- A table: product, share on Subscribe and Save, never-repeat rate, three-month retention.
- One move and how we will know it worked.

Never:
- Never change Subscribe and Save settings or discounts. A person does that.
- Never guess a subscriber count the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-subscribe-and-save-health". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
