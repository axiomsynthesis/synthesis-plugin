# Update my Klaviyo flows for me

Channel: Email · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Update my Klaviyo flows for me" (id: email-update-klaviyo-flows, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Would edit flows and templates directly in Klaviyo, after showing the edits first and getting your approval.
Nothing is pushed today, because our Klaviyo key only reads.
Today it prepares the edit list a person makes in Klaviyo.

What to read: Klaviyo
What to give me: Flow edits made in Klaviyo after you approve them, with the revenue at stake

Synthesis tools to use:
- `klaviyo_metric metric=flow_step_performance`
- `klaviyo_metric metric=flow_funnel`

Steps:
1. Call `klaviyo_metric` with `metric=flow_funnel` to find the flows that lose the most people. Flow numbers are Klaviyo's running totals, with no date setting, so say so.
2. Call `klaviyo_metric` with `metric=flow_step_performance` to find the weak step inside each one. It has no date setting either.
3. Write each edit: flow, step, what to change, and why.
4. Hand the person the edit list to make in Klaviyo.

Checks before answering:
- If a flow read is empty, say it could not be read. Never call a flow weak from missing data.
- A step with few recipients cannot be judged. Say so.

Output:
- An edit list: flow, step, current, proposed change, revenue at stake a month.

Never:
- Nothing is pushed to any account. A person makes the edits in Klaviyo.
- Never guess revenue the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: email-update-klaviyo-flows". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Our Klaviyo key only reads. A brand would need to give us a key that can write. Do the parts you can and say plainly what is missing.
