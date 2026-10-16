---
name: ssi-quickbooks-books
description: >
  Load for any profit, revenue, expense, cash, balance sheet, receivables, payables,
  customer or vendor question answered from QuickBooks Online, the brand's own books
  ("what did we make last month", "where is the money going", "how much cash do we have",
  "who owes us money", "which bills are late", "how dependent are we on one customer").
  Reads Intuit's own report totals, names the accounting basis, never treats the current
  month as complete, and never adds a channel's sales on top of the books.
---

# Read your QuickBooks books without double counting or false months

## Open this page when

- "What did we make last month?" "What is our net income / gross margin?"
- "Where is the money going?" "Which costs went up?"
- "How much cash do we have?" "What is our working capital?"
- "Who owes us money?" "Which bills are late?" "How much do we owe suppliers?"
- "How dependent are we on one customer or one supplier?"
- Any time a figure from the brand's QuickBooks is about to be quoted.

Not for one channel's own sales or fees (Amazon, Shopify, TikTok Shop): those have their
own tools. For a brand whose books are in NetSuite instead, use `ssi-netsuite-pnl-reading`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `quickbooks-books`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`quickbooks_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
