# Build the quarterly strategy deck

Channel: Leadership · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build the quarterly strategy deck" (id: leadership-quarterly-strategy-deck, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the quarterly strategy deck: how the quarter went, the three bets for next quarter, the risks and the asks. Every number on a slide is checked before the deck is made.

What to read: All channels
What to give me: A 10 to 12 slide deck: how the quarter went, three bets for next quarter, the risks and the asks

Synthesis tools to use:
- `build_deck`
- `monthly_pnl`
- `channel_revenue_mix`
- `yoy_comparison`
- `strategy_framework`

Steps:
1. Call `monthly_pnl` for each month of the last closed quarter, and `yoy_comparison` for the same quarter a year ago.
2. Call `channel_revenue_mix` to show where sales came from.
3. Call `strategy_framework framework=swot strengths=[...] weaknesses=[...] opportunities=[...] threats=[...]` with the quarter's facts, each with its number, to frame strengths, risks and bets.
4. Call `build_deck` with `template="operating_review"`, `period` set to the quarter and `filename="quarterly-strategy.pptx"`.
5. Read the deck back and fix any slide whose number does not match the reads above.

Checks before answering:
- Use the last closed quarter only. A quarter still settling is labelled as such.
- If a P&L month is missing, say so on the slide. Never fill it in.
- Every bet must rest on a number in the deck, not on a hunch.

Output:
- One line first: the quarter's sales, margin and the change on a year ago.
- A deck of 10 to 12 slides: scorecard, channel mix, what worked, what did not, three bets, risks, asks.
- File: quarterly-strategy.pptx. If you can save files here, save it and tell me its name. If not, show it in full.

Never:
- Never share the deck outside the company. A person does that.
- Never guess a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-quarterly-strategy-deck". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
