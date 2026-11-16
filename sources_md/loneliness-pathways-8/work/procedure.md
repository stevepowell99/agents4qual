# Procedure

## Documents

The evaluator chose eight interviews from the 48 in corpus/ (I08, I10, I18, I22, I27, I39, I41, I43), the same eight as an earlier pilot run on vulnerability and resilience. The sample step `s8` in workflow.json names them. corpus/ is a copy of the documents folder's corpus at the time of the run.

## First reading and coding (the analyst)

1. The analyst read each of the eight interviews in full and noted every passage in which the interviewee says one thing leads to, deepens or keeps going loneliness, or something on a chain to it, with free labels for cause and effect and whose experience it was. These open notes are work/open_I08_I10.json, work/open_I18.json, work/open_I22.json, work/open_I27.json, work/open_I39.json and work/open_I41.json (I43's notes were kept in the analyst's working notes and coded directly).
2. The analyst grouped the free labels into a list of 16 factors, each defined with what counts and what goes elsewhere, plus two further columns: role (onset or maintaining) and whose (own or others). The definitions are the columns of step `c_links` in workflow.json, written by work/scripts/build_workflow.py.
3. The analyst coded every link against that list, one row per link with the passage copied exactly; work/scripts/build_rows.py holds this first coding and wrote coded/c_links.json (103 rows). During this pass the role of seven rows was changed from maintaining to onset and the role definition tightened, so that withdrawing or anxiety arising from something other than loneliness counts as onset.
4. recount.py recounted the workflow from the rows (outputs work/recount_run1.txt to work/recount_run3.txt); a quotation not found in its document was corrected and the recount rerun until clear. work/scripts/evidence_table.py wrote work/evidence.md, the table of every coded link by document with its quotation (from the first coding; recount/rows.md holds the rows as they now stand).
5. The analyst wrote a first answer.md citing cell ids and row ids, checked it with recount.py --answer (work/recount_answer1.txt, work/recount_answer2.txt) and removed bare numbers.

## Second reading

6. A second coder (a fresh Sonnet subagent, brief in work/briefs/recode_brief.md, return in work/briefs/recode_return.md) coded the same eight interviews to the same definitions without seeing the first coding, writing recode/coded/c_links.json (147 rows) and recode/unclear.md. workflow.json and corpus/ were copied into recode/, recount.py recounted it (work/recount_recode.txt) and compare.py wrote recode/disagreements.md (work/compare_output.txt).
7. A checker (a fresh Opus subagent, brief in work/briefs/check_brief.md, return in work/briefs/check_return.md) read all eight interviews, ruled on each disagreement against the definitions, corrected coded/c_links.json (now 107 rows; these corrections supersede build_rows.py), tightened one definition in workflow.json, added the tabulation t_linkrolewhose, checked every sentence and quotation of answer.md against the documents, rewrote it and wrote check.md.

## Combining into the answer

8. Every count in the answer is a cell of a tabulate step recounted by code from coded/c_links.json: t_links and t_map (links by cause and effect, the map showing links stated by at least two interviewees, with the catch-all "Other cause" excluded), t_paths (paths joined within each interviewee's own links), t_role, t_roleonly, t_linkwhose, t_linkrolewhose and t_rolewhose (by role and by whose experience). Every citation is a row id from recount/rows.md. The analyst then added one section cross-reference, reran recount.py --answer (work/recount_final.txt) and rendered the report with render_report.py.
