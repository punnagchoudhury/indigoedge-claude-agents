# IndigoEdge Market Research Agent — Operating Playbook (v5)

*The complete, current design spec for the Claude + connectors research agent. Replaces all earlier versions. A fellow names a company; the agent produces a sourced, conflict-flagged three-part dossier, always writes it to the Notion database, and optionally hands back a branded Word doc. The companion "Agent Instructions v6" is the executable version. Stands alone.*

**What's current in v5:** two depth modes; rearranged pipeline with risk folded into the news sweep + Tracxn status; Notion-always + optional branded Word; the global pattern-match; the three-part Company / Sector / Comparables structure with Sector and Comparables as the high-value branches; a consolidated **Filings & compliance** block; a **who-invested investor table**; **cap table = shareholding pattern** (Option 1) sourced from MCA/DRHP filings; **DRHP/filing mining**; hardened, staged delivery; and a **clean-professional branded docx template**. The "projected entry/exit/outcome" remains excluded to avoid biasing the fellows.

---

## 1. The accuracy doctrine (non-negotiable)

1. **Zero fabrication** — not retrieved = a listed gap.
2. **Full traceability** — every figure carries a clickable source link, in Notion and Word.
3. **Conflicts surfaced and explained** — show both values, explain the difference (filing tranche vs announced round, group vs entity, metric definitions); never blend.
4. **Confidence labelled** — `[FACT]` `[ESTIMATE]` `[UNCONFIRMED]` `[COMPANY-PROVIDED]` `[INTERNAL]` `[CONFLICT]`, each High/Med/Low.
5. **Source tiering** — primary filing > reputable named press > research house > aggregator > forum.
6. **No projected outcomes** — observed facts and *others'* outcomes only; never a predicted exit/valuation/outcome for the target.
7. **Sourcing hygiene** — cite only what was actually used, by its real path; never imply unowned subscriptions.
8. **Multiples show their basis** — numerator, denominator (which revenue/ARR), date.

**Golden rule:** a marked gap or explained conflict is a success; a confident wrong number is a failure.

---

## 2. Depth modes (chosen at intake)

- **Quick screen** — snapshot, funding, investors, valuation, top comparables, controversy flags.
- **Standard** *(default)* — the full three-part dossier below.

---

## 3. The pipeline

Effort is weighted toward Sector and Comparables, since company facts are largely retrievable while the sector and competitive picture are where the value is.

0. **Intake** — company + domain/LinkedIn; depth; documents (only if provided); Word download? Notion is automatic.
1. **Entity resolution (mandatory)** — exact Tracxn ID; disambiguate; watch product/subsidiary records and name collisions.
2. **External structured pull (Tracxn)** — profile, founders, headcount, financials, legal entities + legal-status flags, funding rounds + valuations + investors, sector acquisitions, comparables.
3. **Filings pull (MCA + regulatory)** — AOC-4, MGT-7, PAS-3, CHG, DIR-12/SH-7, AGM/auditor/compliance, via Tofler/Zauba/Probe42/InstaFinancials; DRHP/RHP for IPO-bound; ACRA/Companies House/SEC for foreign entities.
4. **Internal precedent layer** — Slack/Notion/Drive/Airtable, by company *and* sector; surface direct prior work and precedents/benchmarks; tell the fellow what matched.
5. **Document ingestion (only if provided)** — parse decks/models/CIMs; `[COMPANY-PROVIDED]`.
6. **Market & competitive intelligence (high-value)** — Sector and Comparables branches (§5) with the global pattern-match (§6) and DRHP mining.
7. **News sweep** — typed sweep + risk/controversy queries (folded in here, no separate stage) + sector sweep; Indian outlets + global wires; full articles, paraphrased, linked, tiered.
8. **Signals** — product/customer reception, hiring trend, founder track record.
9. **Reconciliation & QA** — cross-check; group-vs-entity rule; `[CONFLICT]` explained; build the Verify checklist.
10. **Synthesis** — narrative + SWOT on verified facts only.
11. **Delivery** — Notion always (chunked), optional branded Word; both with links, freshness stamps, visuals, verify checklist.

---

## 4. Data-source routing

| Field | Primary | Notes |
|---|---|---|
| Company facts | Tracxn + provided docs + web | Largely retrievable |
| **Filings** | MCA (AOC-4/MGT-7/PAS-3/CHG/DIR-12/SH-7) via Tofler/Zauba/Probe42/InstaFinancials; DRHP; ACRA/CH/SEC | Consolidated audit-trail block |
| **Cap table** | DRHP (if IPO-bound) > MGT-7 pattern + PAS-3 > modeled estimate | Shareholding *pattern* (Option 1), not per-line |
| Legal/controversy | News sweep + Tracxn status flags | No separate stage |
| Valuation | Tracxn round post-money (filing) | Explain divergences; never blend |
| Sector sizing & dynamics | Research-house summaries + web + bottom-up + DRHPs | India sized separately; global-anchored where thin |
| Comparables | Tracxn comp graph + web + DRHPs + internal | Tiered; global parallels included |
| Internal precedents | Slack/Notion/Drive + Airtable trackers | `[INTERNAL]`; surface matches |
| Delivery | Notion database (always) + branded Word (optional) | Word styled via the house template |

---

## 5. The dossier template — three parts

Each section opens with *Sources as of [date]*; every figure links; visuals used where natural.

### Part 1 — The Company
Snapshot · About (product, founders + track-record, how they make money, locations, entities, clients) · Funding history (round-by-round) · **Investor table** · **Cap table & ownership (shareholding pattern)** · Financials · Valuation · **Filings & compliance block** · Product & customer reception + talent signals · Controversy/legal flags inline · Company-provided materials (if any) · Direct internal prior work (if any).

- **Investor table** — the complete, untruncated list of *everyone who invested* (institutional, strategic, angel, debt, accelerator): **Investor · Type · Round entered · Lead? · Status (active / partial exit / full exit) · Stake % (where the filing exposes it)**, plus a one-line cap-table-dynamics note (who controls, who's exiting, who might lead next). Concise — no padded fund bios.
- **Cap table (shareholding pattern)** — founders %, investors' collective % + major holders, ESOP pool %, dilution trend, at the best resolution the filings allow; precise per-line / fully-diluted / share-class detail flagged as a DDE pull. Draws on the same DRHP/MGT-7 data as the investor table's Stake %.
- **Filings & compliance block** — consolidated primary-source audit trail: AOC-4 financials, MGT-7 shareholding, PAS-3 allotments, CHG charges/debt, DIR-12/SH-7 changes, AGM/auditor/compliance status, DRHP and foreign-entity filings. Each line dated and linked. The Financials/Valuation/Cap-table sections analyse on top — no duplication.

### Part 2 — The Sector *(high-value branch)*
Market definition & segmentation · value chain / ecosystem map · sizing & growth (TAM/SAM/SOM, found-primary + bottom-up cross-check, India separate from global, global-anchored where thin) · demand drivers & tailwinds · headwinds & sector risks · regulatory & policy · market structure & maturity (India vs global) · trends & inflection points · capital & deal activity · global driver pattern-match (§6).

### Part 3 — The Comparables / Competition *(high-value branch)*
Criteria-first tiered comp set (T1 direct · T2 adjacent · T3 global analogs; Indian + global; rationale + exclusions) · consistent profile per comp · head-to-head differentiation + positioning view · competitive dynamics · funding/valuation benchmarking (multiple basis shown) · exits & outcomes in the set (others', never a projection) · internal precedents.

### Closing
**SWOT** (from verified facts) · **Open Questions / Verify** checklist (the most valuable section).

---

## 6. Rules for the hard parts

**Global pattern-match (market-stage method).** Abstract the target to its category → find global exemplars → diagnose *why* they won (timing, structural/regulatory tailwinds, model & unit economics, moats, capital intensity, GTM) → map parallels **and divergences** to India (the divergences carry the insight) → tier (T1 direct analog/leader, T2 adjacent, T3 loose), weighting by tier. Drivers feed Sector; analog companies feed Comparables. Global market size ≠ India size.

**Market sizing.** Found/triangulated figure is the headline (≥2 cited sources, as a range); bottom-up build (target customers × realistic ACV, arithmetic shown, inputs sourced) is the cross-check; mine DRHPs for both. Divergence between found and computed → flag and explain.

**Cap table = shareholding pattern (Option 1).** As §5; DRHP > MGT-7+PAS-3 > modeled estimate; precise per-line is a DDE pull.

**Valuation.** Latest disclosed round filing post-money is primary `[FACT]`; divergent figures shown and explained; never blended.

**Risk/controversy (no separate stage).** Public items from the news sweep; silent legal/regulatory flags (NCLT/CIRP/charges) from Tracxn + the filings block; surfaced inline. Deep legal work stays in the DDE.

**Group vs entity.** State which entity/level each figure is; don't report a group-vs-entity difference as a real conflict.

**Thin-company protocol.** Primary sources as the floor; triangulate from comps and global parallels; lower confidence, flag, state what came back empty; write concisely, don't pad.

---

## 7. Delivery & house style

**Notion is non-negotiable** — every run creates/updates a page in the Market Research Dossiers database, built by appending sections (within Notion's per-request block limit), never one monolithic call. On request, the agent **also generates a branded Word (.docx)**.

**Build method (robust, staged).** Author the dossier to a Markdown file once (never re-type the full text); generate charts as image files up front (math parsing off); deliver Notion first, then convert Word from the same file. Stage across bounded steps when a run has been long.

**House style (branded docx).** The Word doc is styled through `IndigoEdge_Dossier_Template.docx` — a pandoc reference template carrying the IndigoEdge look: clean-professional, no cover band, **deep indigo #3E3B95** (title, headings, table-header fill), **electric teal #00A4E4** (sub-headings, hyperlinks, section rule), white table-header text, light row borders, and a branded page-number footer. The agent converts with `--reference-doc`; if the template file isn't on disk it regenerates it via `build_ie_template.py`. Styling lives in the template, so the build stays simple — change the template once and all future dossiers follow.

---

## 8. Data stack & subscriptions

- **Core (in use):** Tracxn; Slack/Notion/Drive (priority channels `#all-hands-notes`, `#company-outreach-notes`, `#company-response-notes`, `#fund-notes`, `#km-sharing`, `#dde-notes`); web search + fetch; MCA-filing aggregators (Tofler/Zauba/Probe42/InstaFinancials) and DRHP/RHP filings for filings, cap table, and sizing.
- **To wire:** Airtable connector (closed-DDE + live-mandate trackers — the structured precedent corpus); Google Drive deal-materials folders.
- **No news API / RSS for v1** (RSS parked for the monitoring phase).
- **Parked pending pricing:** AlphaSense; signal enrichers (workforce data; G2 / Gartner Peer Insights). Check the "Database Access Logins" page first. PitchBook only if cross-border.

---

## 9. Connector access & roadmap

- Connectors, not scraping — permissioned, real-time. `#dde-notes` now public and included; DDE_[Company] Notion teamspaces need account access granted to mine fully. Output database "Market Research Dossiers" exists and is schema'd.
- This agent is the **pre-diligence front end** of the firm's broader AI-native DDE effort; align output with the firm's DDE methodology and house format.
- **Phase 1 (now):** Claude Project + connectors running this playbook.
- **Phase 2 (scale):** software; own vector-store index (wrapped as a custom MCP connector); monitoring mode; approved paid sources; a quality/eval rubric to grade every run.

---

*v5 — living document. Refine the tiering, branches, and house style as fellows surface needs.*

---

## Presentation standards (added v9.1, from stakeholder review)

House format rules applied to every dossier:

1. **People as a table** — founders/team rendered as Founder · Role · Background / relevant experience, one row each (not a prose list of names).
2. **State valuation once** — all valuation sits in the funding section (round table + trajectory + implied multiple with basis); no separate, repeating Valuation section. Same single-statement rule as the cap table.
3. **Comparables are tables, every tier the same shape** — T1/T2/T3 each a table with matching columns; no bracket/semicolon-dense prose bullets. T2 columns: Company · Type · Revenue/scale · Raised · Read.
4. **Global analogs enriched** — the T3 table carries scale/funding and a "relevance to target / why it matters" column.
5. **Internal precedents labelled by relationship (accuracy rule)** — each company tagged Mandate · DDE done · Pitch/advised · Company met · Benchmark-only (not engaged). Never imply the firm worked with a company it only met or benchmarked.
6. **SWOT as a 2×2 quadrant table** — not four prose paragraphs.
