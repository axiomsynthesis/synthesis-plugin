---
name: ssi-meta-ad-build-and-publish
description: >
  Load when someone is about to build, load or publish Meta ads, by hand in Ads Manager or
  from a creator platform ("load these creator videos", "put the new videos in the test
  campaign", "copy the winners into the main campaign", "set up a test for these 40 ads",
  "why won't this ad publish", "should we use a cost cap", "move this ad to the other
  campaign"). The order that works: sort every video by the product it shows, build one
  clean ad and copy it, switch off what Meta turns on by itself, publish only your own
  drafts, check every ad is really on, then read and scale against the brand's own lines.
---

# Build and publish Meta ads without losing the sale

## Open this page when

- Before loading a batch of creator videos or statics into Meta.
- Before copying winners into a scaling campaign, or moving ads between campaigns.
- When Ads Manager refuses to publish, or a new ad set spends nothing.
- When choosing a test structure, a budget per test, or a bidding type.
- After publishing: load `ad-launch-check` to check every new ad, one by one.

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `meta-ad-build-and-publish`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`trybe_creator_program` · `ad_health_check` · `meta_metric` · `ad_idea_bank`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
