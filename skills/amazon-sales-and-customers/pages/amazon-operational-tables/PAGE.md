---
name: ssi-amazon-operational-tables
description: >
  Load before answering anything about your Amazon stock, returns, reimbursements, promotions,
  reviews, suppressed listings, buyer email, order-status quality, US state mix, month-of-year
  seasonality or settled daily revenue, and before writing SQL against any raw Amazon table
  ("are we about to stock out", "what did Amazon pay back", "why are returns up", "what do
  reviews say", "is this month really down"). These tables are snapshots, restating feeds and
  a few deliberate empties, and several read as a confident zero when the truth is that the
  pull failed, the window is short or your account never had that feed.
---

# Amazon operational tables, read correctly

## Open this page when

- Any FBA stock, cover, restock, reserved-unit, inventory-age or reimbursement question.
- Any Amazon returns, return-reason or refund-driver question.
- Any Amazon review, review-topic or competitor-review-language question.
- Any Amazon promotion, coupon-depth, state-level or month-of-year seasonality question.
- Any "is our Amazon order data trustworthy" question (Pending share, suppressed listings,
  buyer-email coverage).
- Before any `run_sql` against a table named in the coverage list below.
- For Amazon profit, ads or search terms, load the Amazon P&L, advertising and search skills.
  This one covers the operational feeds underneath them.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-operational-tables`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric` · `return_rate` · `competitor_review_voice` · `shelf_history` · `warehouse_freshness` · `describe_schema` · `run_sql`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
