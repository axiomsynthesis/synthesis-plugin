# Client report in my agency's look

Channel: Agency · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Client report in my agency's look" (id: agency-client-report, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds a weekly report for one client that you can send as your own work. It wears your agency's look, set when you signed up: your colours, type and logo. It signs Prepared by your agency, never in the client's colours.

What to read: All of this client's channels, your agency's look
What to give me: A client-ready weekly report in your agency's colours, type and logo, signed Prepared by your agency

Synthesis tools to use:
- `switch_brand`
- `brand_kit`
- `data_freshness`
- `get_weekly_brief`
- `query_series metric=net_revenue grain=week`
- `channel_revenue_mix`
- `render_report format=html`

Steps:
1. Call `switch_brand` with no arguments to see which client this conversation is on. If it is not the client named, call `switch_brand` with that client's brand id first.
2. Call `brand_kit`. It must answer `source: agency`. Keep its colours, type, logo, `prepared_by` name and `rule` for the report.
3. Call `data_freshness` and note any source more than 2 days old.
4. Call `get_weekly_brief` for last week's movers and the items that need attention.
5. Call `query_series` with `metric=net_revenue`, `grain="week"` and the last 8 closed weeks.
6. Call `channel_revenue_mix` for the split across channels.
7. Build it with `render_report`, `format="html"`, `title` the client's name and "weekly report", `filename="client-weekly-report.html"`. It renders in the agency's look and signs the cover for you.

Checks before answering:
- `brand_kit` must say `source: agency`. If it says `brand`, this account is not an agency: say so and build it in the brand's own look only if the person still wants it. If it says `unknown`, call it again and stop if it still cannot tell.
- Use the last closed week only. Sunday's numbers may still be filling in.
- If a source is stale, say so in the report before its numbers.
- If a read fails, say that number is missing. Never print a zero in its place.

Output:
- One line first: the client's sales last week and the change.
- The report: headline numbers, the two biggest movers with dollars, one next step for the client.
- File: client-weekly-report.html from `render_report`, in the agency's look, signed Prepared by the agency, with Powered by Synthesis small in the footer.

Never:
- Never use the client's colours, type or logo as the report's look.
- Never send the report to the client. A person at the agency does that.
- Never guess a number a tool did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-client-report". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
