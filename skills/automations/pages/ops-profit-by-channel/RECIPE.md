# Which channel actually makes money?

Channel: Money · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which channel actually makes money?" (id: ops-profit-by-channel, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts each sales channel on the same profit ladder so the founder can see where a dollar of sales is worth most. Today only Amazon reaches net. The other channels stop where their cost data stops, and the recipe says exactly where.

What to read: Revenue, channel fees, product cost, shipping and ad spend for Amazon, the website, TikTok Shop and retail
What to give me: Profit after costs and ads for each sales channel, side by side for one month

Synthesis tools to use:
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `net_revenue_dtc month=YYYY-MM`
- `tiktok_metric metric=shop_payouts months=3`
- `netsuite_metric metric=customer_trend months=6 top=20`
- `meta_metric metric=spend month=YYYY-MM`

Steps:
1. Amazon: call `amazon_metric metric=pnl_waterfall month=YYYY-MM`.
2. Website: call `net_revenue_dtc month=YYYY-MM`, product cost from entered costs, and website ad spend from `meta_metric metric=spend month=YYYY-MM` and Google if connected.
3. TikTok Shop: call `tiktok_metric metric=shop_payouts months=3` for what the platform actually paid after its fees.
4. Retail: call `netsuite_metric metric=customer_trend months=6 top=20` for invoiced revenue per retail account.
5. Once the build lands, add card fees, shipping per order and retail trade spend, and end every channel at net.

Checks before answering:
- Each channel stops at the last line with real data. Mark the missing lines "not connected", never zero.
- Ad spend must be assigned to the channel it drives. Meta can drive Amazon sales; say how it was split, or leave it unassigned.
- TikTok Shop orders include free samples. Use payouts, not order totals.
- Use the same month for every channel, and a settled one.

Output:
- Table: Channel | Revenue | Channel fees | Product cost | Shipping | Ads | Profit | Profit % | Lines missing.
- Two lines: the channel with the best measured margin, and what is needed to compare the rest fairly.

Never:
- Never fill missing costs with industry averages.
- Never compare a channel ending at net with one ending at gross profit as if equal.
- Never move budget between channels.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-profit-by-channel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Amazon profit to net is held. The website lacks payment processor fees (Stripe and PayPal have no reader tool) and per-order shipping cost (ShipStation and ShipHero have no reader tool and no rows yet). Retail lacks trade spend and freight per account. Needs those readers before a channel P&L can end at net. Do the parts you can and say plainly what is missing.
