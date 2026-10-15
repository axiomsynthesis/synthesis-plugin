# Three honest Meta return numbers

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Three honest Meta return numbers" (id: grw-meta-three-roas, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts Meta's own return number beside your whole-business return on all ad spend and beside a version cut for the credit Meta usually overclaims. It ends the argument about which number is right by saying what each one is for.

What to read: Meta-reported return, blended marketing efficiency, and a haircut for credit Meta did not earn
What to give me: Meta's three return numbers side by side, and which one to plan with

Synthesis tools to use:
- `meta_metric metric=roas month=<YYYY-MM>`
- `meta_metric metric=spend month=<YYYY-MM>`
- `mer month=<YYYY-MM>`
- `attribution_lenses`

Steps:
1. Pick the last fully closed month.
2. Pull `meta_metric metric=roas` and `meta_metric metric=spend` for that month.
3. Pull `mer` for that month.
4. Run `attribution_lenses platform_roas=<meta roas> blended_mer=<mer> incrementality_haircut_pct=<value>`. Use 30 when the brand has no lift test, and say it is an assumption.
5. Explain each lens in one line: Meta's view, the whole business view, the cautious view.

Checks before answering:
- If `mer` is gated, do not state it. Give its refusal reason.
- Use a closed month only.
- The haircut is an assumption unless the brand ran a holdout. Label it.

Output:
- Answer first. A 3-row table: lens, value, use it for.
- One sentence on which to plan budget with.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never add Meta-reported revenue to store revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-three-roas". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
