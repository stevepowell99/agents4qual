# Core papers — one-page summaries (append-only)

## 2026-01-20T??:?? — Initialized

Purpose: store one-page summaries of each PDF in `/core_papers/`, plus methodological “rules” adopted/rejected.

## 2026-01-20T??:?? — Morgan (2025) — Query-Based Analysis (QBA)

### What the paper is doing
Morgan proposes **Query-Based Analysis (QBA)** as an alternative to “code-then-theme” workflows in qualitative analysis when using LLMs like ChatGPT. Instead of fragmenting data into many small codes and re-assembling themes, QBA starts with **broad queries** to generate initial summaries/topics and then iteratively **narrows** via follow-up queries, ending by checking **supporting data** (e.g., returning to source excerpts) to verify and refine interpretations.

### Core claims (high-signal)
- Coding-based CAQDAS is “computer-assisted”: it organizes *human* coding rather than analyzing. LLMs change the landscape by enabling **conversational interrogation** of data.
- QBA is explicitly **inductive**: it avoids pre-specifying themes (deductive), but reaches interpretive conclusions by progressive questioning rather than code aggregation.
- Practical guidance includes controlling randomness (e.g., “temperature” set low) and privacy settings (don’t retain data for training), plus acknowledging that large datasets may require preprocessors/tools.

### Methodological significance for Agents4Qual
QBA gives a defensible *process* for AI-led analysis: you can show the research unfolded as a sequence of queries → answers → checks against source material. That maps well to the conference’s emphasis on transparency and “what happened when AI took the helm” (and fits our append-only log requirement).

### Rules for this repo (adopt / reject)
- **Adopt**: structure analysis around **explicit, logged query sequences** (broad → specific → evidence-check) in `analysis/queries_and_outputs.md`.
- **Adopt**: treat “supporting data” as mandatory: every substantive claim should point to specific interview files (and, where needed, short quotes).
- **Reject (for our dataset)**: combining all interviews into one mega-document (Morgan’s example does this for thematic commonality); we will keep interviews as independent sources and only aggregate at the level of comparisons/syntheses.

## 2026-01-20T??:?? — Braun & Clarke (2023) — Toward good practice in thematic analysis

### What the paper is doing
Braun & Clarke respond to widespread “thematic analysis” usage by clarifying what counts as **methodologically coherent** TA and what common problems undermine it. A key message is to become a **“knowing researcher”**: own your perspective (personal + theoretical), make deliberative choices, and be reflexive—rather than treating TA as a recipe.

### Core claims (high-signal)
- **TA is a family of methods**, not a single standardized procedure. They distinguish (among others) **coding reliability TA (small q/positivist)** vs **reflexive TA (Big Q/non-positivist)**, plus codebook approaches.\n+- A major failure mode is **methodological incoherence** (“mash-ups”): e.g., claiming reflexive TA while doing intercoder reliability/consensus coding, or talking about “bias” as contamination while also invoking reflexivity.\n+- Another failure mode is confusing **themes-as-topic-summaries** with **themes-as-meaning-unifying interpretative stories** (themes should do explanatory/interpretive work, not just list topics).

### Methodological significance for Agents4Qual
This paper gives a sharp criterion to avoid “AI theme-dumps”: our outputs must be **interpretive stories** (with an owned stance) rather than surface topic clustering. It also helps us explicitly justify which “TA-like” commitments we are (and are not) making—important because an AI-led process can otherwise drift into incoherent hybrids.

### Rules for this repo (adopt / reject)
- **Adopt**: treat “themes” as **interpretive claims** (meaning-unifying stories), not topic headings.\n+- **Adopt**: explicitly document **paradigmatic commitments** (Big Q-ish, reflexive orientation) in `analysis/methodology_stance.md` and avoid importing small-q “reliability” rituals that don’t fit.\n+- **Reject**: “methodolatry/proceduralism” (doing steps because a checklist says so). Our audit trail must show *reasons*, not just *steps*.

## 2026-01-20T??:?? — Friese (2025) — Conversational Analysis with AI (CAAI / “CA to the Power of AI”)

### What the paper is doing
Friese argues that generative AI pressures us to reconsider the **centrality of coding**. She proposes **Conversational Analysis to the Power of AI (CAAI)**: a dialogic framework where analysis is conducted through structured interaction with an LLM (iterative questioning, synthesis, contrast), explicitly positioning this as more than shallow “classification proxies.”

### Core claims (high-signal)
- Many “LLM qualitative coding” papers are really **classification** (few categories, pre-chunked text), which loses continuity and interpretive depth.\n+- CAAI reframes analysis as researcher-led inquiry: the LLM retrieves/synthesizes contrasts in response to questions.\n+- The method is described as **four iterative steps** plus an optional **fifth** for theory building:\n+  - Step 1: get to know data via summaries + preliminary themes.\n+  - Step 2: prepare for analysis by selecting a topic and crafting guiding questions (researcher-owned, documented for transparency).\n+  - Step 3: ask questions (start with a focused subset to avoid generic smoothing).\n+  - Step 4: (implied continuation) integrate, compare, and refine through dialogue.\n+  - Optional Step 5: theory-building.\n+
### Methodological significance for Agents4Qual
CAAI offers a rigorous story for “AI-led qualitative analysis” that is still **traceable**: the unit of work becomes a logged sequence of questions and outputs rather than a code list. It also gives concrete warnings about overfeeding the model and getting generic summaries—relevant for a 48-participant corpus.

### Rules for this repo (adopt / reject)
- **Adopt**: treat the analysis as **topic-by-topic dialogic inquiry** with an explicit question set (logged) rather than “code everything first.”\n+- **Adopt**: start with smaller subsets when depth is needed; expand only after the question set stabilizes.\n+- **Reject**: paragraph-level chunking/classification as a substitute for interpretive analysis.

## 2026-01-20T??:?? — Friese et al. (2025) — Open Letter: Beyond binary positions (GenAI in qualitative research)

### What the paper is doing
This open letter responds to calls for categorical exclusion of GenAI from reflexive qualitative research. The authors argue against binary framings (pro/anti AI) and propose a stance of **critical, reflexive, ethically responsible** GenAI integration—typically with **human interpretive agency** retained.

### Core claims (high-signal)
- GenAI does not “make meaning” like humans, but can still be used as a **supportive tool** under researcher control.\n+- They emphasize transparency, methodological literacy, and responsibility (including environmental/labour harms).\n+- They highlight that some automation-focused uses align with “small q” mechanization, which they critique; they prefer iterative, abductive, dialogic collaboration where humans remain accountable.

### Methodological significance for Agents4Qual
This paper creates a productive tension with the CFP: it advocates **researcher-led** GenAI, while Agents4Qual explicitly demands **AI-led** research. We need to explicitly acknowledge this tension and explain what “AI-led” means *without* pretending the AI has human-like meaning-making—i.e., the agent performs the analytic labour and writing, while responsibility/ethics are handled via transparent disclosure and audit trail.

### Rules for this repo (adopt / reject)
- **Adopt**: explicit transparency about roles, limitations, and harms; keep methodological reflection live throughout `analysis/journal.md` and `analysis/methodology_stance.md`.\n+- **Adopt**: treat LLM outputs as *proposals* requiring verification against sources, even in an AI-led workflow.\n+- **Reject**: both absolutist rejection and “anything goes” enthusiasm; we’ll document constraints and decisions explicitly.

