---
name: ssi-product-display-names
description: >
  Load whenever a table, chart label, legend or sentence is about to name one of your
  products, or when a draft shows a bare item code, a name cut off with "…", a note such as
  "(top seller)" inside a name, or two rows with the same label ("make this table readable",
  "put product names on the chart", "what is B0... called"). Product names are derived from
  the marketplace listing title by one fixed rule, with your curated product family list as
  the fallback. For which product a name refers to, load ssi-product-identity-resolution.
---

# Product display names

## Open this page when

- You are about to write a product into a table, a chart label, a legend or a sentence.
- A draft contains a bare item code, a name ending in "…", or a note like "(hero SKU)"
  inside a product name.
- Two rows or two bars in the same view show the same product name.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `product-display-names`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`find_product` · `amazon_metric`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
