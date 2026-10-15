---
name: ssi-shopify-traffic-and-conversion
description: >
  Load for website sessions, conversion rate, traffic source, UTM tags, landing pages or SEO
  on a Shopify store. Situations: "how many visits did the site get", "what is our conversion
  rate", "why did the site convert worse this week", "where does our traffic come from", "is
  Instagram or email sending anyone", "did the SEO changes work", "did the campaign bring
  people to the site", "our agency deck says a different conversion rate". Keeps sessions on
  the shop's own clock, builds rates from counts, and names the traps: the in-flight day, a
  real zero, and broken ad tags relabelled as direct.
---

# Read Shopify sessions, conversion and traffic source

## Open this page when

- "How many visits did the site get?" "What is our conversion rate?" "Why did the site
  convert worse this week?"
- "Where does our traffic come from?" "Is Instagram, email or Google sending anyone?" Any
  question about UTM tags (the source and medium labels added to an ad or email link),
  referrers or landing pages.
- "Did the SEO changes work?" "Did the campaign bring people to the site?"
- A deck, dashboard or agency quotes a sessions or conversion figure that differs from ours.

Not for order revenue or order counts. Those come from the order tables and are cut in UTC
days (see "Like for like").

## Fetch the method before you answer

This page is a pointer. The method it stands for — the order to work in,
the traps, the exact argument for each call — is held on the server and
served to your brand. Do not answer from this page alone.

**Server tool:** `get_skill`
Call with: `name`
Pass `name` as `shopify-traffic-and-conversion`. The `doctrine` field of the result is this page's
full method. Read it, then follow it. If the method names a tool you cannot
find, the result's `tool_reach` field says which tool to call instead.

Pull one page per call, and only the page the question needs. A connection
may pull 12 different pages in a conversation and 25 in a day; the result's
`pulls` field says where you stand against both. If the pull is refused, say
so in your answer and do not present a method you were not given.

## The server tools this subject uses

`describe_schema` · `run_sql` · `shopify_metric` · `funnel_decomposition` · `ga4_metric` · `search_console_organic` · `propose_brand_fact`

Names only. Do not guess an argument from this list — the method above
gives each call its shape.

## When the method names another page

Fetch that one the same way: `get_skill` with its name. The `ssi-` prefix
is optional, and underscores work as well as hyphens. Calling it with no
name at all returns every page name there is.
