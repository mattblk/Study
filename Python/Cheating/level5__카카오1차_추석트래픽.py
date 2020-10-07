def time2durationSec (time):
    lst = time.split(' ')
    end = lst[1]
    duration = lst[2]
    # print(end, duration)
    lst2= end.split(':')
    hour = int(lst2[0])*1000
    minu = int(lst2[1])*1000
    sec = int(lst2[2][0:2] + lst2[2][3:])
    micsec = hour*3600 + minu*60 + sec
    lst3 = duration[:-1].split('.')
    if len(lst3)>1:
        duration2 = int(lst3[0])*1000 + int(lst3[1]+('0'*(3-len(lst3[1]))))
    else: duration2 = int(lst3[0])*1000

    # print([micsec-duration2, micsec])
    return [micsec-duration2 + 1, micsec]

def checkProcessNum (time, lst):
    num = 0
    start = time
    end = time + 1000
    for duration in lst:
        if not (duration[1] < start or duration[0] >= end):
            num += 1
    return num

def solution(lines):
    answer = 0
    lst = []
    count = []
    for string in lines:
        lst.append(time2durationSec(string))
    print(lst)
    for i in lst:
        print(i)
        count.append(checkProcessNum(i[0], lst))
        count.append(checkProcessNum(i[1], lst))

    return max(count)
