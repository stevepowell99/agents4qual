# Procedure

## Corpus

The 48 interview transcripts (Markdown converted from Word) were turned into one plain-text file each in `corpus/`, with `corpus/index.csv` giving id, title, file, gender, age and borough from each file's header. Two files holding only part 2 of interviews 13 and 14 were left out, as the combined files already hold both parts.

## Question

Settled with the evaluator before any coding: four theories (discrepancy; Weiss's emotional and social loneliness; Cacioppo's self-reinforcing loop; social media as displacing or compensating), a random sample of 12 stratified by borough, first-hand accounts only, base the 12 sampled interviews, pitched as a methods demonstration. The full wording is `question_as_agreed` in `workflow.json`.

## Sample

The sample step in `workflow.json` (n 12, stratified by borough) uses the engine's seeded draw. `work/scripts/draw_sample.py` prints which documents it takes; the output is `work/sample_drawn.txt`: I05, I06, I10, I11, I17, I18, I21, I32, I39, I41, I43, I45.

## Codebook

`work/scripts/make_workflow.py` writes `workflow.json`: four per-document code steps, one per theory, each with one nominal column whose values (supports, contradicts, both, no_evidence; for social media, displaces, compensates, both, no_evidence) are defined with what counts and what does not; a tabulation of each; and the write step.

## Reading and coding

Four subagents each read three sampled interviews in full (one borough each) and coded every interview against all four code steps, applying the definitions in `workflow.json`. Briefs: `work/subagents/brief_template.md` and `work/subagents/<group>_brief.md` (groups newham, hackney, bd, th). Returns: `work/subagents/<group>_return.json`, each row with document, step, value, an exact quotation, a second quotation where the value is both, and a one-sentence reason. The analyst reviewed every returned row against its quotation, and checked context in the transcript where a value was borderline.

## Combining

`work/scripts/build_coded.py` turns the returns into `coded/<step>.json` (one row per document per step) and the evidence table `work/evidence_table.md`. `recount.py` recounts the workflow from those rows (`work/recount_1.txt`), then checks the answer (`work/recount_2.txt`, `work/recount_3.txt`); every count in `answer.md` is a cell id, and every citation a row id from `recount/rows.md`.
