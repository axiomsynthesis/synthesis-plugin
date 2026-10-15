# Where shoppers leave your site

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where shoppers leave your site" (id: website-site-conversion-read, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows where shoppers leave your site, from first visit to purchase, split by phone or computer and by where they came from. It names the one step that loses the most money.

What to read: GA4, Shopify
What to give me: The step from visit to purchase that loses the most, by phone or computer and by source, and its cost

Synthesis tools to use:
- `ga4_metric metric=funnel`
- `ga4_metric metric=devices`
- `ga4_metric metric=traffic_sources`
- `ga4_metric metric=landing_pages`
- `shopify_metric metric=weekly_revenue`

Steps:
1. Call `ga4_metric` with `metric=funnel` and `days=28` for visits, product views, add to cart, checkout and purchase.
2. Call `ga4_metric` with `metric=devices` and `days=28` to split the funnel by phone, computer and tablet.
3. Call `ga4_metric` with `metric=traffic_sources` and `days=28` to see which sources convert and which only bring visits.
4. Call `ga4_metric` with `metric=landing_pages`, `days=28` and `limit=20` to find pages with many visits and few sales.
5. Check GA4 purchases against `shopify_metric` with `metric=weekly_revenue` for the same 4 weeks, then put a dollar value on the worst step.

Checks before answering:
- If GA4 purchases are far below Shopify orders, say tracking is missing sales before reading any rate.
- Use closed days only. Today is still filling in.
- If a GA4 read is empty or fails, say so. Never show a zero rate.
- A small source with few visits is not a finding. Say how many visits each rate rests on.

Output:
- One line first: the step that loses the most, and its cost a month.
- A table: step, phone rate, computer rate, gap, dollars a month.
- One move and how we will know it worked in four weeks.

Never:
- Never change the site or its settings. A person does that.
- Never guess a conversion rate the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-site-conversion-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
