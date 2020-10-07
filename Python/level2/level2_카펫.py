brown=24
red = 24

def solution(brown, red):
    sum_mlt = brown+red
    i=3
    answer =[]
    while True :
        if sum_mlt%i==0 :
            a=i
            b=sum_mlt/a
            if 2*a+2*b-4 == brown :
                answer.append(int(b))
                answer.append(int(a))
                return answer
            else : i+=1
        else : i+=1

print(solution(brown,red))


#2점 23분소요
