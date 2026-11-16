# Check of answer.md

## Counts

- Disagreements at the level of document and value (recode/disagreements.md): 0.
- Passage-level differences (work/passage_compare_output.md): 11 listed, of which 4 are real disagreements and 7 are not (the same feeling quoted from different words, or unrelated passages paired by word overlap).
- Real disagreements ruled for the rows: 3. Ruled for the second coder: 1. Unsettled by the definition: 0.
- Definition tightened: 1 (in workflow.json, from the second coder's notes in recode/unclear.md), with both documents recoded against it.
- Rows changed: 5 (2 removed, 3 edited). I01 positive goes from 4 to 3; I48 negative goes from 12 to 11.
- Sentences changed in answer.md: 15.

## Rulings on the passage-level differences

Real disagreements:

1. I01, first coder only, positive: "I’ve seen how some people do that the right things with soup kitchens and stuff and I respect and appreciate" [emotions.7nrgg]. For the rows. It comes in their own answer about the shopping centre and names their own feeling (respect, appreciation) about people who run soup kitchens; respect is a positive value in the definition. Kept.
2. I48, first coder only, negative: "puts me in a bad mood" (box 2, being out of work). For the second coder. The bad mood comes from "I think about a lot of stuff" because "I’ve actually been through a lot"; her later answer "Like I said, I’ve been through a lot so sometimes I just remember things and I’m not happy about that" [emotions.87mj7] elaborates the same feeling about the same thing, which the prompt says to code once. Row removed; 87mj7 relabelled "unhappiness, bad mood" about "thinking about past experiences when out of work or alone".
3. I01, second coder only, positive: "I haven’t experienced this too many times in my life, in context I don’t, I’m fortunate in that way". For the rows. "Fortunate" judges their circumstances (rarely lacking support) and names no feeling; the positive value excludes passages with "no feeling named or plainly expressed". Not coded.
4. I01, second coder only, negative: "just not having someone there could also provide the same feeling of helplessness. For me." For the rows. The sentence is about what "people go through" and what not having someone "could" provide, after a hypothetical about being robbed; "For me" reads as "in my view", and in the same answer they say they have not experienced this "too many times". It is a generalised, conditional feeling not tied to an occasion of their own, which the prompt excludes. Their own experience of lacking support is already coded as "I felt unsupported" [emotions.rcepv]. Not coded.

Not disagreements:

5. I01, resentment: the first coder quotes "I feel completely resentment when I walk through those environments and see those people sleeping rough" [emotions.a2qbn], the second "sometimes I feel like um, I feel like quite resentful to systems like councils, governments". Same answer, same feeling about the same thing; both coded it once. No change.
6. I48, crying at night: the first coder quotes "at night before going to bed I sometimes I have to cry myself to sleep because I’m lonely" [emotions.dq9j6], the second "Because I feel lonely." Same feeling about the same thing, coded once by each. No change.
7. I01, "I think I feel quite lonely in that moment" paired with "when I choose to kind of lock myself away ... I think I’m quite at ease with that situation": unrelated passages (the shopping centre; time alone by choice). Both coders coded the first negative and the second positive. No change.
8. and 9. I48, "I feel like I need help sometimes" paired both ways with "I feel like I’m used to it now but sometimes it can get to me.": unrelated passages (constant thinking when alone; having no one to talk to about her day). Both coders coded the first negative and the second mixed. No change.

## Ruling on the second coder's notes (recode/unclear.md)

- I01, "Frustrated, frustrated ... a lack of opportunities can lead to frustration" and "it can feel quite sad. Um, bitter maybe": both coders left these out, rightly. They answer "if you don't have the same opportunities" and "if there's no one to rescue you", hypotheticals in the generalised you. No change.
- I01, "Probably quite sad, annoyed": both left it out, rightly; they answer "If I were to experience what 'thing guy' is experiencing?", a feeling imagined for the figure in the drawing. No change.
- I01, "I’m fortunate in that way": ruled above (3).
- I01, barber shop enjoyment and gratitude; I48, "I wished I had my mom" beside the sadness about friends with their mothers. The prompt said how to treat the same feeling repeated and feelings about different things, but not several different feelings about one thing. Both coders had in practice coded several feelings named in one answer as one row (I48 "it really makes me sad, it makes me feel lonely"; "It’s annoying, sad, lonely.") and a different feeling in a later answer as its own row (I01 loneliness then "quite frustrating"). workflow.json now says so: "Where one answer names several feelings about the same thing, code them as one passage and name them all in the emotion label; where a later answer names a different feeling about the same thing, code that too." The emotion column now allows a list where one passage names several feelings. Recoding I01 and I48 against it:
  - I01: "it feels good to go, um I mean I enjoy the barber shop" and "I’m grateful to see people that I know and have known for a long time fine." are one answer, and the enjoyment is of "the experience I get to have by going there and seeing the same people and knowing that they’re doing well", the same thing the gratitude is about. Merged into one row, "enjoyment, gratitude" [emotions.rcr2x], quoting the whole span exactly.
  - I48: "Just, I wished I had my mom." comes in a later answer (to "what kind of thoughts do normally go through your head?") than the sadness and loneliness, and names a different feeling (longing). Kept as its own row [emotions.asuzr].
  - I48: "It’s annoying, sad, lonely. [pause]. It makes me wish I can do what they do with their siblings." is one answer naming several feelings about friends with siblings. The row now quotes the whole answer and is labelled "annoyance, sadness, loneliness, longing" [emotions.wpafh].
  - No other answer in either interview had two rows for one thing.

## Rows changed (coded/emotions.json)

- Removed: I48 "puts me in a bad mood" (repeat of 87mj7; ruling 2).
- Edited: I48 "sometimes I just remember things and I’m not happy about that." relabelled "unhappiness, bad mood", subject "thinking about past experiences when out of work or alone" (ruling 2).
- Removed: I01 "I’m grateful to see people that I know and have known for a long time fine." (merged into the barber row).
- Edited: I01 barber row extended to the whole span from "it feels good to go" to "have known for a long time fine.", labelled "enjoyment, gratitude", subject "the barber shop and seeing long-known people there doing well" (new id rcr2x, was e49x9).
- Edited: I48 "It’s annoying, sad, lonely." extended to "... It makes me wish I can do what they do with their siblings.", labelled "annoyance, sadness, loneliness, longing" (new id wpafh, was br42h).

## Sentences changed (answer.md)

Opening paragraph:
1. The counts now come first, rephrased so that the table's wording reads correctly; they now read I01 6 negative, 3 positive, 1 mixed and I48 11 negative, 7 positive, 1 mixed.
2. "most of the negative ones are loneliness or close to it" was overstated: loneliness is the label on half of their negative rows and fewer than half of hers. Now "loneliness recurs among the negative ones of both".
3. "counted once per feeling about a given thing" now also says that several feelings named together in one answer count once, following the tightened definition.
4. "They place their loneliness in not being understood and in public settings" left out their breakups [emotions.6ygx6] and named a place generally; now "in not being understood, after breakups and in the shopping centre where people sleep rough".
5. "For them, good feelings come from belonging to a familiar local community; for her, from being with people" left out their ease in time alone [emotions.gqkh7] and respect for soup kitchen workers [emotions.7nrgg], and her love of children, hope and acceptance; now names them, with "mostly" for her.

The person from Newham:
6. "at night ... three feelings at once": they say "shopping centre after 7pm roughly" and also mentions before 7am, and the three feelings are about different things; now "after 7pm ... three feelings".
7. The barber shop sentence now cites the merged row [emotions.rcr2x] for both quotations.

The woman from Barking & Dagenham:
8. "I can’t bring my mom back" was placed among feelings about friends with their mothers; it answers how she feels about not sleeping at night. Now says so and quotes the full words of the row [emotions.z9fyf].
9. The siblings sentence adds her wish to do what they do, citing the extended row [emotions.wpafh].
10. "Alone, she reports a bad mood [emotions.yp3dq] ... unhappy memories [emotions.87mj7]" counted one feeling twice; now quotes 87mj7 alone.
11. "Her positive feelings come almost entirely from company and activity" overstated, since the same paragraph lists hope and acceptance; now "mostly". "Good, relieved" at work is now tied to work and her colleagues, which is what she was asked about, with "I love kids so much" cited separately.
12. "an acceptance that sits uneasily beside her later longing" was the writer's reading; now "sits beside her later longing for her mother" with the longing row cited.

Side by side:
13. The interviewer's words were quoted as "how does that make you feel?" without a speaker id; now paraphrased.
14. "For both, the positive feelings depend on being with familiar people" went against their ease in time alone that they choose; now "Most of the positive feelings of both" and names that row against it.

Limits:
15. "chosen for being short" had no basis in the documents (the question names the two interviews); cut.

recount.py now reports no faults: no citations to missing rows, no bare numbers, no quotation outside its document or its cited row.
