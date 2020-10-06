priorities =[2, 1, 3, 2]
location = 2

def solution(priorities, location):
    time = 1
    location = location

    while True :
        max_idx = priorities.index(max(priorities))
        if max_idx == location : return time
        elif max_idx>location : location = location + len(priorities[max_idx+1:])
        else : location = location - len(priorities[:max_idx])-1
        # print(max_idx,location)
        priorities = priorities[max_idx+1:] + priorities[:max_idx]
        time+=1

print(solution(priorities,location))


#4점 32분 소요
