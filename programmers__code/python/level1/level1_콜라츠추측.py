def solution(num):
    if num==1 :return 0
    i = 0
    while True :
        i+=1
        if num%2 ==0 : num/=2
        else : num = num*3 +1
        if num==1: return i
        elif i>=500 : return -1

        #score 5
