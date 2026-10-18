# Ads that get clicks but not sales

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Ads that get clicks but not sales" (id: grw-meta-click-no-buy, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds ads that win the click and then lose the buyer on the page. It joins each ad's funnel to the link it sends people to and to that page's site behaviour, so the fix lands on the page, not the ad.

What to read: Per-ad funnel from impression to click to cart to purchase, and where each ad points
What to give me: Ads whose landing page is losing the sale, and the page to fix

Synthesis tools to use:
- `cost_rules for=grw-meta-click-no-buy`
- `meta_metric metric=ad_microfunnel limit=30`
- `meta_metric metric=creative_action_breakdown limit=30`
- `meta_metric metric=ad_destinations days=28`
- `ga4_metric metric=landing_pages days=28 limit=30`

Steps:
1. Pull `meta_metric metric=ad_microfunnel limit=30`.
2. Flag ads whose click rate is in the top third but whose click-to-purchase rate is in the bottom third.
3. Pull `meta_metric metric=ad_destinations days=28` and attach each flagged ad's destination link.
4. Pull `ga4_metric metric=landing_pages days=28 limit=30` and match the landing path to read bounce and conversion for that page.
5. Group flagged ads by destination. A page shared by several flagged ads is the fix to make first.

Checks before answering:
- Match by ad id. Strip tracking parameters before matching pages.
- If the destination is an Amazon page, the site funnel cannot see the sale. Say so and drop that ad from the page read.
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.
- GA4 is behaviour only. Never quote its revenue as sales.

Output:
- Answer first. Table with columns destination page, flagged ads, clicks, click-to-purchase rate, page conversion rate, likely fix.
- Under 10 rows.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-click-no-buy". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
