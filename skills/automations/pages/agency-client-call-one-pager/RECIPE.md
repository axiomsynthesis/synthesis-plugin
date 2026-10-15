# Client call one-pager in my agency's look

Channel: Agency · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Client call one-pager in my agency's look" (id: agency-client-call-one-pager, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Gets you ready for a client call in two minutes. One page with where the client stands, what changed, three talking points and one ask. It wears your agency's look and is signed Prepared by your agency.

What to read: This client's recent numbers, your agency's look
What to give me: One page to bring to a client call: where they stand, what changed, three talking points and one ask, in your agency's look

Synthesis tools to use:
- `switch_brand`
- `brand_kit`
- `data_freshness`
- `get_weekly_brief`
- `channel_revenue_mix`
- `monthly_projection`
- `render_report format=pdf`

Steps:
1. Call `switch_brand` with no arguments to confirm the client. Switch with its brand id if needed.
2. Call `brand_kit`. It must answer `source: agency`. Keep its colours, logo and `prepared_by` name.
3. Call `data_freshness` and note any source more than 2 days old.
4. Call `get_weekly_brief` for what moved last week.
5. Call `channel_revenue_mix` for the split across channels, and `monthly_projection` for where the month is heading.
6. Write the page: where they stand, what changed, three talking points, one ask. Build it with `render_report`, `format="pdf"`, `filename="client-call-one-pager.pdf"`.

Checks before answering:
- `brand_kit` must say `source: agency`. If it says `brand` or `unknown`, stop and say why before building anything.
- Every talking point carries a number from a tool, with its date range.
- If a source is stale, say so next to its numbers.
- If a read fails, say that number is missing. Never print a zero in its place.

Output:
- One line first: the one thing to say on the call.
- File: client-call-one-pager.pdf from `render_report`, in the agency's look, signed Prepared by the agency.

Never:
- Never use the client's colours, type or logo as the page's look.
- Never send the page to the client. A person at the agency does that.
- Never guess a number a tool did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-client-call-one-pager". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
