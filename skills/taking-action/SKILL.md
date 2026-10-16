---
name: taking-action
description: >-
  Load when the brand wants to change something rather than read it: block wasted ad searches, raise a capped budget, rewrite a listing, build a reorder sheet, tag lapsed customers. Hands over an exact change list the brand applies itself, in the platform or via its own Claude, one approved change at a time. Synthesis never changes an account.
---

# Taking action

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/change-list-standard/PAGE.md` | Whenever a finding is about to become a list of changes for the brand to make itself: "give me the negatives to add", "which ads should I pause", "make me the bulk file", "turn this into something I can upload", "what exactly do… |
| `pages/amazon-block-wasted-searches/PAGE.md` | When you want to turn wasted Amazon ad searches into a list of negative keywords you can upload yourself ("which searches should I block", "give me the negatives to add", "make me a bulksheet of negative keywords", "stop paying… |
| `pages/amazon-budget-release/PAGE.md` | When an Amazon ad campaign keeps running out of daily budget and you want to know whether to raise it, and by how much ("which campaigns are budget capped", "should I raise my budgets", "my campaigns run out of money by… |
| `pages/amazon-listing-rewrite/PAGE.md` | When you want new words for an Amazon listing, not just a score: "rewrite my title", "write me five better bullets", "fix the gaps the listing audit found", "our description is empty, write one", "make our listing as complete as… |
| `pages/amazon-reorder-sheet/PAGE.md` | When you want a reorder list you can send to a supplier, not just a stock warning: "what should I reorder and how much", "build me a PO sheet", "which products do I need to order this week", "give me reorder quantities for 90… |
| `pages/shopify-winback-tags/PAGE.md` | When you want to act on lapsed website customers: "who should we win back", "give me a list of lapsed repeat buyers to tag", "build a win-back segment for Klaviyo", "tag customers who haven't ordered in six months", "export the… |
| `pages/did-it-land/PAGE.md` | After the brand has applied a change list and wants to know whether it took effect ("did my negatives land", "did the bid cuts go through", "check the upload worked", "are those keywords paused now", "did the new exact keywords… |
| `pages/amazon-pause-losers/PAGE.md` | When you want to stop ads that keep losing money ("which campaigns should I pause", "what ad groups are losing money", "which keywords should I turn off", "kill the losers", "which Meta ads should I pause", "make me a file to… |
| `pages/amazon-bid-trim/PAGE.md` | When you want a list of Amazon keyword bids to bring down, ready to upload yourself ("which bids are too high", "trim my keyword bids", "what should each bid be", "make me a bulksheet of bid changes", "which keywords are losing… |
| `pages/amazon-harvest/PAGE.md` | When you want to give Amazon searches that already sell their own exact-match keywords, as a list you upload yourself ("harvest my winning search terms", "which searches should become exact keywords", "promote converting searches… |
| `pages/google-block-wasted-searches/PAGE.md` | When you want to turn wasted Google Ads searches into negative keywords you add yourself ("which Google searches should I block", "give me negatives for Google Ads", "stop paying Google for searches that never convert", "make me… |
| `pages/apply-a-change-in-the-browser/PAGE.md` | When the brand wants its own Claude to make the changes on a Synthesis change list, in the brand's own browser and signed in as the brand: "apply this for me", "make these changes", "go pause those ads", "add the negatives in the… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
