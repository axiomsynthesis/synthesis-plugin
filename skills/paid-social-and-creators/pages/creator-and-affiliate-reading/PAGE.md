---
name: ssi-creator-and-affiliate-reading
description: >
  Load before answering any creator, affiliate or influencer question (Growi, Trybe,
  Levanta, Cruva, Euka, ShopMy, GRIN): "what did creators sell", "what did the creator
  program cost us", "is it worth it", "which creators should we keep", "why did creator
  sales drop", "are our creators posting", and whenever creator revenue sits next to ads,
  TikTok Shop or Amazon Attribution figures. A zero is often unmeasured, lifetime and dated
  figures never divide, creator sales are a slice of the shop, overlapping sources are
  shown side by side and never summed, and confirmed money leads over reported.
---

# Read creator and affiliate programs

## Open this page when

- "What did creators or affiliates sell?" "What did the creator program cost us?" "Is it worth it?"
- "Which creators should we keep?" "Why did creator sales drop?" "Are our creators posting?"
- Any Levanta question: creator sales on Amazon, commission, the Brand Referral Bonus, net
  creator cost, creator return on cost.
- Any answer that puts creator revenue beside ad revenue, TikTok Shop sales or Amazon
  Attribution sales.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `creator-and-affiliate-reading`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`data_freshness` · `trybe_creator_program` · `cruva_metric` · `tiktok_metric` · `amazon_metric` · `levanta_metric` · `describe_schema` · `run_sql` · `create_ad_links` · `capture_turn`
`growi_metric`, with `metric` set to: `creator_channel_trend` · `creator_payouts` · `top_creators` · `campaign_performance` · `roster_health` · `post_compliance`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

A line that says "with `metric` set to" is ONE tool: call it and pass
the value. The method may name a read by its own name instead:
`growi_creator_channel_trend` means `growi_metric` with `metric` set to `creator_channel_trend`.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
