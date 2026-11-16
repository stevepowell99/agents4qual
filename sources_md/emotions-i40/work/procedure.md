# Procedure

- Documents read: corpus/I40.txt only (the sample step `one`), read in full by the analyst.
- Coding: the analyst applied the code step `emotions` in workflow.json (definitions carried over unchanged from the I10/I38 run, with a sentence added saying what makes a passage weak for valence). The rows were written by work/code_rows.py, which checks every quotation against the document, into coded/emotions.json. coded/emotions.json, with recount/rows.md, is the per-document table of passages bearing on the question.
- Recount: recount.py recounted the tables from the rows (work/recount_output.txt).
- Second coder: a fresh helper (Sonnet) coded I40 afresh under work/brief_recode.md (the plugin's recode brief, documents "all of them"), writing recode/coded/emotions.json and recode/unclear.md; recode/disagreements.md comes from compare.py (work/compare_output.txt).
- Check: a fresh helper (Opus) worked under work/brief_check.md (the plugin's check brief with the question filled in), also asked to compare the two codings row by row since there is one document. It ruled on the passages, corrected coded/ and answer.md, recounted, and wrote check.md.
- The answer's counts are cell ids resolved by recount.py into recount/answer.resolved.md.
