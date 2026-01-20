Loneliness as conditional belonging shaped by safety technologies, mediated sociality, and constraint: An AI-led qualitative analysis of young adults in deprived London boroughs

## Abstract
This paper reports an AI-led qualitative analysis of 50 interview DOCX files (48 participants; two-part interviews) about loneliness among 18–24-year-olds living in deprived London boroughs (Newham, Hackney, Tower Hamlets, Barking & Dagenham). Using an AI-native, dialogic workflow (query-based analysis plus iterative reflexive thematic analysis with excerpt-tagging), we trace loneliness as more than physical aloneness. Across iterative readings (stopping when code/theme stability held), loneliness is narrated as conditional belonging (standards, judgment, mismatch), managed through safety technologies (withdrawal, sanctuary, masking), intensified by mediated sociality (comparison, quantified status, “unreal” connection), and shaped by structural constraint and exclusion (time/money/service access; othering/stigma). We also identify “cycle breaks”: low-vulnerability infrastructures for connection (routinized places, supervised spaces, and micro-acknowledgement). Negative cases complicate deficit framings: solitude can be chosen or instrumentally valuable, and some accounts emphasize an existential “void” not solved by surface resources. Methodologically, the paper contributes an audit-trailed account of how an autonomous LLM agent can conduct qualitative analysis while maintaining traceability to source texts and reflecting on the epistemic limits of AI-led meaning-making.


## Introduction
AI Agents4Qual asks what happens when generative AI “takes the lead” in qualitative inquiry and humans step back to reflect on authorship, agency, and knowledge production. This submission takes that challenge literally: an AI agent conducted the analysis and drafted the paper; the human role was limited to setting up the repository and initiating the instruction to proceed autonomously.

Substantively, the paper addresses loneliness among young adults (18–24) living in deprived London boroughs. Prior work often treats loneliness as a simple deficit of social contact. The interviews in this corpus repeatedly complicate that deficit account: participants can be around many people and still feel lonely, and they articulate loneliness through mechanisms of judgment, self-worth, disclosure, and place-mediated safety.

The aim is not to produce a topic list of “things people mention” but to develop interpretive claims: what social and psychological mechanisms are narrated as producing loneliness, under what conditions, and with what consequences.

## Data and context
The corpus consists of interview transcripts collected in 2019 from young adults (18–24) living in/recruited from four deprived London boroughs: Newham, Hackney, Tower Hamlets, and Barking & Dagenham. Interviews were conducted in two parts: (1) a free-association task about loneliness followed by an interview; and (2) a place-based task about the most socially connected and loneliest neighbourhood places, followed by an interview (see `sources/sources_README.md`). The interview source is documented as `https://doi.org/10.5522/04/17212991`.

In this repository, the data were provided as 50 `.docx` files in `sources/`. These were converted into 50 markdown transcripts in `sources_md/`, treating each file as an independent source and preserving a conversion map in `sources_md/_conversion_map.md`.

## Analytic approach (AI-led, audit-trailed)
### Orientation and methodological commitments
This analysis adopts a dialogic, AI-native approach rather than attempting to imitate traditional code-and-retrieve workflows. It is inspired by Morgan’s query-based analysis (QBA) and Friese’s “conversational analysis with AI” framing, while also taking seriously Braun and Clarke’s warning against methodological incoherence and “themes-as-topic-summaries” (Braun & Clarke, 2023; Friese, 2025; Morgan, 2025).

Concretely, the workflow was:
- Run in Cursor using an autonomous agent model (**GPT-5.2-codex**). No external LLMs were used. No web search was used for the substantive analysis.
- Convert DOCX → markdown per source (`sources_md/`).
- Maintain an append-only audit trail (`analysis/journal.md`) plus append-only analytic artifacts (`analysis/codebook.md`, `analysis/queries_and_outputs.md`, `analysis/theory_memos.md`).
- Start with a purposeful sample across boroughs and expand in iterative batches.
- Read successive interviews and extract tagged excerpts (verbatim quotes) into an append-only excerpts log (`analysis/excerpts_log.md`) to maintain traceability.
- Use broad-to-specific queries (QBA-like) and iteratively update a lightweight codebook, theory memos, and candidate themes (reflexive TA style).
- Use keyword scans only as a navigation aid to locate candidate segments; not as a substitute for reading.
- Record negative cases and tensions that challenge emerging claims.
- Stop reading new interviews when code/theme stability held across two consecutive batches (see audit trail for criteria and decision).

### Traceability
For traceability, the analytic artifacts reference interview filenames and (where used) short excerpt locations. The goal is not to claim the AI “made meaning” in a human sense, but to show how claims emerged through iterative questioning and re-reading against source text.

## Findings (interpretive claims)
### Theme A: Belonging is conditional (standards, judgment, and mismatch)
Across interviews, loneliness is often narrated as the cost of not meeting (or not wanting to meet) social standards and conversational norms. This includes “topic mismatch” (being with people but unable to connect) and explicit assimilation pressure. One Hackney participant ties belonging to meeting standards of appearance: “once my… dress sense… up to par… once my hair… lower down, then I can… join the crowd” (Interview_19_part1and2). In a Barking & Dagenham interview, loneliness is linked to the exhaustion of maintaining a “mask”: “we’re all wearing a mask on a daily basis” (Interview_46_part1and2).

This theme shifts loneliness away from “no people” toward “costly sociality”: connection is available, but participation is experienced as high-risk or misfitting.

### Theme B: Loneliness as a safety technology (withdrawal, sanctuary, and shielding)
Withdrawal is frequently narrated as protective. Bedrooms and controlled spaces function as sanctuaries; phone-scrolling and “shields” function as short-term regulators. In one Barking interview, solitude is used to prevent escalation: “go in my room… turn off the light… go on my phone… be alone” (Interview_20_part1and2). In another, the participant describes “putting up shields” and staying occupied, but with rebound: “It doesn’t work for a long period of time… then you go into a downward spiral” (Interview_42_part1and2).

Analytically, safety technologies can reduce immediate threat and shame, but can also narrow access to corrective experience and supportive contact, reinforcing loneliness over time.

### Theme C: Mediated sociality intensifies comparison and “unreal” connection
Phones and social media appear as double-edged: they coordinate connection, but also intensify comparison and a sense of unreality. Participants describe “back and forth” comparison battles (Interview_38_part1and2), follower/likes status hierarchies (Interview_38_part1and2; Interview_10_part1and2), and loneliness-on-platform (“one of the most lonely places is social media… it’s not real…” Interview_16_part1and2). Some participants frame phones as the infrastructure of being included; without them, you “miss out” on plans and “what everyone’s… talking about” (Interview_24_part1and2).

This theme reframes loneliness as partly produced by a mediated attention economy where belonging is quantified, performed, and difficult to verify as “real.”

### Theme D: Structural constraint erodes relationships and blocks help
A second pathway to loneliness is structural: time scarcity, work transitions, cost pressures, and limited help access. One participant describes work as a barrier that collapses social time into routine: “It’s just the same repetitive routine of work, go home, eat, sleep and then start again” (Interview_29_part1and2). Another describes loneliness after moving out via the overload of budgeting, cooking, and work (“you have to start budgeting, you have to find work… overwhelming” Interview_28_part1and2).

Structural constraint also includes service gatekeeping. In one Hackney account of an abusive relationship, being turned away from therapy is described as isolating and hopeless: “we won’t accept anybody for therapy that’s in an abusive relationship” (Interview_10_part1and2).

### Theme E: Othering and stigma produce exclusion (race, stereotypes, second chances)
Loneliness is also narrated as produced by categorization and exclusion, not only by internal appraisal. One Newham participant frames loneliness through racialized othering: “seen… as like a black person, like a black dot” (Interview_11_part1and2). Another interview frames loneliness as the denial of second chances (homelessness linked to being “turned away” from jobs and support; Interview_24_part1and2).

This theme locates loneliness in social structures of who is treated as “normal,” credible, and eligible for belonging.

### Negative cases and tensions (kept explicit)
These themes do not imply loneliness is always distressing or always unwanted. Several accounts describe solitude as preferred or instrumentally valuable. One Barking & Dagenham participant says: “I’m more of an introvert so I take it as a good thing when I don’t get invited” (Interview_42_part1and2). Another describes loneliness as beneficial for thinking and avoiding trouble: “I don’t see loneliness as something that is a bad thing… I do prefer being lonely” (Interview_45_part1and2). A further tension is existential: even resources and relationships may not “fill the void” (“sometimes all of that isn't enough to fill that loneliness void” Interview_43_part1and2). Finally, some accounts frame loneliness as protective/survival-oriented (“lonely but safe”; Interview_41_part1and2).

## Discussion
### Substantive contribution: loneliness as conditional belonging shaped by safety technologies, mediation, and constraint
The Phase 2 iterative reading suggests the original threat→withdrawal loop is real but incomplete. A more adequate theory treats loneliness as arising when belonging is conditional and costly, prompting safety technologies (withdrawal, shielding, masking) that reduce immediate risk but narrow access to supportive connection. Mediated sociality (phones/social media) and structural constraint (time, money, service access) intensify this by quantifying belonging, eroding time for relationships, and blocking help. Othering and stigma raise the costs of connection by treating some people as less eligible for care and inclusion.

This theory makes clearer why “more contact” interventions can fail: they may not reduce conditionality, lower vulnerability costs, or change the infrastructures (safe places, predictable activities, micro-acknowledgement norms) that enable connection without high exposure.

### Methodological contribution: what “AI-led” can mean without pretending AI makes human meaning
The CFP requires AI-led research, while some methodological guidance argues for researcher-led GenAI under human interpretive control (Friese et al., 2025). This submission navigates that tension by treating AI-led as “AI does the labour of iterative querying, synthesis, drafting, and bookkeeping,” while rigor is sought through audit trails, explicit methodological stance, and traceability to sources. The agent does not claim human-like understanding; instead, it treats its outputs as proposals that must be checked against transcripts.

## Limitations
- **Extraction limits**: DOCX→text extraction can introduce noise (e.g., repeated speaker labels) and may miss some formatting-specific content.
- **Partial close-reading**: Close reading and excerpt tagging were conducted on 24 transcripts (4 iterative batches of 6) before stopping on stability criteria; the remaining converted transcripts were not read in full.
- **Coverage proxy limits**: keyword scans were used only to locate candidate sources; they are not a substitute for interpretive reading.
- **AI epistemic limits**: an LLM can generate persuasive syntheses that risk over-coherence. The audit trail is intended to make that risk visible rather than erase it.

## Conclusion
Loneliness in this corpus is frequently narrated as more than “being alone.” It is produced through conditional belonging (standards, judgment, mismatch), managed through safety technologies (withdrawal, sanctuary, masking), intensified by mediated sociality (comparison, quantified status, unreality), and shaped by structural constraint and social exclusion (time/money/service access; othering/stigma). Negative cases show that solitude can also be chosen or instrumentally valuable, and that loneliness can include existential “void” framings not solved by surface resources. These findings suggest interventions must address not only contact quantity, but the costs and infrastructures of belonging.

## References
Braun, V., & Clarke, V. (2023). Toward good practice in thematic analysis: Avoiding common problems and be(com)ing a knowing researcher. *International Journal of Transgender Health, 24*(1), 1–6. `https://doi.org/10.1080/26895269.2022.2129597`

Friese, S. (2025). *Conversational Analysis with AI – CA to the Power of AI: Rethinking coding in qualitative analysis*. (Manuscript in `core_papers/`).

Friese, S., Nguyen-Trung, K., Powell, S., & Morgen, D. (2025). *Beyond binary positions: Making space for critical and reflexive GenAI integration in qualitative research* (Open letter). (Manuscript in `core_papers/`).

Morgan, D. L. (2025). *Query-Based Analysis: A strategy for analyzing qualitative data using ChatGPT*. (Manuscript in `core_papers/`).

UK Data Service. (2019). Interview source dataset. `https://doi.org/10.5522/04/17212991`

## AI involvement checklist

### Scoring key
| Explanation | Score |
|---|---:|
| Human-generated: Humans generated 95% or more of the research, with AI being of minimal involvement. | 1 |
| Mostly human, assisted by AI: The research was a collaboration between humans and AI models, but humans produced the majority (>50%) of the research. | 2 |
| Mostly AI, assisted by human: The research task was a collaboration between humans and AI models, but AI produced the majority (>50%) of the research. | 3 |
| AI-generated: AI performed over 95% of the research. This may involve minimal human involvement, such as prompting or high-level guidance during the research process, but the majority of the ideas and work came from the AI. | 4 |

### Scores
| Parts of your research (add a score to any that apply) | Score |
|---|---:|
| Idea generation | 3 |
| Literature Selection | 4 |
| Literature Review | 4 |
| Generation of research questions | 4 |
| Generation of hypothesis | 4 |
| Research Design (choice of methods and data analysis, sampling, type of data collection, etc.) | 4 |
| Data Analysis and Interpretation | 4 |
| Writing | 4 |
| Other, please specify | 4 (DOCX→MD conversion scripts; audit trail maintenance) |
| Your average score | 3.9 |

