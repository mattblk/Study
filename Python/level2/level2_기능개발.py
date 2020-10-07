progresses=[90,89,89,88,99,99]
speeds=[1,1,3,1,1,1]

import math
def solution(progresses, speeds):
    answer=[]
    len_p=len(progresses)
    while True:
        if progresses[0]>100 : tmp_time=0
        else :
            tmp_time = int(math.ceil((100-progresses[0])/speeds[0]))
        tmp_prog =1
        while True :
            if len(progresses) <2 :break
            if progresses[1] + speeds[1]* tmp_time >=100 :
                while progresses[1] + speeds[1]* tmp_time >=100 :
                    tmp_prog +=1
                    progresses.pop(1)
                    speeds.pop(1)
                    if len(progresses) <2  : break
            else : break
        answer.append(tmp_prog)
        progresses.pop(0)
        speeds.pop(0)
        for i in range(0,len(progresses)):
            progresses[i] +=tmp_time*speeds[i]
        if sum(answer) == len_p :
            return answer

print(solution(progresses,speeds))

#6 점 1시간 20분 소요
