---
name: finance-and-supply
description: >-
  Load for the P&L, accounting, margins, unit economics, product cost, cash, inventory planning, suppliers, an outside finance pack, or whether the business is ready to sell.
---

# Finance, costs and supply

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/netsuite-finance-detail/PAGE.md` | Before quoting any accounting-ledger (NetSuite) figure below the top line: supplier spend, operating cost by category, discounts and refunds given back, revenue by product family, receivables ageing, refund rate, the gross-to-net… |
| `pages/netsuite-pnl-reading/PAGE.md` | For any company-level P&L, gross margin, EBITDA, net income, operating cost, year-over-year, channel mix, receivables, supplier spend, working capital or runway question from your accounting ledger (NetSuite) or the monthly P&L… |
| `pages/financial-package-audit/PAGE.md` | When you are handed another company's own finance pack (P&L workbooks, a financial model, a cash or health model, a data-room export) and need to know whether the numbers are real, want the P&L rebuilt, or are deciding whether to… |
| `pages/unit-economics-and-margin-grounding/PAGE.md` | Before quoting any margin, contribution, CM1/CM2/CM3, gross-margin percent or "is this product profitable", before a pricing call ("can we afford to drop the price?"), and before feeding a margin into a scenario, a valuation or a… |
| `pages/product-cost-resolution/PAGE.md` | For any margin, contribution, profit-after-ads or unit-economics answer, when you have just entered or changed a product cost, when a cost looks wrong or shows $0, or when a product looks unusually profitable or unprofitable… |
| `pages/archetype-economics-models/PAGE.md` | Before answering a lifetime value, retention, repeat, payback, first-order margin or acquisition-cost question where how often people rebuy decides what "good" means ("is our repeat rate bad", "why is retention so low", "can we… |
| `pages/inventory-and-supply-planning/PAGE.md` | When the question is HOW MUCH to order and WHEN to place the order: "how many units do I reorder", "what is my reorder point", "how much safety stock", "what cover should this product be held at", "are we going to make Q4", "is… |
| `pages/supply-chain-and-cash-cycle/PAGE.md` | Before scoring or ranking a supplier, choosing between Amazon fulfilment and a third-party warehouse, or quoting a cash conversion cycle ("is this supplier any good", "rank my suppliers", "should we move to a 3PL", "how long is… |
| `pages/exit-readiness-review/PAGE.md` | When you ask whether the business is ready to sell or raise, what a buyer or banker would say about it, how it scores against an exit or acquisition checklist, what to fix before going to market, or what the company might be… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
