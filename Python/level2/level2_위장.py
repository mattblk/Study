
arr = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# arr = [[1,1,1],[1,1,1]]
__dict = []
for i in range(0, len(arr)) :
    __dict.append(arr[i][1])
answer = 1
for i in range(0, len(list(set(__dict)))) :
    answer =answer *(__dict.count(list(set(__dict))[i]) + 1)

print(answer)
