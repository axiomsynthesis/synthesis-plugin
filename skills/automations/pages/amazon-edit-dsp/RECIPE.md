# Change Amazon DSP ads for me

Channel: Amazon · Level: Push live · Status: Not possible yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Change Amazon DSP ads for me" (id: amazon-edit-dsp, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Would change display and streaming TV campaigns on Amazon DSP.
This is not available. We have no DSP connection, so nothing can be read or changed there.
Today it can only say what the brand spends on Sponsored ads, for context.

What to read: Amazon DSP
What to give me: A prepared DSP change list, once Amazon DSP access exists

Synthesis tools to use:
- `amazon_metric metric=ppc_rollups`

Steps:
1. Tell the person that Amazon DSP is not connected, and that it needs its own access through an agency or a DSP seat.
2. If they want context, call `amazon_metric` with `metric=ppc_rollups` and `days=30` to show Sponsored ads spend and sales, and say clearly that DSP is not in it.

Checks before answering:
- Never present Sponsored ads numbers as DSP numbers.
- If the person shares DSP numbers by hand, say they come from them and were not read by Synthesis.

Output:
- Two lines: DSP is not connected, and what access would be needed.
- If asked, one line on Sponsored ads spend for the last 30 days.

Never:
- Nothing is pushed to any account.
- Never guess DSP spend or results.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-edit-dsp". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (not possible yet): We do not connect to Amazon DSP today. It needs its own access from Amazon, usually through an agency or a DSP seat. Do the parts you can and say plainly what is missing.
