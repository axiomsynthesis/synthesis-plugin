---
name: ssi-ad-launch-check
description: >
  Load when someone has just launched or is building Meta ads and wants each ad's SETUP
  checked ("are these ads set up right", "check the ads I just launched", "double-check
  my new ads", "did I send this video to the right page", "check this ad before it
  spends", or while working in Ads Manager in the browser). One server call checks each
  ad one by one: the video and the page sell the same product, the page opens, tracking
  and creator tags, naming, placements, Meta's automatic changes and discounts, ad, ad
  set and campaign all switched on, end dates, duplicate videos, cost per sale against
  the keep line, and Amazon-bound links. Not for an account-wide audit: that is the ad
  health check without `ads`.
---

# The ad launch check

## Open this page when

- Right after ads are launched or copied into a new campaign or ad set.
- While someone builds ads in Meta Ads Manager, especially with a browser open.
- When a new ad set spends nothing, or a new batch underperforms on day one.
- Not for "is my ad account healthy": call the same tool without `ads`.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `ad-launch-check`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`ad_health_check`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
