# Is marketing spend past the point of paying?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is marketing spend past the point of paying?" (id: ops-marketing-share-of-revenue, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tracks blended revenue per ad dollar across all channels, month by month, against the break-even level your margin allows. It answers "are we spending too much on marketing" with one number and a line you should not cross.

What to read: Total ad spend and revenue by month across channels, and contribution margin before ads
What to give me: Revenue per ad dollar each month against the level where ads stop paying, and the months that crossed it

Synthesis tools to use:
- `mer month=YYYY-MM`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `amazon_metric metric=tacos month=YYYY-MM`
- `attribution_lenses platform_roas=<roas> blended_mer=<mer>`

Steps:
1. For each of the last six closed months call `mer month=YYYY-MM` for revenue, total ad spend and the ratio.
2. Get margin before ads. Use `amazon_metric metric=pnl_waterfall month=YYYY-MM` for Amazon. For the company view use the closed-month gross margin less variable fees if the ledger is connected.
3. Break-even ratio = 1 divided by margin before ads.
4. Call `amazon_metric metric=tacos month=YYYY-MM` to show Amazon's share of the picture.
5. Run `attribution_lenses platform_roas=<roas> blended_mer=<mer>` to show how far platform-reported returns sit from the blended figure.
6. Name the channel whose spend grew fastest against revenue.

Checks before answering:
- Revenue and spend must cover the same channels. Amazon plus website revenue against Amazon plus Meta plus Google spend is fine; leaving out a channel that spends is not.
- A month with missing ad data reads as a great month. Check every spend source has data for every month.
- Use closed months only. The current month's attribution is still moving.
- The break-even line depends on a margin. Say where the margin came from.

Output:
- Table: Month | Revenue | Ad spend | Revenue per ad dollar | Break-even | Above or below.
- Two lines: the trend, and the channel driving it.

Never:
- Never change a budget or bid.
- Never present platform-reported return as incremental.
- Never use a default margin.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-marketing-share-of-revenue". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
