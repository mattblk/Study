name = 'JEROEN'
def solution(name):
    answer=0
    len_name = len(name)
    intname= list(map(lambda k:abs(abs(ord(k)-78)-13),name))
    cursor = 0
    while True:
        if intname[cursor] !=0:
            answer+=intname[cursor]
            intname[cursor] = 0
        else :
            tmp_fw=0
            tmp_rw=0
            for i in range(len_name):
                if intname[cursor+i] ==0:
                    tmp_fw+=1
                else : break
            for i in range(len_name) :
                if intname[cursor-i] ==0 :
                    tmp_rw+=1
                else :break
            if tmp_fw<=tmp_rw :
                cursor+=tmp_fw
                answer+=tmp_fw
                answer+=intname[cursor]
                intname[cursor]=0
            else :
                cursor-=tmp_rw
                answer+=tmp_rw
                answer+=intname[cursor]
                intname[cursor] = 0
        if sum(intname) == 0 : return answer


print(solution(name))

#13점 59분 소요
