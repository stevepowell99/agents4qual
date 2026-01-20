# Research journal (append-only)

## 2026-01-20T00:00:00Z — Project initialization

### Purpose
- Keep a historical, append-only record of decisions, prompts/queries, hypotheses, and methodological reflections.
- **Rule**: Never delete or overwrite prior entries; only append new dated sections.

### Tooling disclosure (initial)
- **LLM environment**: Cursor Agent (model: GPT-5.2-codex) used for reading/writing/analysis within this repo.
- **External web search**: Not used for substantive analysis. Conference materials are already in `/call/`.

### Corpus notes (initial)
- Interviews are provided as individual `.docx` files in `/sources/`.
- Each interview will be treated as an independent source (not concatenated into one corpus file).

## 2026-01-20T00:10:00Z — DOCX→Markdown conversion + corpus inventory

### What I did
- Converted every interview `.docx` in `/sources/` into **one Markdown file per DOCX** in `/sources_md/`.
- Wrote a generated mapping table: `/sources_md/_conversion_map.md`.

### Important correction
- The corpus contains multiple DOCX files that can share an interview number (e.g. separate “part 2” files). The converter therefore outputs **unique filenames per DOCX** (e.g. `Interview_13_part1and2.md` and `Interview_13_part2.md`) to avoid overwriting.

### Inventory (from filenames + conversion outputs)
- **Total source DOCX**: 50
- **Total transcript MD produced**: 50 (plus `_conversion_map.md`)
- **Borough (from filenames)**:
  - Newham: 12
  - Hackney: 14
  - Tower Hamlets: 12
  - Barking & Dagenham (incl. B&D/B & D): 12

## 2026-01-20T00:45:00Z — Metadata parsing correction (derived corpus)

### What changed
- The initial DOCX→MD run extracted `age` incorrectly for many files because it sometimes picked up the interview number (e.g., Interview 33 → age 33).
- I updated the converter to parse age from the comma-delimited slot in filenames (e.g., “Male, 23, Tower Hamlets” → age 23), then regenerated `/sources_md/` (derived outputs only).

### Why it matters
- Accurate metadata helps purposeful sampling and borough/age/gender comparisons without manually re-annotating each transcript.

## 2026-01-20T00:55:00Z — Start of first analytic cycle (initial familiarization)

### Purposeful initial sample (v0)
Goal: begin initial coding and hypothesis generation with a small, diverse set of sources before scaling.

Initial sources read closely:
- `/sources_md/Interview_01_part1and2.md` (Male, 24, Newham)
- `/sources_md/Interview_12_part1and2.md` (Female, 22, Hackney)
- `/sources_md/Interview_33_part1and2.md` (Male, 23, Tower Hamlets)

## 2026-01-20T01:25:00Z — DOCX extraction correction (tables)

### What changed
- Some DOCX files store transcript text inside tables. The converter now extracts paragraphs from both the document body and tables, then regenerates `/sources_md/` (derived outputs only).

### Why it matters
- Prevents “empty transcripts” and reduces selection bias caused by extraction failures.

## 2026-01-20T01:30:00Z — Sample extended (v1)

Additional sources read closely to test/extend initial codes beyond the first three:
- `/sources_md/Interview_37_part1and2.md` (Female, 19, Barking & Dagenham)
- `/sources_md/Interview_41_part1and2.md` (Male, 18, Barking & Dagenham)
- `/sources_md/Interview_14_part2.md` (Female, 18, Hackney; neighbourhood/places only)

## 2026-01-20T10:40:00Z — Phase 2 begins: iterative reflexive TA (Batch 1 completed)

### Why Phase 2
Phase 1 generated an initial theory and codes, but did not iterate through successive interviews in a way that could systematically *disconfirm* the initial theory or develop it through repeated reading and re-reading.

### Batch 1 (diverse; not selected by keyword hits)
Read and excerpt-tagged in `analysis/excerpts_log.md`:
- `/sources_md/Interview_05_part1and2.md` (Female, 19, Newham)
- `/sources_md/Interview_08_part1.md` (Male, 18, Newham)
- `/sources_md/Interview_14_part2.md` (Female, 18, Hackney; part 2)
- `/sources_md/Interview_19_part1and2.md` (Male, 19, Hackney)
- `/sources_md/Interview_29_part1and2.md` (Female, 22, Tower Hamlets)
- `/sources_md/Interview_41_part1and2.md` (Male, 18, Barking & Dagenham)

### What changed after Batch 1 (high level)
- Expanded codebook to include rival mechanisms (work/time scarcity, grief/loss, loneliness-as-emptiness, coping cycles, assimilation pressure, faith framing, loneliness-as-safety).
- Added Q3 to explicitly track competing mechanisms (see `analysis/queries_and_outputs.md`).
- Updated theory memos with per-interview micro-memos (see `analysis/theory_memos.md`).

### Decision rule (to reduce confirmation bias going forward)
- New codes are allowed only when they represent a distinct mechanism that appears in more than one interview or is theoretically crucial as a negative/rival case; otherwise we memo it as variation under an existing code.

## 2026-01-20T12:05:00Z — Phase 2 continues: Batch 2 completed (testing rival mechanisms)

### Batch 2 (diverse; selected to stress-test candidate themes)
Read and excerpt-tagged in `analysis/excerpts_log.md`:
- `/sources_md/Interview_11_part1and2.md` (Male, 23, Newham)
- `/sources_md/Interview_34_part1and2.md` (Female, 19, Tower Hamlets)
- `/sources_md/Interview_38_part1and2.md` (Female, 22, Tower Hamlets)
- `/sources_md/Interview_24_part1and2.md` (Female, 18, Hackney)
- `/sources_md/Interview_16_part1and2.md` (Male, 24, Hackney)
- `/sources_md/Interview_46_part1and2.md` (Female, 18, Barking & Dagenham)

### What changed after Batch 2 (high level)
- Added a small set of **recurrent** new codes to the codebook: race/othering, social façade/mask, phone-mediated connection, urban anonymity, social-media-as-fake-connection, stigma/second-chances.
- Added Q4 to propose candidate **themes** (interpretive stories) that unify mechanisms while preserving tensions.

### Next step (Batch 3 design: disconfirmation-oriented)
- Purpose: pick interviews likely to **break** each candidate theme (A–E), and re-read at least 2 earlier “anchor” interviews if we split/merge themes again.

## 2026-01-20T13:35:00Z — Phase 2 continues: Batch 3 completed (first disconfirmation pass)

### Batch 3 (deliberately chosen to disconfirm candidate themes)
Read and excerpt-tagged in `analysis/excerpts_log.md`:
- `/sources_md/Interview_02_part1and2.md` (Male, 23, Newham)
- `/sources_md/Interview_10_part1and2.md` (Female, 24, Hackney)
- `/sources_md/Interview_42_part1and2.md` (Male, 24, Barking & Dagenham)
- `/sources_md/Interview_43_part1and2.md` (Male, 23, Tower Hamlets)
- `/sources_md/Interview_44_part1and2.md` (Male, 24, Tower Hamlets)
- `/sources_md/Interview_45_part1and2.md` (Female, 24, Barking & Dagenham)

### What changed after Batch 3 (high level)
- No new core mechanisms were required; Batch 3 primarily **refined scope conditions** and clarified tensions (chosen solitude vs unwanted exclusion; strategic boundary-setting vs avoidance; existential “void” framing).
- Memo 3 (v2) remains viable, but needs an explicit distinction between **instrumental solitude** and **unwanted loneliness**.

## 2026-01-20T14:40:00Z — Phase 2 continues: Batch 4 completed (stability + saturation check)

### Batch 4 (stability check; chosen to avoid “new mechanism chasing”)
Read and excerpt-tagged in `analysis/excerpts_log.md`:
- `/sources_md/Interview_18_part1and2.md` (Male, 23, Hackney)
- `/sources_md/Interview_20_part1and2.md` (Female, 18, Barking)
- `/sources_md/Interview_28_part1and2.md` (Male, 22, Tower Hamlets)
- `/sources_md/Interview_32_part1and2.md` (Male, 24, Tower Hamlets)
- `/sources_md/Interview_39_part1and2.md` (Female, 22, Tower Hamlets)
- `/sources_md/Interview_47_part1and2.md` (Male, 24, Barking & Dagenham)

### Saturation criteria check (per Phase 2 plan)
- **Code stability**: met across Batches 3–4 (12 interviews): no new core codes were introduced; Batch 4 reinforced existing mechanisms.
- **Theme stability**: candidate themes A–E remained stable; only scope/tension clarifications (instrumental solitude vs unwanted loneliness) were needed.
- **Negative-case stability**: we can now name and keep distinct:
  - chosen solitude/introversion (Interview_19, 42, 45)
  - loneliness-as-safety/survival (Interview_41, 45)
  - existential “void” not solved by resources (Interview_43)
- **Evidence sufficiency**: each candidate theme now has multi-interview support and explicit tensions (see `analysis/excerpts_log.md` Batches 1–4).


