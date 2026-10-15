---
name: ssi-market-size-and-rivals
description: >
  Load before answering how big your market is, what share you hold, how crowded the category
  is, what a competitor's price cut or new channel means, what protects you from a copycat or an
  Amazon own-brand, or what the business might be worth if you sold it: "how big is this
  category", "what share do we have", "should we respond to their price drop", "what is our
  moat", "what would we sell for". Every tool here computes on numbers you type in and none of
  them reads your data, so the answer looks measured and is only as good as its inputs. Says
  where each input must come from and which defaults quietly invent one.
---

# Market size, rivals and what the business is worth

## Open this page when

- Category size, TAM, SAM, SOM, addressable market, "how big could this get".
- Your market share, share tier, where you sit against the category's growth.
- How concentrated or fragmented the category is, how many players matter.
- A competitor cut price, entered a channel, or copied you, and you want to know how to
  respond.
- Moat, defensibility, private-label or Amazon own-brand threat.
- Why customers choose you, and whether that reason is fragile.
- Valuation, exit readiness, "what would a buyer pay", due-diligence prep.
- For your search share against named rivals on Amazon, load **ssi-amazon-search-share-sqp**
  and **ssi-amazon-search-rivals-and-keyword-gaps** first. Those are measured. These tools are
  not.
- For live shelf prices or a rival's listing, load **ssi-competitor-shelf-and-price-checks**.
  Those reads spend a limited outside allowance, so ask first.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `market-size-and-rivals`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`size_market` · `estimate_market_share` · `market_posture` · `classify_competitor_move` · `classify_moat` · `private_label_threat` · `win_loss_analysis` · `valuation_and_exit_readiness`
`strategy_framework`, with `framework` set to: `hhi`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `framework` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`hhi` means `strategy_framework` with `framework` set to `hhi`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
