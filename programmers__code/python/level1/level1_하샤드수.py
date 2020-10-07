def solution(x):
    m=0
    for i in str(x):
        m+=int(i)
    if x%m == 0 : return True
    else : return False

#score 1
