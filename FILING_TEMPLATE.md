# Redline — Filing Template (v2)

Fill this in per candidate, from first lead to published filing. Every field
maps to something that renders on the page or governs the research workflow —
don't skip fields to save time; the fields are what keep a candidate from
becoming a published claim before it's earned that.

---

## 0. Evidence-Status Ladder

Every candidate moves through these stages in order. Don't skip a stage.

**LEAD → PARTIALLY VERIFIED → VERIFIED → PUBLISHED**

| Stage | What's required to be here |
|---|---|
| **LEAD** | A reported change with a company, rough date, and at least one source. Nothing independently checked yet. Never shown on the live docket. |
| **PARTIALLY VERIFIED** | Current document retrieved directly by Redline. Previous document still missing, OR a reputable outlet (Reuters, etc.) did the before/after comparison directly but Redline hasn't reproduced it independently yet. May appear on the docket, clearly labeled. |
| **VERIFIED** | Both current and previous documents retrieved and compared directly by Redline. Effective date confirmed. Notice status searched. Agreement scope confirmed. |
| **PUBLISHED** | Verified, written up in full using this template, and live on the docket. |

**Do Not Publish rule:** if any official document, FAQ, or support page
*contradicts* the candidate claim, the filing stays at LEAD or is marked
UNVERIFIED with the conflict stated. It does not move forward on the strength
of secondary reporting alone, no matter how strong that reporting is.

## 1. Filing Identity

| Field | Value |
|---|---|
| Docket | REDLINE-[YEAR]-[###] |
| Company | |
| Product / Service | |
| Policy Type | Terms of Service / Privacy Policy / Subscription Terms / Other |
| Change Status | New / Amended / Major Revision / Minor Revision |
| **Agreement Scope** | *Exactly which agreement/product/plan/customer group this applies to.* Don't say "T-Mobile" — say "T-Mobile postpaid wireless Terms & Conditions; does not cover T-Mobile Money, Fiber, or Business agreements." Telecoms, banks, insurance, marketplaces, and enterprise SaaS almost always have more than one governing document — assume that's true until you've confirmed otherwise. |
| Document Date | [Month Day, Year the document itself was updated/published] |
| Effective Date | [Month Day, Year the provisions actually take effect / Not stated] — **keep separate from Document Date.** A document can be updated well before its terms take effect. |
| Previous Version | [Date / URL / archive reference, or "not yet retrieved"] |
| Current Version | [Date / URL] |
| Status / Confidence | LEAD / PARTIALLY VERIFIED / VERIFIED / UNVERIFIED — HOLD, plus HIGH/MEDIUM/LOW confidence and one sentence on what's still unconfirmed |
| **Conflict Found?** | YES / NO. If YES, name the contradicting document and quote or paraphrase the conflict. A YES here overrides everything else — see Do Not Publish rule above. |

## 2. Headline & Summary
*(renders in `<h3>` and the docket-no line — keep the headline to ~10 words)*

- **Headline:**
- **One-line summary:**

## 3. Facts / Community Reports / Inference
*(keep these three visually and structurally separate — this is what stops a
reported allegation from quietly becoming a stated fact)*

- **FACT** *(renders in `.finding`)* — only what the actual documents establish. No adjectives, no framing.
- **COMMUNITY REPORT** *(renders in the `.finding` block, second paragraph or a labeled sub-line)* — what Reddit threads, news coverage, or forum discussion say happened. Attribute it: "Reporting from X says..." — never blend this into FACT.
- **INFERENCE** *(renders in `.finding.interpretation`, i.e. Why It Matters)* — Redline's own read. Always framed as analysis ("this likely means...", "in practice..."), never as something the document itself states.

## 4. Document Evidence — Before / After
*(renders in `.redline` — the actual diff block)*

- **Section / Clause:** [exact section number + heading]
- **PREVIOUS:** [paraphrase; quote under 15 words if quoting at all]
- **CURRENT:** [paraphrase; quote under 15 words if quoting at all]
- **Change type:** Added / Removed / Expanded / Narrowed / Reworded / Moved

If you don't have both PREVIOUS and CURRENT confirmed firsthand, say so in
the diff block itself rather than presenting a one-sided "current only" diff
as if it were a comparison.

## 5. Why It Matters
*(renders in `.finding.interpretation`)*

Practical, financial, or privacy consequence — neutral framing, not a legal
conclusion. Say "this narrows what a user can recover if..." not "this
clause is unenforceable" or "this violates the law." That's for a lawyer to
say, not Redline.

## 6. User Impact
*(renders in the second `.source-trail`-styled block, labeled "User Impact")*

- **Who is affected:** free users / paid users / business customers / all users / specific region — and cross-check against Agreement Scope above
- **What should users do:** [action required, or "none"]
- **Notice given?** One of: **YES — CLEAR** / **YES — VAGUE** / **NO CLEAR NOTICE LOCATED IN OUR SEARCH** / **UNKNOWN**. Never write "no notice was sent" unless you have positive evidence of that — absence of a source is not proof of absence of a notice.
- **Opt-out:** yes / no / not stated / not verified

## 7. Source Trail
*(renders in the first `.source-trail` block — every link must be real)*

Ranked by reliability — cite the highest tier you actually have, and don't
let a lower tier substitute for a missing higher one:

1. Vendor agreement / current live document
2. Vendor support or legal page
3. Archived version (Wayback Machine, etc.)
4. Regulatory filing
5. Reputable reporting (Reuters, major outlets)
6. Community discussion (Reddit, forums) — **this generates leads, it never
   establishes the change by itself**

- **Current document:** [URL]
- **Previous document:** [URL or archive link, or "not yet retrieved"]
- **Archive snapshot:** [Wayback Machine link, or "not yet pulled"]
- **Company announcement:** [URL, or "no clear notice located in our search"]
- **Reporting:** [URL(s) — name the publication]
- **Community discussion:** [URL(s), labeled as leads only]

## 8. Verification Checklist
*(only move to VERIFIED when every box that applies is checked — an
unchecked box isn't a failure, it's a reason to stay at PARTIALLY VERIFIED)*

- [ ] Current document retrieved directly
- [ ] Previous document retrieved directly
- [ ] Effective date confirmed (and distinguished from document date)
- [ ] Agreement scope confirmed (which product/plan/customer group)
- [ ] Exact changed language confirmed word-for-word
- [ ] Notice searched (and labeled per the standardized values above)
- [ ] Community reaction searched
- [ ] Current URL confirmed live
- [ ] Archived URL confirmed accessible
- [ ] Conflict check run — no official document contradicts the claim
- [ ] Facts, community reports, and inference are visually separated
- [ ] Quotations stay under 15 words; most writing is original paraphrase
- [ ] No fictional/demo company is presented as a real filing

---

### HTML mapping cheat sheet

| Template section | HTML element |
|---|---|
| Docket, Company, Product, Agreement Scope | `.docket-no`, `<h3><span class="company">`, add a line in `.dates` for scope |
| Document Date / Effective Date / Verified date | `.dates` (three separate lines, never merged) |
| Status Label | `.stamp` (`""` = Verified, `.partial` = Partially Verified, `.demo` = Unverified/Demo) |
| Conflict Found | a `.finding.interpretation` block titled "Why this isn't published" (see the T-Mobile entry in `index.html` for the pattern) |
| Document Evidence (Before/After) | `.redline` with `<del>`/`<ins>` |
| Facts | `.finding` |
| Community Report | `.finding.community` (dotted underline, neutral tone, `.attribution` line naming the source) |
| Why It Matters / Inference | `.finding.interpretation` |
| Source Trail (ranked) | `.source-trail` (first instance) |
| User Impact | `.source-trail` (second instance, labeled "User Impact") |
| Status + Categories | `.case-footer` |
