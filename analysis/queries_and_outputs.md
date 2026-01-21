# Queries and outputs (append-only)

## 2026-01-20T??:?? — Initialized

Purpose: record each analytic query posed to the corpus, the answer, supporting sources, tensions/negative cases, and what changed as a result.

## 2026-01-20T??:?? — Q1 (broad): What are initial “causal stories” of loneliness in the first sample?

### Query
From the initial sample of three interviews (Newham/Hackney/Tower Hamlets), what “causal stories” do participants give for loneliness (mechanisms, not just topics)?

### Answer (initial, sample-limited)
Across these three sources, loneliness is described less as mere physical aloneness and more as a set of relational and self-relational mechanisms:
- **Relational mismatch / not being understood**: loneliness persists even with others present when one’s lived experience is not grasped (Interview 1).
- **Exclusion and opportunity gaps**: loneliness is produced by being left out (not invited / pushed aside) and by perceived barriers to participation (Interview 1; Interview 12).
- **Blocked disclosure / self-protective distance**: loneliness is maintained by keeping emotions inside and avoiding vulnerability due to fear of judgment (Interview 33; Interview 12).
- **Comparison-driven self-doubt**: social media exposure to others’ success/support networks produces intimidation, doubt, and a felt lack of “someone to do that with” (Interview 12).
- **Support absence**: loneliness becomes acute in distress when support is unavailable or perceived as unavailable (Interview 1; Interview 33).
- **Loss/void**: relationship breakup amplifies loneliness even without changing the number of people around you (Interview 1).

### Supporting sources (sample)
- `/sources_md/Interview_01_part1and2.md`
- `/sources_md/Interview_12_part1and2.md`
- `/sources_md/Interview_33_part1and2.md`

### Tensions / negative cases (not yet searched)
- This is not yet tested against cases where loneliness is framed primarily as structural/material constraint (e.g., finances, housing, neighbourhood safety) or as chosen solitude.

### What changed as a result
- Created initial code set (v0) in `analysis/codebook.md` around misunderstanding, exclusion, support absence, breakup/void, social-media comparison, and blocked disclosure.

## 2026-01-20T??:?? — Q2 (broad): Where do the initial codes show up across the corpus (rough coverage scan)?

### Query
Using lightweight keyword scans as a first-pass *coverage proxy*, which interview files show evidence consistent with the current codebook?

### Answer (keyword-based coverage proxy; to be refined)
Note: this is not “coding by keyword”; it’s a quick way to locate candidate sources for each code and ensure we are not overfitting to the initial sample.

- **Misunderstood_or_noSharedExperience** (keyword: `misunderstood`): 6 files
  - Interview_01_part1and2.md; Interview_02_part1and2.md; Interview_11_part1and2.md; Interview_13_part1and2.md; Interview_19_part1and2.md; Interview_39_part1and2.md
- **Exclusion_leftOut_opportunityGap** (keywords: `outcast|left out|excluded|not invited`): 27 files
  - Includes Interview_01, 11, 12, 14_part2, 37 and many others (see grep output history).
- **Breakup_voidAndHeightenedLoneliness** (keywords: `break up|breakup`): 10 files
  - Interview_01_part1and2.md; Interview_04_part1and2.md; Interview_05_part1and2.md; Interview_13_part1and2.md; Interview_13_part2.md; Interview_33_part1and2.md; Interview_41_part1and2.md; Interview_42_part1and2.md; Interview_43_part1and2.md; Interview_44_part1and2.md
- **SocialMediaComparison_overwhelm_intimidation** (keywords: `social media|instagram`): 34 files
  - Very widespread; includes Interview_05, 07, 08, 09, 10, 11, 12, 13, 16, 17, … etc.
- **Sanctuary_bedroomSafety_withdrawal** (keywords: `bedroom|sanctuary`): 12 files
  - Includes Interview_08_part1.md; Interview_16_part1and2.md; Interview_18_part1and2.md; Interview_37_part1and2.md; Interview_41_part1and2.md; etc.
- **ConnectedPlace / youth clubs** (keywords: `youth club(s)`): 6 files
  - Interview_14_part2.md and Interview_14_part1and2.md plus Interview_20, 24, 28, 32.
- **Safety/crime/secure location** (keywords: `crime|safe|secure`): 22 files
  - Includes Interview_12_part1and2.md; Interview_14_part2.md; Interview_37_part1and2.md; Interview_41_part1and2.md; etc.

### What changed as a result
- Confirms that several candidate codes are **not rare** (e.g., social media comparison), so we need to be careful not to make “frequency = importance” claims.
- Flags which sources to return to for deeper, excerpt-grounded analysis when drafting results and negative cases.

## 2026-01-20T??:?? — Q3 (iterative): What mechanisms *compete* with the threat→withdrawal loop?

### Query
As we read successive interviews, what rival or additional mechanisms explain loneliness that are not reducible to “social threat appraisal → withdrawal”?

### Answer (after Phase 2 / Batch 1)
Batch 1 suggests the threat→withdrawal loop is important but incomplete. Competing/additional mechanisms include:
- **Work/time scarcity**: loneliness produced by structural routine, exhaustion, and lack of time for relationships (Interview_29_part1and2).
- **Grief/loss**: bereavement as an initiating condition; loneliness following loss even with some social surroundings (Interview_29_part1and2; echoed as a possible cause in Interview_05_part1and2).
- **Loneliness-as-emptiness + coping cycles**: emptiness framed as central, with substance/comfort coping that briefly relieves and then rebounds (Interview_05_part1and2).
- **Normative assimilation pressure**: loneliness as the cost of not meeting standards (appearance/hair/dress) required to “join the crowd” (Interview_19_part1and2).
- **Loneliness-as-safety/survival**: loneliness framed as protective training (“lonely but safe”), complicating the assumption that loneliness is always simply negative (Interview_41_part1and2).
- **Class/resource inequality**: shared background and resource access shape who can connect/confide (Interview_14_part2).

### Evidence pointers
See `analysis/excerpts_log.md` entries for the six batch interviews, especially Interview_29 (work/time and grief), Interview_05 (emptiness + coping), Interview_19 (assimilation pressure), Interview_41 (survival framing), Interview_14 (class + safety infrastructures).

### What changed as a result
- The theory needs at least a **multi-mechanism model** with explicit scope conditions (when the threat loop dominates vs when structural/time or grief dominates).

## 2026-01-20T??:?? — Q4 (theme building): What are the candidate *themes* that unify these mechanisms without becoming a topic list?

### Query
Given the expanded mechanisms from Batch 1–2, what higher-level themes (interpretive stories) could unify them while preserving tensions and negative cases?

### Answer (provisional; after Phase 2 / Batch 2)
Candidate themes (to test in subsequent batches; not final):
- **Theme A — Belonging is conditional**: fitting in requires meeting standards (appearance, behavior, topics, class-coded norms); fear of judgment and assimilation pressure make connection costly.
  - Evidence anchors: Interview_19_part1and2, Interview_14_part2, Interview_46_part1and2, Interview_38_part1and2.
- **Theme B — Loneliness as a safety technology**: withdrawal/phones/sanctuary are used to manage threat and mismatch; short-term relief can deepen isolation.
  - Evidence anchors: Interview_37_part1and2, Interview_05_part1and2, Interview_38_part1and2, Interview_41_part1and2.
- **Theme C — Mediated sociality intensifies comparison and unreality**: social media/phones create quantified status systems (followers/likes) and “show vs reality,” producing envy, FOMO, and loneliness-on-platform.
  - Evidence anchors: Interview_29_part1and2, Interview_11_part1and2, Interview_16_part1and2, Interview_24_part1and2, Interview_38_part1and2.
- **Theme D — Structural constraint erodes relationships**: time scarcity, work transitions, cost pressures, and therapy access barriers reduce supportive contact and increase emotional isolation.
  - Evidence anchors: Interview_29_part1and2, Interview_16_part1and2, Interview_46_part1and2, Interview_38_part1and2.
- **Theme E — Being ‘othered’ (race, stigma) is loneliness-making**: loneliness emerges from categorization/dehumanization and denial of second chances.
  - Evidence anchors: Interview_11_part1and2, Interview_24_part1and2, Interview_46_part1and2.

Key tensions/negative cases to preserve:
- Outsiderhood can be content/curious (Interview_19_part1and2).
- Loneliness can be framed as protective/survival (Interview_41_part1and2).

### What changed as a result
- We now have a candidate theme set to **test (not declare)** in Batch 3 by selecting interviews likely to disconfirm each theme.


