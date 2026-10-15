# Pause ads before a product sells out

Channel: Amazon · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Pause ads before a product sells out" (id: mkt-amazon-pause-ads-on-stockout, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Advertising a product that is about to run out spends money to empty the shelf faster, and a stockout hurts rank. This prepares the bid cuts and pauses, and the matching restart list.

What to read: Days of stock cover per product, and the ad campaigns and keywords promoting each product
What to give me: Ad pauses and bid cuts for products that will run out before new stock lands, and the restart list for when it does

Synthesis tools to use:
- `amazon_metric metric=days_of_cover status=CRITICAL limit=40`
- `amazon_metric metric=inventory_position limit=60`
- `amazon_metric metric=ppc_keyword_bids days=30 min_clicks=1 limit=200`
- `export_xlsx`

Steps:
1. Call `amazon_metric metric=days_of_cover status=CRITICAL limit=40`.
2. Call `amazon_metric metric=inventory_position limit=60`. Keep products whose inbound will not be checked in before stock runs out.
3. Call `amazon_metric metric=ppc_keyword_bids days=30 min_clicks=1 limit=200` and keep keywords and targets that advertise those products.
4. Prepare changes: cut non-branded bids 60%, keep branded at a floor, pause Display. Write a restart tab with the original bids.
5. Build `stockout_ad_changes.xlsx` with `export_xlsx`.

Checks before answering:
- Stock is Amazon's live count, refreshed when asked. Quote Amazon's update time, and name any product the answer left out because its numbers did not add up. If the answer flags the pull as stale, a product can show as running out that was restocked.
- Shared campaigns advertise several products. Change only the targets for the product running out.
- Keep the original bids in the file. Without them the restart is guesswork.

Output:
- One line: products at risk, daily spend affected, and days of stock gained.
- The spreadsheet with a changes tab and a restart tab.

Never:
- Never push changes to the ads account. With access, each change still waits for a person's approval.
- Never cut branded defense to zero.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-pause-ads-on-stockout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Synthesis reads the ads account but cannot write to it. Applying the pauses needs write access to the Amazon Ads account, which is not granted. Today a person uploads the prepared file. Do the parts you can and say plainly what is missing.
