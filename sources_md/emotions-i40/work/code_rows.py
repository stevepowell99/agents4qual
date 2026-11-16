import json
T=open('corpus/I40.txt',encoding='utf-8').read()
R=[
("When I'm on the tube, you don't know anyone when you’re on the tube. So that’s kind of way I guess I feel lonely that's the most lonely place I can kind of think of.","negative","loneliness","being on the tube among strangers","loneliness",0),
("I don't know it just feels like just feel something you dealing with…something you just want to get through","negative","resignation","tube journeys among strangers","neither",1),
("Pretty crowded. Yeah I don't like that I hate…when it gets really crowded everyone is just in everyone’s personal space…you know…you just feel really awkward I guess.","negative","dislike, awkwardness","crowded tube, personal space invaded","neither",0),
("It’s just a bit maybe a bit stressful like again I was just like I would like to get over and get done quickly when the space opens up the train I feel like relieved now","mixed","stress, relief","packed train, then space opening up","neither",0),
("So, the whole ride was just nervous. But I end up in the right place. So, it just makes you uneasy I guess the whole time and I was alone by myself so made me feel quite nervous.","negative","nervousness","alone in a cab abroad after getting lost on holiday","loneliness",0),
("the exact same situation happened to me in another holiday with my mate I was having one person with me, and I was complete I almost didn't care","positive","ease","lost on holiday with a friend beside him","connection",1),
("being alone I wouldn’t say is something I don't like…sometime I’d like to… I would like to you know just go somewhere by myself","positive","liking time alone","doing errands or the gym by himself","loneliness",0),
("It’s just really local to everyone that's what I feel yeah…yeah feel most socially connected.","positive","social connectedness","local hang-out by the football pitch","connection",0),
("Just very, very comfortable.","positive","comfort","local hang-out where faces are familiar","connection",0),
("It just feels lonely ‘cause there’s no one I know there, not at all","negative","loneliness","Liverpool Street, where he knows no one","loneliness",0),
("Yeah when it’s busy, crazy like that…I don't really like it.","negative","dislike","busy, rushing city","neither",0),
("It makes me feel like…I wanna quickly get in and out of that place that…seems like everyone else is doing that as well …seems like everyone is alone as well. That’s why I feel lonely I guess over there.","negative","urge to get away","Liverpool Street crowds of people alone","loneliness",0),
("I mean…I enjoy living here.","positive","enjoyment","living in London next to the city","neither",0)]
rows=[]
for q,v,e,s,l,wk in R:
    assert q in T, q[:40]
    r={"document":"I40","quote":q,"valence":v,"emotion":e,"subject":s,"link":l}
    if wk: r["weak"]=True
    rows.append(r)
json.dump(rows,open('coded/emotions.json','w'),indent=1,ensure_ascii=False); print(len(rows))
