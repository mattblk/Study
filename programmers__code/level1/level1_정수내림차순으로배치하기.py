def solution(n):
    _list=[]
    for i in sorted(list(str(n)),reverse=True) :
        _list.append(str(i))
    return int("".join(_list))

    #score 1
