# This week in stores

Channel: Retail · Level: On a schedule · Status: Ready after we build it
Schedule: every Tuesday 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "This week in stores" (id: retail-weekly-store-sales-read, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads the weekly Walmart and Target store sales each week. It says how units moved, which products drove it, and which stores sold nothing for weeks, so someone can ask the buyer or a field team to check the shelf.

What to read: Retail POS files
What to give me: Units and dollars by retailer, what drove the change, and stores that sold nothing for weeks

Synthesis tools to use:
- `list_documents`
- `read_file`
- `gsheets_metric metric=breakdown`
- `export_xlsx`

Steps:
1. Call `list_documents` to find this week's retail store sales file or connected sheet.
2. Call `read_file` with its `file_id`, or `gsheets_metric` with `metric=breakdown` on the sheet, by store and by product.
3. Compare units to last week and to the four-week average, for each retailer.
4. List stores with zero units for three weeks or more on a product they carry.
5. Call `export_xlsx` with `filename=store_watch_list.xlsx` for the store list.

Checks before answering:
- A store at zero may not carry the product. Only flag stores that sold it before.
- If this week's file is missing, say so. Never compare against last week's file twice.
- One week's change is not a trend. Say so.

Output:
- One line first: units and dollars this week by retailer, and the change.
- A short table: product, units, change, stores selling.
- A file named `store_watch_list.xlsx`: retailer, store, product, weeks at zero, last week sold.

Never:
- Never contact a buyer or a store. A person does that.
- Never fill a missing store or week with a guess.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: retail-weekly-store-sales-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every Tuesday 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. No customer tool reads the store-level Walmart and Target sales yet, so a store sales tool needs building; until then it works only from a weekly file shared as a document or sheet. Do the parts you can and say plainly what is missing.
