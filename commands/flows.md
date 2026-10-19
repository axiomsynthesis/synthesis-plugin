---
description: "Where your email flows lose people: The flow steps that lose readers or earn nothing, and the step to rewrite"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Where your email flows lose people

Channel: Email · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where your email flows lose people" (id: grw-email-flow-step-leak, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads each automated flow step by step: welcome, abandoned cart, browse, post-purchase and win-back. It finds the step where clicks or orders fall off a cliff and the steps that earn nothing.

What to read: Klaviyo flow step results from first email to last
What to give me: The flow steps that lose readers or earn nothing, and the step to rewrite

Synthesis tools to use:
- `klaviyo_metric metric=flow_funnel`
- `klaviyo_metric metric=flow_step_performance limit=60`

Steps:
1. Pull `klaviyo_metric metric=flow_funnel`.
2. Pull `klaviyo_metric metric=flow_step_performance limit=60`.
3. Put each flow's steps in their real order. Use the email names or templates first, and the number of people reached only when they say nothing.
4. For each flow, compute click rate and placed-order rate per step from summed counts. Give each rate a 95% range, using the Wilson method for a share. Flag a step only when its range sits fully below the step before. Otherwise say there are too few sends to tell, and about how many more sends would settle it.
5. Flag steps with fewer than 1 order per 1,000 delivered only when the range backs it.
6. Name one rewrite or removal per flagged step. List common flows that are missing, such as win-back or browse abandon, with when each last sent.

Checks before answering:
- Open rates are inflated by Apple's privacy auto-opens. Judge on clicks and placed orders, never on opens alone.
- Klaviyo revenue is last-touch credit on website orders. It cannot see Amazon orders. Never call it email's total effect.
- Flow numbers cover recent sends, up to the last 12 months, not a fixed window. Say so.
- Say when the step order is a guess made from how many people each email reached.
- Later steps reach fewer people because some already bought or left. Compare a step only with the step before it, among people sent both.
- Say how many orders each verdict rests on, and call anything under 10 orders a hint, not a result.

Output:
- Answer first: the one step that is truly leaking, or that no step has enough sends to call, and the biggest missing flow.
- Table with columns flow, step, delivered, orders, order rate with its range, problem, move.
- One move: switch on a 10% held-back group in each flow, who get no email, and read extra website orders after 30 days. Name the read date. Say that a discount in the first welcome email may pay buyers who would have ordered anyway.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-email-flow-step-leak". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
