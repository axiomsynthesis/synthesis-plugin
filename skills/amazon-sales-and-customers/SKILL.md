---
name: amazon-sales-and-customers
description: >-
  Load for any Amazon seller or vendor (1P) sales, revenue, fees, settlement, profit, stock, listing, offer, Subscribe and Save, traffic, customer count, repeat or new-product question, when a figure disagrees with Seller Central, and for the weekly Amazon report.
---

# Amazon sales and customers

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/amazon-revenue-basis/PAGE.md` | Before quoting, charting or checking any Amazon revenue, sales, units, average order value, order count, best day or before-and-after figure, or when two screens disagree on Amazon revenue ("what did I sell on Amazon this month",… |
| `pages/amazon-settlement-and-fees/PAGE.md` | For Amazon fee rates, net proceeds, settlement tie-out, per-product contribution, storage fees, reimbursements, fee anomalies or any settlement-basis figure ("what are my Amazon fees", "why did my fee rate jump this month", "what… |
| `pages/amazon-pnl-build/PAGE.md` | When you want an Amazon P&L with Amazon's fees, ad spend and product cost for recent months, a "what are we actually keeping per product" view, or a weekly profit ("what did we make last week, Monday to Sunday"), or when you are… |
| `pages/amazon-profit-tools/PAGE.md` | For Amazon profit, net, contribution after product cost, daily or weekly profit estimates, new versus repeat customer economics, break-even ACoS or ROAS, or plan versus actual ("what did Amazon actually make last month", "are we… |
| `pages/amazon-customer-identity-and-counts/PAGE.md` | Before quoting any Amazon customer count, new vs returning split, orders or revenue per customer, cost per new customer, cohort, repeat, LTV or "bought both" figure, or before planning to match Amazon buyers to Meta, Google,… |
| `pages/amazon-new-repeat-and-product-customers/PAGE.md` | For Amazon questions about new-to-brand customers, returning customers, repeat rate, net active customers, "how many customers bought this product", gateway products, or whether people rebuy the same product ("are we still… |
| `pages/amazon-subscribe-and-save/PAGE.md` | For any Amazon Subscribe and Save question: active subscribers, attach rate, S&S revenue or forecast, never-repeated ("fake") signups, the retention ladder, subscriber vs non-subscriber value, or S&S offer design ("how many… |
| `pages/amazon-offer-structure-deals-and-pricing/PAGE.md` | When your question is about the SHAPE of an Amazon offer rather than one price: a single / 2-pack / 3-pack ladder, price per use, whether a list price moved, how deep a deal really was, whether a bigger pack covers for a sibling… |
| `pages/amazon-listing-and-reviews/PAGE.md` | Before answering anything about your Amazon listing's quality, its main image, its price or rank against rivals, its star rating and review flow, or who buys it ("is our listing worse than theirs", "why did our rating drop", "are… |
| `pages/amazon-new-product-launch-readout/PAGE.md` | When you ask how a new Amazon product or listing is doing ("how is the launch going", "how is the new one selling", "is the new pack working"), when a product you do not recognise appears in a table, or when someone says a… |
| `pages/amazon-traffic-and-conversion/PAGE.md` | When your Amazon sessions, page views, conversion rate, buy box or sales velocity swing, when sessions surge or drop while conversion moves the other way, or when you ask whether a traffic change is real ("sessions tripled this… |
| `pages/amazon-operational-tables/PAGE.md` | Before answering anything about your Amazon stock, returns, reimbursements, promotions, reviews, suppressed listings, buyer email, order-status quality, US state mix, month-of-year seasonality or settled daily revenue, and before… |
| `pages/amazon-weekly-expert-report/PAGE.md` | When you ask about your weekly Amazon report: what a section means ("what is 'who took the clicks'", "is that click-through rate"), why a number looks wrong or looks the same as last week, why a product is flagged for reorder,… |
| `pages/amazon-fba-inventory-and-cover/PAGE.md` | For any Amazon stock, FBA inventory, inbound shipment, stock moving between Amazon warehouses, days of cover, weeks of supply, stockout risk, reorder, restock, excess or dead stock question, or a report's inventory section ("am I… |
| `pages/amazon-vendor-central/PAGE.md` | For any Amazon Vendor Central (1P) question: a brand that sells to Amazon wholesale on purchase orders, where Amazon owns the stock and sets the price ("what did Amazon buy from us", "what is our fill rate", "which POs are open",… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
