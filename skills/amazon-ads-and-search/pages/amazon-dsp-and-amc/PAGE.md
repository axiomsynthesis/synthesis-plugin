---
name: ssi-amazon-dsp-and-amc
description: >
  Load for Amazon DSP (programmatic display, video, streaming TV, Fire TV, off-Amazon
  display bought through Amazon) and Amazon Marketing Cloud (AMC) questions: DSP spend,
  ROAS, line items, creatives, audiences, whether DSP brings new customers, how Sponsored
  ads and DSP work together, path to purchase, time to conversion, reach and frequency
  ("is DSP worth it", "what does DSP add on top of Sponsored Products", "how many touches
  before someone buys", "are we showing ads too often"). Knows DSP is 14-day
  view-and-click and is never added to Sponsored sales, that AMC drops small rows for
  privacy, and that missing DSP or AMC data is never zero.
---

# Read Amazon DSP and Amazon Marketing Cloud

## Open this page when

- "How is DSP doing?" "Which line items or creatives are working?" "Is DSP worth it?"
- "Does DSP bring new customers?" "What does DSP add on top of Sponsored Products?"
- "How many ads does someone see before buying?" "How long from first ad to purchase?"
- "Are we showing the same people too many ads?"
- For Sponsored Products, Brands and Display, open `ssi-amazon-ads-data-reading` instead.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `amazon-dsp-and-amc`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`amazon_metric`, with `metric` set to: `dsp_performance` · `amc_new_to_brand` · `amc_overlap` · `amc_path_to_purchase` · `amc_reach_frequency`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`amazon_dsp_performance` means `amazon_metric` with `metric` set to `dsp_performance`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
