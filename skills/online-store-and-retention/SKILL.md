---
name: online-store-and-retention
description: >-
  Load for Shopify or TikTok Shop sales, site traffic and conversion, email and SMS, subscriptions, support tickets, customer lifetime value, cohorts, retention, cross-sell, offers, bundles and customer or product mix.
---

# Online store, subscriptions and retention

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/shopify-orders-and-revenue/PAGE.md` | Before quoting any Shopify or website revenue, order count, average order value, discount, refund or product figure, and before writing SQL on Shopify order tables. |
| `pages/shopify-summary-tables/PAGE.md` | Before reading any prebuilt Shopify summary: channel mix, subscription mix, order tags, new vs returning orders, the per-customer lifetime table, revenue concentration, winback candidates, country revenue, weekly revenue,… |
| `pages/shopify-traffic-and-conversion/PAGE.md` | For website sessions, conversion rate, traffic source, UTM tags, landing pages or SEO on a Shopify store. |
| `pages/dtc-unit-economics-and-funnel/PAGE.md` | For the website margin ladder (CM1, CM2, CM3) and the site funnel. |
| `pages/dtc-and-creator-leftovers/PAGE.md` | When you ask how many customers came back to your website, what share of web revenue is repeat, how long people take to order again, what your subscription revenue or run-rate is on Skio, where site traffic comes from or which… |
| `pages/klaviyo-email-and-sms/PAGE.md` | Before you quote any email or SMS figure from Klaviyo: campaign or flow revenue, open rate, click rate, bounce or spam rate, which subject lines work, the best time to send, template performance, or "how much of our revenue does… |
| `pages/recharge-subscriptions/PAGE.md` | For Recharge subscription questions on your web store: "how many subscribers do we have", "what is our MRR", "is churn going up", "why do subscribers cancel", "what is our skip rate", "how much churn is failed payments", "what… |
| `pages/gorgias-customer-service/PAGE.md` | Before you quote any customer-service figure from Gorgias: ticket volume, why customers write in, channel mix, time to close or one-touch rate, agent load, or how many customers have ever contacted support ("are support tickets… |
| `pages/cohort-ltv-and-retention/PAGE.md` | For any LTV, cohort, retention curve, payback, "what is a customer worth", young-product repeat or cohort grid question on Amazon, Shopify, Recharge or Skio ("what is our 90-day LTV", "are newer customers worse than older ones",… |
| `pages/cross-sell-and-bundles/PAGE.md` | For cross-sell, attach, bundle and upgrade questions: "do buyers of A buy B", "what do our buyers buy next", "which product is the front door", "should we bundle these two", "why didn't the bundle sell", "how do I get A buyers to… |
| `pages/customer-and-product-mix/PAGE.md` | Before answering who the customers are and what actually sells: value segments, which states the money comes from, which products carry the window, who to win back, how to lift order value, and which products to keep or cut… |
| `pages/tiktok-shop-sales-and-payouts/PAGE.md` | For any TikTok Shop question: "how is TikTok Shop doing", "what did we sell on TikTok last month", "which products sell on TikTok", "what did TikTok actually pay us", "why is the payout so far below sales", "did TikTok raise its… |
| `pages/landing-page-go-live/PAGE.md` | When someone wants a new or changed landing page for paid traffic on a Shopify store ("build a page for these ads", "make a version of our best page with the bigger pack", "push this page live", "is the new page live", "the price… |
| `pages/store-test-readout/PAGE.md` | When planning or reading a test on an online store: a page against a page, a pre-picked pack, a price, an add-on box, free shipping, or a copy change ("set up an A/B test for the 4-pack", "who is winning the page test", "can we… |
| `pages/offers-upsells-and-discounts/PAGE.md` | When setting or changing what a website order contains or costs: pack sizes and pack prices, free shipping lines, an add-on box, an after-payment upsell, free gifts with bigger packs, or discount codes ("should we add a 6-pack",… |
| `pages/email-flow-go-live/PAGE.md` | When building, fixing or switching on an automated email flow in Klaviyo or the store ("set up an after-purchase series", "our abandoned checkout emails make nothing", "turn the new flow on", "is the welcome flow sending",… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
