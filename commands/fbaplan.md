---
description: "FBA ship plan for a client: The finished ship plan as a PDF and a spreadsheet: units to ship into FBA for every product, with the demand and stock behind each"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# FBA ship plan for a client

Channel: Agency · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "FBA ship plan for a client" (id: agency-fba-ship-plan, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Hands back the finished ship plan: the same fixed page for every brand, as a PDF and a spreadsheet. It gives the exact units to ship into FBA for every product so each holds 90 days of stock. Demand is the highest of the last 7, 30, 60 and 90 days' sales with sale days and spikes left out. Upcoming Amazon sales such as Black Friday are added at the product's own lift last year, and stock already at or on its way to Amazon is taken off.

What to read: Amazon sales by day, the live stock feed, upcoming Amazon sales and last year's same sale
What to give me: The finished ship plan as a PDF and a spreadsheet: units to ship into FBA for every product, with the demand and stock behind each

Synthesis tools to use:
- `switch_brand`
- `amazon_metric metric=fba_ship_plan_report target_days=90 transit_days=20 fast_transit_days=17`

Steps:
1. Call `switch_brand` with no arguments. If it is not the client named, call `switch_brand` with that client's brand id.
2. Call `amazon_metric` with `metric=fba_ship_plan_report`, `target_days=90`, `transit_days=20`, `fast_transit_days=17`. Use the client's own days of stock and days to land if they gave them.

Checks before answering:
- If the result has `error`, say it in plain words and stop. No file was made.
- The server wrote every word and number on the page. Do not rebuild the table or reword the page.

Output:
- One line first: the result's `summary`.
- The PDF link (`download_url`) and the spreadsheet link (`spreadsheet_url`).

Never:
- Never build or send a shipment. Hand over the links; a person creates the shipment in Seller Central.
- Never round a line down.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Inputs only I know: supplier lead time in days. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Then tell me to save the lead time on the Costs (COGS) page, Lead times & rivals tab. On a scheduled run, name what is missing instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-fba-ship-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: agency-fba-ship-plan".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
