def solution(s):
    p=0
    y=0
    for i in s:
        if i.upper()=='P':
            p = p +1
        elif i.upper()=='Y':
            y = y +1
    if p==y :
        return True
    else:
        return False




#4 점
