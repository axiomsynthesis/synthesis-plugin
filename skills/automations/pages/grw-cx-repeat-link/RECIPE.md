# Does contacting support change repeat buying?

Channel: Support · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does contacting support change repeat buying?" (id: grw-cx-repeat-link, Support).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares customers who wrote to support with those who did not on how often they buy again. It shows which contact reasons go with lost customers, so support time goes where it saves the most.

What to read: Gorgias contacts per customer joined to their orders
What to give me: Whether customers who contact support buy again more or less, by contact reason

Synthesis tools to use:
- `gorgias_metric metric=customer_cx`
- `gorgias_metric metric=contact_reasons months=6`

Steps:
1. Pull `gorgias_metric metric=customer_cx`.
2. Pull `gorgias_metric metric=contact_reasons months=6`.
3. Compare repeat rate for contacted and not contacted customers, and by top reason.

Checks before answering:
- Join is by email. Report the email match rate and stop if under 50%.
- Contact counts are lifetime, not a window. Say so.
- Contact does not cause churn by itself. Unhappy customers both write and leave.

Output:
- Answer first. Table: group or reason, customers, repeat rate.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cx-repeat-link". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): A read that joins each support contact to that customer's later orders, giving repeat rate for customers who wrote in and those who did not, by reason. The support tools today give contact counts and reasons only. Do the parts you can and say plainly what is missing.
