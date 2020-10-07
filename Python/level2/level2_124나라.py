n = 10 # 12
def solution(n):
    answer=''
    while True:
        if n%3 == 0 :
            answer ='4'+answer
            n=n//3 -1
        elif n%3 == 1:
            answer = '1' +answer
            n=n//3
        else :
            answer = '2' +answer
            n=n//3
        if n == 0 : break
    return answer

print(solution(n))

#6점  16분
