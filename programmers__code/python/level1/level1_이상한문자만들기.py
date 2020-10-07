def solution(s):
    _list = s.split(" ")
    answer = ''
    def sub(string):
        k=0
        sub_ans=''
        for i in string:
            if i==' ' : sub_ans+=' '
            elif k%2 == 0 : sub_ans+=i.upper()
            else : sub_ans+=i.lower()
            k=k+1
        return sub_ans
    for i in _list :
        answer+=sub(i)+" "
    return answer[:-1]

#score 12
