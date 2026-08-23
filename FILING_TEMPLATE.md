# Redline — Filing Template

Fill this in per filing, then translate it into a `<article class="case-file">`
block using the pattern in `index.html`. Every field here maps directly to
something that renders on the page — don't add fields the template doesn't
have a place for.

---

## 1. Filing Identity

| Field | Value |
|---|---|
| Docket | REDLINE-[YEAR]-[###] |
| Company | |
| Product / Service | |
| Policy Type | Terms of Service / Privacy Policy / Subscription Terms / Other |
| Change Status | New / Amended / Major Revision / Minor Revision |
| Published | [Month Day, Year — date the company published the change] |
| Effective Date | [Month Day, Year / Not stated] |
| Previous Version | [Date / URL / archive reference] |
| Current Version | [Date / URL] |
| Status Label | VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / DEMO-SAMPLE |

Status label rules (do not skip this — it's the whole point):
- **VERIFIED** — you compared the actual previous and current documents yourself.
- **PARTIALLY VERIFIED** — the change is supported, but one piece of evidence
  is missing (usually: you have the current doc but not the prior one).
- **UNVERIFIED** — you found a reported change but haven't confirmed the
  underlying documents yet. Publish sparingly, and say so plainly.
- **DEMO / SAMPLE** — fictional or prototype content only. Never used for a
  real company.

## 2. Headline & Summary
*(renders in `<h3>` and the docket-no line — keep the headline to ~10 words)*

- **Headline:**
- **One-line summary:**

## 3. What Changed
*(renders in `.finding` — factual only, no interpretation)*

2-4 sentences or bullets describing only what the documents establish. No
adjectives about how bad or good it is — that belongs in Why It Matters.

## 4. Document Evidence
*(renders in `.redline` — this is the actual diff block)*

- **Section / Clause:** [exact section number + heading]
- **Previous language:** [paraphrase; quote under 15 words if quoting at all]
- **New language:** [paraphrase; quote under 15 words if quoting at all]
- **Change type:** Added / Removed / Expanded / Narrowed / Reworded / Moved

## 5. Why It Matters
*(renders in `.finding.interpretation` — clearly Redline's read, not fact)*

Practical, financial, privacy, or legal-exposure consequence. Frame as
analysis: "this means...", "in practice...", never stated as if it were in
the document itself.

## 6. User Impact
*(renders in the second `.source-trail`-styled block, labeled "User Impact")*

- **Who is affected:** free users / paid users / business customers / all users / specific region
- **What should users do:** [action required, or "none"]
- **Notice given:** email / in-app / website only / no notice found / not verified
- **Opt-out:** yes / no / not stated / not verified

## 7. Source Trail
*(renders in the first `.source-trail` block — every link must be real)*

- **Current policy:** [URL]
- **Previous policy:** [URL or archive link, or "not yet retrieved"]
- **Archive snapshot:** [Wayback Machine link, or "not yet pulled"]
- **Company announcement:** [URL, or "none found"]
- **Secondary reporting:** [URL(s) — name the publication]

## 8. Editorial Safety Check
Run through before publishing. If any box is unchecked, downgrade the status
label — don't publish as VERIFIED anyway.

- [ ] Every factual claim traces to a source in the trail above
- [ ] Previous and current versions were actually compared (not just described)
- [ ] Dates are verified, not guessed
- [ ] Facts (What Changed) are separated from interpretation (Why It Matters)
- [ ] Any missing evidence is explicitly marked "not verified" / "not yet retrieved"
- [ ] No fictional/demo company is presented as a real filing
- [ ] Quotations stay under 15 words; most of the writing is original paraphrase
- [ ] Any legal/privacy conclusion is framed as analysis, not legal advice

---

### HTML mapping cheat sheet

| Template section | HTML element |
|---|---|
| Docket, Company, Product | `.docket-no`, `<h3><span class="company">` |
| Published / Effective / Verified dates | `.dates` |
| Status Label | `.stamp` (`""`, `.demo`, or `.partial` class) |
| Document Evidence | `.redline` with `<del>`/`<ins>` |
| What Changed | `.finding` |
| Why It Matters | `.finding.interpretation` |
| Source Trail | `.source-trail` (first instance) |
| User Impact | `.source-trail` (second instance, labeled "User Impact") |
| Status + Categories | `.case-footer` |
