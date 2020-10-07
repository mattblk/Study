genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

answer = []
__hash = {}
_list_gens = list(set(genres))
tot_plays_gens = {}
print(_list_gens)
for i in range(0,len(_list_gens)):
    __hash[_list_gens[i]] = []
    tot_plays_gens[_list_gens[i]] = 0
for i in range(0, len(genres)):
    __hash[genres[i]].append([i,plays[i]])
for i in range(0,len(_list_gens)):
    __hash[genres[i]] = sorted(__hash[genres[i]], key=lambda k:k[1],reverse=True)

for i in range(0,len(_list_gens)):
    for j in range(0, len(__hash[_list_gens[i]])):
        tot_plays_gens[_list_gens[i]] = tot_plays_gens[_list_gens[i]] + __hash[_list_gens[i]][j][1]

print(__hash)
print(tot_plays_gens)

for i in range(0, len(_list_gens)):
    for j in range(0,2):
        answer.append(__hash[sorted(tot_plays_gens.items(), key=lambda k:k[1], reverse = True)[i][0]][j][0])
        if len(__hash[sorted(tot_plays_gens.items(), key=lambda k:k[1], reverse = True)[i][0]]) ==1:
            break
print(answer)
