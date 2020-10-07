import itertools
d= [100,200,300,400,500]
budget = 600

def solution(d, budget):
    d.sort()
    i=0
    sum=0
    for n in d:
        i+=1
        sum+=n
        if sum==budget:
            return i
        elif sum>budget:
            return i-1
    return len(d)

print(solution(d,budget))

#6점짜리 greedy 알고리즘 문제였음.....


#전체 조합으로 판단... 좀 오바인 것 같아서 greedy탐색으로 변경
#
# def solution(d, budget) :
#     def min_budget(n,d):
#         str_d = list(map(str,d))
#         sums=[]
#         for i in list(map(" ".join, itertools.combinations(str_d,n))) :
#             tmp = list(map(int,i.split(" ")))
#             sums.append(sum(tmp))
#         return min(sums)
#     for i in range(len(d),0,-1):
#         if min_budget(i,d)<= budget :
#             return i
