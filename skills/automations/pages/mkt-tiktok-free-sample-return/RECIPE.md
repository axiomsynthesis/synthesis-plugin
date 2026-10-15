# Which TikTok free samples turned into sales?

Channel: TikTok Shop · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which TikTok free samples turned into sales?" (id: mkt-tiktok-free-sample-return, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Free samples are often a quarter of a TikTok Shop's orders. This checks which samples turned into selling videos and which were given away for nothing.

What to read: Free sample orders sent to each creator, their product cost, and the sales each creator's videos drove afterwards
What to give me: Creators who turned free samples into sales, those who never posted, and the sample spend to cut

Synthesis tools to use:
- `tiktok_metric metric=shop_sales_trend months=6`
- `tiktok_metric metric=shop_video_performance days=120 limit=100`
- `operator_inputs section=cogs`

Steps:
1. Call `tiktok_metric metric=shop_sales_trend months=6` for sample order counts per month, reported apart from sales.
2. Call `operator_inputs section=cogs` and cost the samples at product cost.
3. Call `tiktok_metric metric=shop_video_performance days=120 limit=100` for sales per creator.
4. Once sample orders carry the creator: match samples to creators, and split creators into posted and sold, posted no sales, never posted.

Checks before answering:
- Samples are excluded from sales figures. Never count them as sales.
- Video data covers 120 days at most. Match sample windows to it.
- Until the per-creator join exists, report only totals: sample count, sample cost, creator sales. Never name a creator as never posted.

Output:
- Three lines: samples sent, their cost, creator sales in the same window.
- When built: a table of creator, samples, videos, sales, sales per sample dollar.

Never:
- Never message creators.
- Never treat a sample as a sale.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-free-sample-return". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Free sample orders are counted per month but not tied to the creator who received them. Needs sample orders joined to the creator's handle before sample return can be read per creator. Do the parts you can and say plainly what is missing.
