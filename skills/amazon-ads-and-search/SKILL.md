---
name: amazon-ads-and-search
description: >-
  Load for Amazon ad spend, ACoS, TACoS, ROAS, when an ad figure disagrees with the console, search terms, negatives, keyword gaps, search share, rivals on a search, branded searches, outside traffic sold on Amazon, Amazon DSP, or AMC.
---

# Amazon ads and search

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/amazon-ads-data-reading/PAGE.md` | Before quoting any Amazon ad spend, attributed sales, ACoS, TACoS or ROAS figure, comparing two ad weeks, or reconciling your ad numbers to an agency report or the Amazon ad console ("what is my ACoS", "why did ad sales drop this… |
| `pages/amazon-ppc-decisions/PAGE.md` | When deciding what to change in Amazon ads: which search terms waste money, what to negate or harvest, whether ACoS is too high, how to split budget, whether ads grow the business, or whether to cut a product's ads ("what should… |
| `pages/amazon-ppc-diagnostics/PAGE.md` | Before diagnosing WHERE your Amazon ad money goes and why a PPC number moved: placement splits, keyword and match-type detail, branded versus non-branded, day-of-week pattern, paid versus organic share, halo onto other products,… |
| `pages/amazon-search-share-sqp/PAGE.md` | For any Amazon impression, click or purchase share question, keyword performance, search funnel gap, head vs tail terms, or any Amazon demand, visibility or acquisition conclusion ("what share of searches do we get for this… |
| `pages/amazon-search-rivals-and-keyword-gaps/PAGE.md` | When you ask who is winning a search term on Amazon, which competitors take your clicks, which searches you do not show up on, or which keyword opportunities to pursue ("who is beating us on this search", "who are our real… |
| `pages/amazon-search-and-competitors/PAGE.md` | Before quoting any Amazon search share, keyword, share-of-search, branded versus non-branded, competitor product, rival click share or search-gap figure ("who is beating us on search", "what is our share of search", "which… |
| `pages/brand-search-and-own-name/PAGE.md` | For branded search volume, "are more people searching our name", brand awareness, "did the TV spots or the influencer push lift searches for us", the halo of outside marketing on Amazon search, a branded vs non-branded split on… |
| `pages/amazon-offsite-attribution/PAGE.md` | When asked what Instagram, Meta, TikTok, Google, email, creators or affiliates sold on Amazon, whether to renew an influencer or affiliate, why off-Amazon traffic "stopped converting", how much of the Amazon business comes from… |
| `pages/amazon-dsp-and-amc/PAGE.md` | For Amazon DSP (programmatic display, video, streaming TV, Fire TV, off-Amazon display bought through Amazon) and Amazon Marketing Cloud (AMC) questions: DSP spend, ROAS, line items, creatives, audiences, whether DSP brings new… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
