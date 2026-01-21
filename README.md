# A repo to write a social research paper (in Cursor IDE) entirely by GenAI.

## Abstract
This repo is the source material for a paper in January 2026 submitted to agents4qual. 

The paper reports qualitative analysis conducted entirely by AI of 50 interviews (48 participants; two-part interviews) about loneliness among 18–24-year-olds living in deprived London boroughs. No dedicated software was used; instead, the entire project was conducted inside Cursor Integrated Development Environment (IDE), a generic tool for conducting AI-supported tasks which also gives the AI access to tools like Word document conversion and creation and editing of journal files. The author gave the AI a high-level methodological instruction and four methods papers to read, with the instruction to develop an overall thematic analysis methodology of its own choosing. The AI planned and then implemented a workflow (query-based analysis plus iterative reflexive thematic analysis with excerpt-tagging) and produced an initial draft. The author intervened just once to suggest how to deepen the analysis. The results of this second iteration is the present paper. The total process took less than 60 minutes. 
Substantively, we trace loneliness as more than physical aloneness. Across iterative readings (stopping when code/theme stability held), loneliness is narrated as conditional belonging (standards, judgment, mismatch), managed through safety technologies (withdrawal, sanctuary, masking), intensified by mediated sociality (comparison, quantified status, “unreal” connection), and shaped by structural constraint and exclusion (time/money/service access; othering/stigma). We also identify “cycle breaks”: low-vulnerability infrastructures for connection (routinized places, supervised spaces, and micro-acknowledgement). Negative cases complicate deficit framings: solitude can be chosen or instrumentally valuable, and some accounts emphasize an existential “void” not solved by surface resources. Methodologically, the paper contributes an audit-trailed account of how an autonomous LLM agent can design and implement a qualitative analysis while maintaining traceability to source texts. 

## Repo structure (what’s in here and why)

This repo is intentionally simple: raw sources, derived text, a small number of append-only “research logbooks,” a small set of scripts, and the final submission files.

### Primary outputs
- `paper_submission.md`: the main submission text (the “paper”).
- `paper_submission.pdf`: exported PDF of the submission (for convenience).
- `paper_submission_edit.md`: a working/editing copy (if you need to experiment without touching the submission draft).

### Data (raw + derived)
- `sources/`: the original interview files as provided (DOCX). Also includes `sources/sources_README.md` describing the dataset/interview structure.
- `sources_md/`: derived transcripts (one Markdown file per source DOCX) created by the conversion script. Includes `sources_md/_conversion_map.md` linking each DOCX to its derived transcript file.

### Analysis logbooks (append-only audit trail)
All files in `analysis/` are intended to be append-only (new dated entries are added; older entries are not silently rewritten).

- `analysis/journal.md`: chronological “what I did and why” research diary (including method changes and correction notes).
- `analysis/excerpts_log.md`: short verbatim excerpts (quotes) tagged with codes/themes and notes; this is the core traceability artifact for the Phase 2 iteration loop.
- `analysis/codebook.md`: evolving code definitions with inclusion/exclusion notes and examples.
- `analysis/theory_memos.md`: evolving theory claims, scope conditions, and negative cases.
- `analysis/queries_and_outputs.md`: the major analytic questions asked of the corpus (query-led analysis) and summarized outputs + evidence pointers.
- `analysis/methodology_stance.md`: the methodological “stance” memo (contentious issues from core papers and what approach I adopted here).
- `analysis/core_papers_onepagers.md`: one-page summaries of the core methods papers and their methodological implications.
- `analysis/core_papers_text/`: extracted plain-text dumps of the core paper PDFs (used as inputs to the one-page summaries).
- `analysis/template_dump.txt` and `analysis/template_tables.txt`: extracted structure/tables from the Agents4Qual template document (used to format the submission + checklist).
- `analysis/notebooks_compiled_verbatim.pdf`: compiled “notebook-style” verbatim notes/export (for convenience/archiving).

### Conference materials
- `call/`: the Agents4Qual announcement + call-for-papers HTML files and the required submission template DOCX.

### Core methods papers
- `core_papers/`: the provided PDF methods papers that the AI used to justify its analytic approach.

### Scripts (automation helpers)
- `scripts/convert_sources_docx_to_md.py`: converts `sources/*.docx` into `sources_md/*.md` and writes the conversion map.
- `scripts/extract_core_papers_text.py`: extracts text from `core_papers/*.pdf` into `analysis/core_papers_text/`.
- `scripts/scan_sources_md_for_low_content.py`: flags derived transcripts with very low substantive content (conversion quality check).
- `scripts/wordcount_paper.py`: word-count helper for the submission draft.

### Notes on duplication
- `method_README.md` contains the original project brief/instructions that kicked off the AI-led workflow. This `README.md` is a short repo overview + abstract.


