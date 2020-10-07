from math import sqrt
def solution(n):
    if sqrt(n)%1 == 0 :
        return int(pow(sqrt(n)+1,2))
    else : return -1

#score 6
