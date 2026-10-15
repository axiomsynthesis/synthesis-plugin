# Monthly client recap deck in my agency's look

Channel: Agency · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Monthly client recap deck in my agency's look" (id: agency-monthly-client-recap-deck, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the monthly recap deck you walk a client through. Every slide wears your agency's look and the cover is signed Prepared by your agency. Every number is checked before the deck is made.

What to read: All of this client's channels, your agency's look
What to give me: An 8 to 10 slide recap of the client's month in your agency's look: results, what drove them, next month's plan

Synthesis tools to use:
- `switch_brand`
- `brand_kit`
- `data_freshness`
- `yoy_comparison`
- `channel_revenue_mix`
- `query_series metric=net_revenue grain=month`
- `monthly_projection`
- `render_report format=pptx`

Steps:
1. Call `switch_brand` with no arguments to confirm the client. Switch with its brand id if the conversation is on another one.
2. Call `brand_kit`. It must answer `source: agency`. Keep its colours, type, logo and `prepared_by` name.
3. Call `data_freshness`. The month must be closed in every source you quote.
4. Call `yoy_comparison` with `month` set to the last complete month (`YYYY-MM`).
5. Call `channel_revenue_mix` with the same `month`, and `query_series` with `metric=net_revenue`, `grain="month"` for the last 13 months.
6. Call `monthly_projection` for where this month is heading.
7. Write 8 to 10 slides: the month at a glance, the year-on-year change, the channel split, what worked, what to fix, next month's plan. Build it with `render_report`, `format="pptx"`, `filename="client-monthly-recap.pptx"`.

Checks before answering:
- `brand_kit` must say `source: agency`. If it says `brand` or `unknown`, stop and say why before building anything.
- Compare the month with the same month last year, not with the month before, unless you say so.
- A source not current through the month's last day is named on its slide.
- If a read fails, that slide says the number is missing. Never a zero in its place.

Output:
- One line first: the client's month in one sentence with dollars and the change.
- File: client-monthly-recap.pptx from `render_report`, in the agency's look, signed Prepared by the agency.
- Then the three points to lead the call with.

Never:
- Never style a slide in the client's colours, type or logo.
- Never send the deck to the client. A person at the agency does that.
- Never guess a number a tool did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-monthly-client-recap-deck". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
