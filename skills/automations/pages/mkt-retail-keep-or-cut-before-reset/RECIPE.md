# Defend your items at the shelf reset

Channel: Retail · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Defend your items at the shelf reset" (id: mkt-retail-keep-or-cut-before-reset, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Before a shelf reset, you choose which items to fight for. This ranks each item on rate, growth, share and margin, and drafts the case for each call.

What to read: Each retail item's sales rate, growth, category share, our margin per unit and its Amazon search demand
What to give me: A defend, swap or let-go call for each item before the retailer resets the shelf, with the case for each

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=breakdown`
- `search_files query=category`
- `operator_inputs section=cogs`
- `amazon_metric metric=search_query_trend grain=month periods=12`

Steps:
1. Call `gsheets_metric metric=tables` and `gsheets_metric metric=breakdown` for item sales rate and growth over 52 weeks.
2. Call `search_files query=category` and open any uploaded category report with `read_file` for category share by item.
3. Call `operator_inputs section=cogs` for our margin: the retailer's cost price minus our cost. Never the shelf price.
4. Call `amazon_metric metric=search_query_trend grain=month periods=12` for demand behind each item's size or flavor.
5. Call each item: defend (fast and growing), swap (slow but we have a better item), let go (slow, low margin, falling demand).

Checks before answering:
- Our margin is what the retailer pays us minus our cost. Never the shelf price.
- Share fractions and percents differ by column. Convert once.
- Amazon demand is a signal, not proof of store demand. Say so.

Output:
- One line: how many to defend, swap and let go.
- A table: item, rate, growth, share, our margin, call, one-line case.

Never:
- Never send this to a buyer. A person decides and sends.
- Never call the retailer's margin ours.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-keep-or-cut-before-reset". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No governed tool reads store sales or syndicated category share for customers yet. Needs item sales and category share connected per brand. Until then it works only from a connected Google Sheet or an uploaded category report. Do the parts you can and say plainly what is missing.
