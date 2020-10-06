def solution(n, lost, reserve):
    answer=0
    tot=[1]*n
    for i in lost :
        tot[i-1] = tot[i-1] -1
    for i in reserve:
        tot[i-1] = tot [i-1]+1
    for i in range(n):
        if tot[i] == 0:
            if i+1>=2 and tot[i-1]>=2:
                tot[i-1] = tot[i-1] -1
                tot[i] = tot[i]+1
            elif i+1<=n-1 and tot[i+1] >=2:
                tot[i+1] = tot[i+1]-1
                tot[i] = tot[i] +1
    for i in tot:
        if i>=1:
            answer = answer+1
    return answer
