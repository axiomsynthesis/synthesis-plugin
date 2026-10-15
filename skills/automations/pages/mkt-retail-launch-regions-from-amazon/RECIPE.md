# Where to launch in stores first

Channel: Retail · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where to launch in stores first" (id: mkt-retail-launch-regions-from-amazon, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A buyer will often start a new brand in a few regions. This uses your Amazon sales by state to show where you already have fans, so you can ask for the right regions.

What to read: Your Amazon sales and customers by US state over the last 12 months
What to give me: The states and regions where you already sell best online, to propose as your first stores

Synthesis tools to use:
- `amazon_metric metric=geo_penetration months=12 limit=51`

Steps:
1. Call `amazon_metric metric=geo_penetration months=12 limit=51`.
2. For each state, compare its share of your sales with its share of US population. Ask the person for population shares or a source if needed. Never invent them.
3. Group states into the retailer's regions if the person gives them. Rank by index.

Checks before answering:
- Sales follow population. Always show an index against population, not raw share.
- Small states swing on few customers. Flag states with under 200 customers.
- Online buyers are not store buyers. Say this is a signal of brand awareness, not a store forecast.

Output:
- One line: the regions to ask for first.
- A table: state, sales share, population share, index, customers.

Never:
- Never present this as a store sales forecast.
- Never invent population figures.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-launch-regions-from-amazon". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
