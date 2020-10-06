# import itertools
# numbers="173"
#
# def solution(numbers):
#     def soin(num):
#         if num<2:
#             return False
#         for i in range(2, num+1):
#             if i==num :
#                 return True
#             if num % i==0:
#                 return False
#     pool = list(numbers)
#     _list=[]
#     for i in range(1,len(numbers)+1):
#         tmp = list(map(''.join, itertools.permutations(pool,i)))
#         _list = _list + tmp
#     _list = [int(i) for i in _list]
#     _list = list(set(_list))
#     answer=0
#     for i in _list:
#         if soin(i):
#             answer = answer +1
#     print(_list)
#     return answer
# print(solution(numbers))


import itertools
def solution(numbers):
    def soin(num):
        if num<2:
            return False
        for i in range(2, num+1):
            if i==num :
                return True
            if num % i==0:
                return False
    comb= list(itertools.combinations(numbers,3))
    sums=[]
    for i in comb:
        sums.append(sum(i))

    answer = 0
    for i in sums:
        if soin(i):
            answer = answer +1

    return answer
