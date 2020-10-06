s='()()'

def solution(s) :
    c=list(map(lambda k:int(-(ord(k)-40.5)*2),list(s)))
    print(c)
    cumm=0
    for i in c:
        cumm+=i
        if cumm<0:
            return False
    print(cumm)
    if cumm==0 :
        return True
    else:
        return False

print(solution(s))

#4점 9분소요
