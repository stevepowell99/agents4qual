import json, pathlib

R = [
# I10
("I10", "it’s very exciting meeting new people, especially we do lots of partying so, you know, just spend amazing times with new people", "positive", "excitement, enjoyment", "meeting new people at parties", "connection"),
("I10", "that can allow you to feel lonely. Yes, so that’s something I’ve experienced a lot here", "negative", "loneliness", "putting energy into short-lived party friendships", "loneliness"),
("I10", "I’m more content with it now than I have been, but I think that’s because I now have been here a long time like I have a really really really stable group of friends that, you know, I love them and trust them with everything", "positive", "contentment, love, trust", "her stable group of close friends", "connection"),
("I10", "there are things that you know friendships that I look back on now I think that’s like a massive shame when it makes you…you know, kind of hurts that some people aren’t still in your life", "negative", "hurt, regret", "friendships that faded", "neither"),
("I10", "now I know where to focus my energy, it makes me feel stronger being able to kind of reject that", "positive", "strength", "choosing not to pursue passing friendships", "neither"),
("I10", "it becomes stressful in an already stressful life style, you know, it’s kind of you are adding extra stress to your plate for something that probably doesn’t matter that much, and that’s what causes, you know, upset and distress", "negative", "stress, upset, distress", "spreading herself across too many new people, which she says is where loneliness comes from", "loneliness"),
("I10", "the fact that no one cares, I mean it is horrible because I wish that we could all care about each other as much like as we care about ourselves", "negative", "dismay", "people in the city caring mainly about themselves", "neither"),
("I10", "be focused on what you are doing without, you know, being completely selfish and disregarding everybody else’s feeling. That makes me feel sad.", "negative", "sadness", "selfishness and entitlement", "neither"),
("I10", "I just think it’s ridiculous. It makes me angry, it doesn’t make me sad, it just make me angry.", "negative", "anger", "follower counts and the social media popularity contest", "neither"),
("I10", "I feel like really grateful that I’m not that heavily affected by … you know … something that other women are", "positive", "gratitude", "not being affected by body image pressure from social media", "neither"),
("I10", "she said she just can’t face looking at all the beautiful girls. That breaks my heart", "negative", "heartbreak", "her best friend leaving social media over comparison", "neither"),
("I10", "You know, I love working for myself", "positive", "love, enjoyment", "freelancing and working for herself", "neither"),
("I10", "what I certainly miss is interacting with other people that have a similar skill set as me. I think it’s a real shame", "negative", "missing, regret", "lack of contact with peers as a freelancer", "neither"),
("I10", "I’m also much less anxious than I was when I work within a team", "positive", "ease, less anxiety", "working alone rather than in a team", "neither"),
("I10", "lacking in being able to go and expand your skills, makes me feel like alone from a work sense", "negative", "aloneness", "freelancing without others to develop skills with", "loneliness"),
("I10", "sometimes I get approached and that’s really nice", "positive", "pleasure", "being approached by other creatives to collaborate", "neither"),
("I10", "for me, that was a really difficult thing to hear because I was just like “What?”", "negative", "shock, disbelief", "being refused therapy while in an abusive relationship", "neither"),
("I10", "I felt completely completely unsafe. I was having three panic attacks a day", "negative", "fear, panic", "being in an abusive relationship without help", "neither"),
("I10", "to continually be turned away really makes you feel like \"I’m fucked! I’m never gonna get out of this”", "negative", "hopelessness", "being repeatedly turned away by mental health services", "neither"),
("I10", "I still struggle with drug and alcoholic addiction or misuse or whatever anybody would like to call it. I’m pretty content with it now", "mixed", "struggle, contentment", "her own drug and alcohol use", "neither"),
("I10", "it just makes me so mad because I feel like, if they have given me some help at that point, that my situation might not have gone to the point that it did", "negative", "anger", "not being given help when she asked", "neither"),
("I10", "Say I felt really lonely then, at that point of moment I’ve, you know, under somebody could have made me not feel alone but they didn’t", "negative", "loneliness", "having no help to leave the abusive relationship", "loneliness"),
("I10", "That’s OK, you know, I’m pretty content with it now.", "positive", "contentment", "that past experience, now", "neither"),
("I10", "I’m really glad that I put that time into it", "positive", "gladness", "the years she invested in her career", "neither"),
("I10", "I feel so guilty for not speaking to these people for such a long time", "negative", "guilt", "losing touch with her father's side of the family", "neither"),
("I10", "I just don’t even know how to pick up the phone, because I’m that anxious that they are, like upset with me", "negative", "anxiety", "getting back in touch with relatives", "neither"),
("I10", "my mom’s been through lots of things since I’ve been here and I feel guilty for that as well", "negative", "guilt", "not being there to support her mother", "neither"),
("I10", "I just feel it makes me like, feel sad for myself. I feel like I missed out.", "negative", "sadness, missing out", "family relationships dissolving because of distance and money", "neither"),
("I10", "places I feel most socially connected, there are three bars in this area", "positive", "social connectedness", "local multi-purpose bars and cafés", "connection"),
("I10", "completely green, which is really amazing for us in Hackney, I love things like that", "positive", "love, delight", "a local bar's green, sustainable approach", "neither"),
("I10", "I started to feel really lonely, working alone in the studio", "negative", "loneliness", "working alone in her studio for six months", "loneliness"),
# I38
("I38", "I feel as though I can’t socially connect with them", "negative", "loneliness, disconnection", "being among family and friends whose interests, such as football, she does not share", "loneliness"),
("I38", "I feel lonely, because I feel as though sometimes everyone is busy with their lives and I have no one to go out with", "negative", "loneliness", "being at home while she sees others out on social media", "loneliness"),
("I38", "I do enjoy my own company, but it gets a bit boring on your own enjoying your own company", "mixed", "enjoyment, boredom", "going out on her own", "loneliness"),
("I38", "I think to myself it’s not fair, how do people actually have no responsibilities", "negative", "sense of unfairness", "others' luxury lifestyles on social media", "neither"),
("I38", "There’s me with just my two hundred followers and then you’ve got someone who’s got over fifty thousand followers, it does make you feel as though, oh you know, how do these people get so many followers", "negative", "inadequacy", "comparing her follower count with others'; she says it separates people and leaves you lonely", "loneliness"),
("I38", "I’m content and I feel happier knowing the fact that I do have my stuff", "positive", "contentment, happiness", "her own possessions, without showing them off", "neither"),
("I38", "I felt a bit lonely, because I saw everyone there at the work place, they know what they’re doing, everyone has already made their friendship groups", "negative", "loneliness", "starting her first graduate job", "loneliness"),
("I38", "I missed my social life. I missed the fact that I was able to act, just the freedom", "negative", "missing", "loss of university freedom and social life", "neither"),
("I38", "I felt as if why couldn’t I fit in like that, why do I feel like an outsider", "negative", "feeling an outsider", "seeing university friends' social life at work", "loneliness"),
("I38", "it’s just that constant fear and just trying to please people", "negative", "fear", "being new at work and afraid of getting in trouble", "neither"),
("I38", "I did feel a bit distressed and a bit of anxiety", "negative", "distress, anxiety", "the move from university to work", "neither"),
("I38", "I don’t mind if I don’t if I don’t sit with anyone on my lunch break anymore, I don’t mind if I don’t have anyone to talk to", "positive", "acceptance", "eating lunch alone at work now", "loneliness"),
("I38", "I felt as though I was so robotic when I went to work", "negative", "constraint", "the rigid timetable of work", "neither"),
("I38", "I hated the fact that I accepted it. It was more like, I just felt more like, ugh I’m just so fed up with this nonsense", "negative", "frustration, resentment", "having to accept work's rules", "neither"),
("I38", "I did feel a sense of loneliness in terms of, I felt not dumb…I felt as though I wasn’t capable, I was incompetent", "negative", "loneliness, incompetence", "struggling to find a graduate job while friends found theirs", "loneliness"),
("I38", "I did feel a bit upset, that my friends managed to get a job where they were earning up to 30,000", "negative", "upset", "earning less than her friends", "neither"),
("I38", "slightly envious and jealous like at the fact that how have they fitted in so well and they managed to make a whole bunch of friends when I have been here a couple of months and I don’t even have anyone to have lunch with", "negative", "envy, jealousy", "friends who fitted in at work when she had no one to have lunch with", "loneliness"),
("I38", "I struggle from anxiety in the mornings I have a routine and that needs to be done", "negative", "anxiety", "her morning routine", "neither"),
("I38", "it just makes me feel a bit low, like okay they’re just laughing at me and I just feel like an odd black sheep in the group", "negative", "low mood, feeling the odd one out", "friends laughing at her anxiety", "loneliness"),
("I38", "I felt comfortable talking to them because I felt like they understood me rather than just laughing at me", "positive", "comfort, feeling understood", "someone who listened about her anxiety", "connection"),
("I38", "it was very difficult for them to understand and I felt as though they still look at me weirdly", "negative", "feeling judged as odd", "non-Muslim friends' reactions to her prayer times", "loneliness"),
("I38", "I feel socially accepted in these places", "positive", "acceptance", "the gym and swimming, among semi-strangers", "connection"),
("I38", "it keeps you a sense of happiness and a sense of belongingness", "positive", "happiness, belonging", "the mosque, especially in Ramadan", "connection"),
("I38", "rather than feeling upset and lonely and distance, you feel connected with everyone", "positive", "connectedness", "meals out with friends and family", "connection"),
("I38", "I felt really lonely because obviously I had to make completely new friends when I went to university", "negative", "loneliness", "starting university among people with a drinking and clubbing lifestyle", "loneliness"),
("I38", "I hate stuff like that, I’d rather be at home watching tv in my slippers", "negative", "dislike", "drunken clubbing", "neither"),
("I38", "maybe a bit of an outcast because my friends are not more slim as I am and it had a huge impact on my social life, but as time has gone on and I’ve managed, social media, I just don’t, it doesn’t really interest me and I don’t mind, it’s okay", "mixed", "regret, feeling an outcast, later acceptance", "friends going clubbing without her", "loneliness"),
]

rows = []
for d, q, v, e, s, l in R:
    text = (pathlib.Path("corpus") / f"{d}.txt").read_text(encoding="utf-8")
    if q not in text:
        print("NOT FOUND", d, q[:60])
    rows.append({"document": d, "quote": q, "valence": v, "emotion": e, "subject": s, "link": l})
json.dump(rows, open("coded/emotions.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(rows), "rows")
