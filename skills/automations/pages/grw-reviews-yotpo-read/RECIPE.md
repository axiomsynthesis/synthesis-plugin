# What your website reviews say

Channel: Customers · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What your website reviews say" (id: grw-reviews-yotpo-read, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads the reviews customers leave on your own website, by product and month. It finds rating drops and the words behind them. The connector exists but has no data and no reading tool yet.

What to read: Yotpo or other website reviews, ratings and text by product
What to give me: Rating trend, top praise and top complaints by product on your own site

Synthesis tools to use:
- `review_themes`

Steps:
1. When a reader exists: pull reviews by product and month with rating and text.
2. Run `review_themes reviews=[...]` on each product's last 90 days.
3. Compare rating and themes against the 90 days before.

Checks before answering:
- An empty review table means not connected, never zero reviews.
- Review themes are a starting map, not a precise analysis. Say so.

Output:
- Table: product, reviews, average rating now and before, top praise, top complaint.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-reviews-yotpo-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The Yotpo connector exists but holds no rows and no governed reading tool exists. A sync and a reader are needed. Do the parts you can and say plainly what is missing.
