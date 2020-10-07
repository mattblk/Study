import heapq
people =[50, 70, 50, 80]
limit = 100
#ans = 3

def solution(people, limit):
    _one_boat_cut=limit-40
    rmv_fr = 0
    rmv_rr=0
    answer =0
    len_people = len(people)
    people.sort()

    for i in range(-1, -len_people-1,-1):
        if people[i] > _one_boat_cut :
            rmv_rr+=1
            answer+=1
        else:
            break

    print(people[:-rmv_rr],answer)


    while True :
        if len_people -rmv_fr-rmv_rr >=2 :
            if people[-rmv_rr-1] + people[rmv_fr] <=limit:
                answer+=1
                rmv_fr+=1
                rmv_rr+=1
            else:
                rmv_rr+=1
                answer+=1
        else :
            if len_people -rmv_fr-rmv_rr == 1 :
                answer+=1
                return answer
            else :
                return answer


print(solution(people,limit))

#12점 sort 한번으로 끝내고  pop은 되도록이면 쓰지 말자 시부럴거
