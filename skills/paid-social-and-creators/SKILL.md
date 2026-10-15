---
name: paid-social-and-creators
description: >-
  Load for Meta, TikTok or Google ad spend, returns, creatives and budgets, creator, affiliate and influencer programs, campaign or event lift, lift on other channels, and "check my ads".
---

# Paid social, search ads and creators

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

| Page | Open it when |
|---|---|
| `pages/meta-ads-reading/PAGE.md` | Before answering any Meta, Facebook or Instagram ads question about spend, ROAS, CPA, creatives, hook or hold rate, placement, device, age and gender, geography, the funnel or ad spend by product, and before adding up raw Meta ad… |
| `pages/meta-amazon-attribution-scoring/PAGE.md` | For any Meta ROI, ROAS, cost per order or "which Meta ads should I cut" question when your Meta ads send shoppers to an Amazon or other marketplace listing, or whenever Meta shows almost no purchases against real spend ("is Meta… |
| `pages/meta-budget-advice/PAGE.md` | When you want advice on Meta ad spend: "what should we do with our Meta budget this week", "should we cut or scale Meta", "where should the money go", "why does the account keep losing money when some ads clearly work", or when… |
| `pages/meta-creative-detail/PAGE.md` | Before answering any Meta (Facebook and Instagram) question about which AD, surface, state, country, age group, gender or device is working ("which creative wins on Reels", "which states waste our spend", "who are we reaching",… |
| `pages/meta-creative-diagnosis/PAGE.md` | When you ask which Meta ads are working, why an ad is failing, whether a creative is tired or worn out, which ads to scale or cut, or how fast to raise budget on a winner ("which of my Meta ads actually work", "is it the hook or… |
| `pages/meta-delivery-and-pacing/PAGE.md` | Before answering anything about how your Meta ads are DELIVERING rather than how the creative looks: daily and weekly spend, campaign and ad set pacing, runaway or stalled spend, reach and frequency, spend concentration, the… |
| `pages/meta-weekly-report/PAGE.md` | When you ask about your weekly Meta ads report: what a section means, why a number looks wrong, whether this week's report can be trusted, how it was built, or when it arrives ("what does the hook section mean", "why is the… |
| `pages/motion-creative-analytics/PAGE.md` | Before answering anything about ad creative from Motion, if your brand has Motion connected: which hook worked, which format holds attention, what a video actually says, what competitors are running, or what Motion's AI tags mean… |
| `pages/tiktok-ads/PAGE.md` | Before quoting any TikTok advertising figure or writing SQL on the TikTok ads tables ("what did we spend on TikTok", "what is our TikTok ROAS", "which TikTok campaign is working", "is our TikTok creative burning out", "who are we… |
| `pages/paid-media-and-acquisition-economics/PAGE.md` | For paid media across more than one channel and for what a new customer costs: "is paid working", "what is my CAC", "what is our MER", "how much does Meta over-report", "can we afford to scale", "what is the most we can pay per… |
| `pages/google-ads-and-web-analytics/PAGE.md` | Before quoting any Google Ads cost, keyword, search-term, Performance Max or impression share figure, any organic search or SEO figure from Search Console, any site sessions or on-site behaviour figure from GA4, or Amazon ad… |
| `pages/creator-and-affiliate-reading/PAGE.md` | Before answering any creator, affiliate or influencer question (Growi, Trybe, Levanta, Cruva, Euka, ShopMy, GRIN): "what did creators sell", "what did the creator program cost us", "is it worth it", "which creators should we… |
| `pages/growi-creator-payouts/PAGE.md` | Before quoting anything about a Growi creator or affiliate channel: what you paid your creators, what a creator earned, who posted, which campaign a creator is enrolled in, or the channel's return ("what do our creators cost",… |
| `pages/cross-channel-halo-and-incrementality/PAGE.md` | When you ask whether Meta, TikTok, creator, influencer or any outside spend lifts Amazon sales, retail sales or branded search: "does TikTok sell our product on Amazon", "is Meta driving Amazon", "is the extra Meta money paying",… |
| `pages/campaign-and-event-lift/PAGE.md` | For "how did the campaign, launch, TV week, promo, billboard, celebrity deal or site change do", "sales jumped this week, was it the campaign", "is this a step change", "did the SEO change bring sales", or any readout over an… |
| `pages/ad-test-and-learn/PAGE.md` | When launching a new batch of ads or reading how one did ("how should we test these statics", "which of the new ads won", "what should the next batch be", "when do we kill an ad"). |
| `pages/ad-health-check/PAGE.md` | When someone wants one verdict across all their ad accounts rather than one platform ("check my ads", "ad health check", "audit my ad accounts", "is my ad spend healthy", "what is wrong with my ads", "run a health check on… |
| `pages/competitor-ad-research/PAGE.md` | When asked what ads rivals or leading brands are running and which of them work ("what statics are the top brands running", "show me our competitors' Meta ads", "what formats are winning in our category"). |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
