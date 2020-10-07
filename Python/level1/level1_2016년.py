a=5
b=24
def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    week=['THU','FRI','SAT','SUN','MON','TUE','WED']
    th=0
    for i in range(a-1):
        th=th+month[i]
    th= th +b
    answer = th
    return week[th%7]
print(solution(a,b))
