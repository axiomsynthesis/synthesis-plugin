# A rival cut price. Match it or hold?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "A rival cut price. Match it or hold?" (id: mkt-amazon-rival-price-cut-response, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns a rival price-cut alert into a decision. Most cuts are short promotions and matching them burns profit for nothing.

What to read: Rival price cuts from the daily shelf watch, your sales rank and units since, and your profit per unit
What to give me: Match, meet halfway or hold after a rival's price cut, based on whether it is actually costing you sales yet

Synthesis tools to use:
- `amazon_metric metric=shelf_position days=30 limit=30`
- `amazon_metric metric=velocity_momentum weeks=8 limit=30`
- `amazon_metric metric=contribution_by_asin months=3`
- `classify_competitor_move new_channel=false`

Steps:
1. Call `amazon_metric metric=shelf_position days=30 limit=30` for the cut size, date and rival.
2. Call `amazon_metric metric=velocity_momentum weeks=8 limit=30` for your units on the affected product since the cut.
3. Call `classify_competitor_move` with the cut size, whether it targets your core product and how many days it has lasted.
4. Call `amazon_metric metric=contribution_by_asin months=3`. Cost of matching = units x price drop.
5. Decide: hold (no damage yet), partial match (damage, cut is lasting), or full match (losing rank fast on a core product).

Checks before answering:
- Judge rank over the window, not one day.
- Rival rows need the watchlist set up. Say so if none show.
- Scraped prices are third-party data. Label them.

Output:
- One line: hold, partial or match, and the profit cost of matching.
- Three lines of evidence: the cut, your units since, the rival's history.
- The date to recheck.

Never:
- Never change your price.
- Never start a price war over a cut under 7 days old without evidence of damage.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-rival-price-cut-response". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
