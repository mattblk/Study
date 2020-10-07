def solution(n):
    answer=list()
    if n==1: return 1

    for i in range(1,n):
        if i%2 !=0:
            if n%i == 0 and (n/i-i//2)>=1:
                answer.append(i)
        else :
            if n/i-n//i==0.5 and (n/i-i/2)>=0.5:
                answer.append(i)

    return len(answer)

print(solution(15))
