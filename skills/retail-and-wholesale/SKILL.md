---
name: retail-and-wholesale
description: >-
  Load for Walmart, Target or other store sales, retail weekly files, coupons and promotions in stores, category scorecards and the combined retail summary.
---

# Retail and wholesale

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/walmart-marketplace-reading/PAGE.md` | For questions about your own Walmart Marketplace seller account on walmart.com: "how is Walmart doing", "what did we sell on Walmart last month", "which SKUs sell on Walmart", "why is Walmart so weak", "are our Walmart listings… |
| `pages/walmart-retail-weekly-files/PAGE.md` | When a Walmart store-sales (Retail Link) export or the weekly agency pack arrives, or for any figure from them: velocity, traited stores, finelines, fiscal weeks, OTIF on-time vs in-full, supply plan, ship-to-home, price-change… |
| `pages/target-weekly-pos/PAGE.md` | For any question about your Target store sales or your weekly Target files: "how did Target do last week", "what are we selling per store", "how many stores carry us", "why is Target down on last year", "is that item leaving the… |
| `pages/retail-combined-exec-summary/PAGE.md` | When asked for one weekly summary across two or more retailers ("give me Walmart and Target on one page", "an exec summary of the retail week for our head of sales", "combine the two retail reports", "make this a one-pager for… |
| `pages/retail-coupons-and-promo-calendar/PAGE.md` | For any cash-back app, digital clip coupon or retail offer question: is it working, what is the return on spend, what is break-even, how big should the next offer be, or is an offer live this week ("is iBotta paying for itself",… |
| `pages/retail-store-sales-and-money/PAGE.md` | For any read of your weekly store sales at a retailer (Walmart stores, Target or any account where the retailer buys from you and sells on its own shelf): "how did Walmart do this week", "why is retail down 20% on last year",… |
| `pages/nielsen-category-scorecard/PAGE.md` | For any retail category share, retailer cut, %ACV (share of stores stocking), competitor share, velocity or retail trend question from your Nielsen data or the category scorecard tool: "where do we sit in the category", "what's… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
