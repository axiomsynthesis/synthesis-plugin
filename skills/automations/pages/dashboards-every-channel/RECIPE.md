# A dashboard for every channel

Channel: Dashboards · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "A dashboard for every channel" (id: dashboards-every-channel, Dashboards).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the same kind of page as the Amazon dashboard for each other connected channel: Meta, email, TikTok Shop, website and retail. One page per channel.

What to read: Each connected channel
What to give me: One page per connected channel, with tiles, trend charts and flags

Synthesis tools to use:
- `meta_metric metric=weekly_trend`
- `klaviyo_metric metric=channel_monthly`
- `tiktok_metric metric=shop_sales_trend`
- `shopify_metric metric=weekly_revenue`
- `emit_chart`

Steps:
1. Check which channels are connected and skip any that are not.
2. Meta: call `meta_metric` with `metric=weekly_trend` and `weeks=13`.
3. Email: call `klaviyo_metric` with `metric=channel_monthly` and `months=6`.
4. TikTok Shop: call `tiktok_metric` with `metric=shop_sales_trend` and `months=6`.
5. Website: call `shopify_metric` with `metric=weekly_revenue` and `weeks=13`. Call `emit_chart` per trend and write one HTML page per channel. If you can save files here, save them and tell me their names. If not, show them in full.

Checks before answering:
- A channel with no connection gets no page. A channel whose read fails gets a page that says so.
- Trends stop at the last closed day.
- Never add channels together on one page. Each has its own definition of sales.

Output:
- One HTML page per channel, named like meta-dashboard.html, with tiles, trend charts and flags.

Never:
- Never change a campaign or setting in any account.
- Never fill a missing tile with a guess.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: dashboards-every-channel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The Amazon page is done. Each other channel needs the same build, one at a time, starting with Meta and then website orders. Do the parts you can and say plainly what is missing.
