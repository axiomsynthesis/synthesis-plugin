---
name: writing-it-up
description: >-
  Load when writing the final answer, a report, a dashboard, a chart, a deck, a spreadsheet or any file to send, brand copy and recurring brand outputs, or a landing page, a static or video ad, social post, banner or email in the brand's own look and voice.
---

# Writing it up

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

**Working for an agency?** Call `brand_kit` first. When it answers `source: agency`, everything the client reads from the agency (report, deck, recap page, chart, email to the client) wears the AGENCY's look from that answer and signs "Prepared by" its `prepared_by` name, with "Powered by Synthesis" small in the footer only; never the client brand's colours, type or logo. An ad, landing page or shopper email the client publishes as itself uses `client_kit` from that answer instead. `source: unknown`: call it again before making anything.

| Page | Open it when |
|---|---|
| `pages/compose-the-founder-answer/PAGE.md` | When writing any final answer, report narrative, deck commentary, alert, table header or gap message that a founder, operator or marketer at your brand will read: "what should I do about this", "write up what happened this… |
| `pages/report-chart-laws/PAGE.md` | Before drawing any chart in a report, deck, artifact or answer: bars, stacked bars, lines, small multiples, funnels, year-over-year overlays, rival lines, stat tiles ("chart our sales by week", "show new vs repeat buyers", "plot… |
| `pages/deliverable-scope-no-substitute/PAGE.md` | When you ask for an export, deck, P&L, spreadsheet or report for a month, basis, channel or season whose data is missing or incomplete: "export June's P&L" before June is closed, "build me the board deck for last month", "compare… |
| `pages/exports-and-deliverables/PAGE.md` | Before turning an answer into a file someone can forward — a PDF, a Word memo, a slide deck, a spreadsheet, a dashboard or a one-call framework deck ("send me that as a PDF", "build the board deck", "export the P&L to Excel",… |
| `pages/brand-assets-and-recurring-outputs/PAGE.md` | Before producing the weekly report as a file, a creative or listing brief, a brand kit drafted off your website, a brand-voice score, or before quoting anything from the object map ("send me this week's report", "write me a brief… |
| `pages/brand-content/PAGE.md` | When asked to make something a customer will see: a landing page, a product page, an ad or social post, a banner, an email, a one-pager or a pitch deck ("build a landing page for the new serum", "make three Instagram posts for… |
| `pages/creative/PAGE.md` | When asked which ad hooks or angles are making money, what ads to make next, for new ad concepts built on what already sells, or for the full Synthesis Creative run ("which hooks are working", "what should our next five ads be",… |
| `pages/ad-studio/PAGE.md` | When asked to make paid social ads: Meta or Instagram statics, short vertical videos, a batch of new ad concepts, or "make ads for this landing page" ("make five statics for the protein bar page", "turn our best video into three… |
| `pages/ad-hooks/PAGE.md` | When writing the headline or opening line of an ad: a static's big words, the first text card of a short video, or the first line of primary text ("write hooks for the new serum ads", "give me ten angles for Meta", "why do our… |
| `pages/static-ad-layouts/PAGE.md` | When building a static image ad for Meta or Instagram ("make a static for this hook", "lay out five statics", "make the 9:16 version", "is this ad well composed"). |
| `pages/ad-image-prompts/PAGE.md` | When an ad needs an AI-made picture: a background, a scene, a texture, a prop or an illustration ("make a bathroom-counter background for the tube", "we need a cross-section illustration of how it works", "give me a dark blue… |
| `pages/short-video-ads/PAGE.md` | When making a short vertical video ad of about 5 to 10 seconds with text over it, including ones with an AI-made person reacting to or handling the product ("make a 7-second video like our best one", "an AI girl looking surprised… |
| `pages/ad-preflight/PAGE.md` | Before any ad leaves your hands: a static, a short video or a batch going into an upload pack ("check these ads before we publish", "is this ad safe to run", "why did Meta reject this"). |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.
