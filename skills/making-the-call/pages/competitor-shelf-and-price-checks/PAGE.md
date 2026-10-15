---
name: ssi-competitor-shelf-and-price-checks
description: >
  Load before any live look at a competitor's Amazon listing, a keyword's search shelf, a
  Walmart.com shelf or a price across retailers ("what is the competitor charging now",
  "who ranks for this search", "where else is this sold and at what price", "is our price
  out of line", "who is undercutting us"). These four tools spend a limited monthly
  allowance of live searches that your weekly shelf history also depends on, so they are
  ask-first and never a loop. It also stops a scraped price being quoted as one of your
  measured numbers, and stops a missing price being read as a stockout.
---

# Competitor shelf and price checks

## Open this page when

- Any live competitor price, rating, review count, best-sellers rank or availability.
- "Who ranks for this keyword", "what does the shelf look like", "who is cheaper".
- Any price-across-retailers question, or any Walmart.com shelf read.
- Before anything that would spend live searches in bulk: a loop over a product list, a
  watchlist or a keyword list. Especially then.
- For search share, click share or keyword gaps from Amazon's own reports, load
  ssi-amazon-search-share-sqp or ssi-amazon-search-rivals-and-keyword-gaps instead. Those
  are measured and free. Scraping is the last resort, not the first.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `competitor-shelf-and-price-checks`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`scrape_amazon_product` · `scrape_amazon_search` · `scrape_walmart` · `scrape_google_shopping` · `shelf_history`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
