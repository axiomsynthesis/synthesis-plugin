"""Match a person's own words to ready automations. Plain matching, no model.

ONE definition, two places it runs. The server's get_skill search calls it
through catalog.find_automations, and the plugin build copies this file
byte for byte into the plugin's hooks, so the check on every message
(synthesis-plugin/hooks/automation_match.py) gives the same answer for the
same words. So: STDLIB ONLY, and no import from the rest of ssi_api.

Why the plugin needs its own copy (measured 2026-11-03): with the rule written
in the start-of-chat text and on the brand overview, 10 of 10 fresh sessions
read it and 0 of 8 acted on it. A rule a model may skip is not a route. The
hook runs this on the message before Claude sees it, so the match is put in
front of it every time.

A row is a dict: id, title, channel, asked (list), how, shortcut.
"""
from __future__ import annotations

import re

HOW_SAY = {
    "run": "Run it now: call get_skill with this automation as `name`, and open the answer "
           "with one line naming it.",
    "run_once_then_offer": "Run it once now: call get_skill with this automation as `name` and "
                           "`once` true. End by asking in one line if they want it repeated.",
    "ask_first": "Do not start it. Answer what you can, then ask in one line if they want it. "
                 "It changes a live account, so it runs only after a clear yes.",
}
MAYBE_SAY = "Answer normally, then offer this automation by its title in one line."

STOP = frozenset(
    "a about all am an and any are as at be been but by can could did do does for from get give "
    "going got had has have help how i if in into is it its just know let me my need of on or our "
    "please should show so tell than that the their them then there these they this to up us was "
    "we were what when where which who why will with would you your".split())
# Different words for one idea, folded before matching. Longest first, so
# "running out of stock" becomes one idea and not two.
SAME = (
    ("running out of stock", "runout"), ("run out of stock", "runout"), ("ran out of stock", "runout"),
    ("going out of stock", "runout"), ("out of stock", "runout"), ("stock outs", "runout"),
    ("stock out", "runout"), ("stockouts", "runout"), ("stockout", "runout"),
    ("running out", "runout"), ("run out", "runout"), ("runs out", "runout"), ("ran out", "runout"),
    ("selling out", "runout"), ("sell out", "runout"), ("sold out", "runout"),
    ("purchase orders", "reorder"), ("purchase order", "reorder"), ("restocking", "reorder"),
    ("restock", "reorder"), ("replenish", "reorder"), ("reordering", "reorder"),
    ("inventory", "stock"),
    ("haven t bought", "lapsed"), ("havent bought", "lapsed"), ("hasn t bought", "lapsed"),
    ("hasnt bought", "lapsed"), ("not bought", "lapsed"), ("stopped buying", "lapsed"),
    ("stopped ordering", "lapsed"), ("win back", "winback"), ("winbacks", "winback"),
    ("profitable", "profit"), ("making money", "profit"), ("make money", "profit"),
    ("worth it", "worth"), ("complaining", "complain"), ("complaints", "complain"),
    ("complained", "complain"),
)

# One word can be a whole request ("when do we run out?", "what should I reorder?"),
# but only about the future and only about stock or a win-back. "Did we run out in
# May?" is a number, and "which campaigns run out of budget?" is an ads question.
ONE_WORD_JOBS = frozenset({"runout", "reorder", "shipment", "winback", "lapsed"})
NOT_STOCK = frozenset({"budget", "ad", "campaign", "cash", "money", "credit", "time", "ideas"})
PAST = re.compile(r"\b(did|was|were|ran|sold|last|yesterday|ago)\b", re.I)


def tokens(text: str) -> set:
    t = " " + re.sub(r"[^a-z0-9 ]+", " ", str(text or "").lower()) + " "
    t = re.sub(r"\s+", " ", t)
    for said, same in SAME:
        t = t.replace(f" {said} ", f" {same} ")
    out = set()
    for w in t.split():
        if len(w) < 2 or w in STOP:
            continue
        out.add(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w)
    return out


def find(question: str, rows, n: int = 3) -> list[dict]:
    """The automations a plain question fits, best first.

    `fit` is "clear" when every word of one of the job's own `asked` questions is
    in the question, or nearly all of a title of three or more words, and "maybe"
    when most are. A single shared word is no fit at all: "how many units do we
    have?" is a number, not a job, and must get a normal answer. A two-word title
    is never clear on its own: "How is this ad set going?" is {ad, set}, and a
    message that says "ad" and "set up" is not asking about one ad set. Client jobs
    stay out unless the question speaks of a client."""
    said = tokens(question)
    if not said:
        return []
    client = bool(said & {"client", "agency"})
    past = bool(PAST.search(str(question)))
    scored = []
    for r in rows:
        if r.get("channel") == "Agency" and not client:
            continue
        rank, fit = 0.0, ""
        for phrase in r.get("asked") or ():
            want = tokens(phrase)
            share = len(want & said) / len(want) if want else 0
            alone = want <= ONE_WORD_JOBS and not (said & NOT_STOCK) and not past
            if want and share == 1 and (len(want) >= 2 or alone):
                rank, fit = max(rank, 3 + len(want) / 10), "clear"
            elif len(want & said) >= 2 and share >= 0.6 and fit != "clear":
                rank, fit = max(rank, 1 + share), "maybe"
        title = tokens(r.get("title"))
        shared = len(title & said)
        if shared >= 2 and title:
            share = shared / len(title)
            if share >= 0.75 and len(title) >= 3:
                rank, fit = max(rank, 2.5 + share), "clear"
            elif share >= 0.5 and fit != "clear":
                rank, fit = max(rank, 0.5 + share), "maybe"
        if fit:
            scored.append((rank, r["id"], r, fit))
    scored.sort(key=lambda x: (-x[0], x[1]))
    out = []
    for _, _, r, fit in scored[:n]:
        how = r.get("how") or "ask_first"
        out.append({"automation": r["id"], "title": r.get("title") or "", "shortcut": r.get("shortcut") or "",
                    "fit": fit, "how": how, "what_to_do": HOW_SAY[how] if fit == "clear" else MAYBE_SAY})
    return out
