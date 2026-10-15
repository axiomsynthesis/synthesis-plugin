# What your subject lines teach you

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What your subject lines teach you" (id: grw-email-subject-lessons, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks at every subject line and email design you have sent and asks which features went with more clicks and orders: a number, a question, an emoji, a discount, length, a template. It is honest about thin evidence.

What to read: Klaviyo campaign subject line features and their click and order lift
What to give me: The words and shapes that work for your list, with the evidence behind each

Synthesis tools to use:
- `klaviyo_metric metric=subject_feature_lift`
- `klaviyo_metric metric=content_copy_features`
- `klaviyo_metric metric=template_performance limit=20`

Steps:
1. Pull `klaviyo_metric metric=subject_feature_lift`.
2. Pull `klaviyo_metric metric=content_copy_features`.
3. Pull `klaviyo_metric metric=template_performance limit=20`.
4. Keep features tested on at least 10 campaigns on each side. Rank by lift in click rate and in orders per delivered.
5. Turn the top three into rules for the next five campaigns.

Checks before answering:
- Open rates are inflated by Apple's privacy auto-opens. Judge on clicks and placed orders, never on opens alone.
- Most brands have under a year of sends. Say how many campaigns a finding rests on, and call anything under 10 a hint, not a result.
- A feature present in the data was not necessarily tested. Read how many campaigns had it.
- Campaigns without a usable subject drop out. Say how many were used.

Output:
- Answer first. Table with columns feature, campaigns with, without, click lift, order lift, confidence.
- Three rules for the next campaigns.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-subject-lessons". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
