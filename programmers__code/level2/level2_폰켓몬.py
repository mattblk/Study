nums=[3,3,3,2,2,2]

def solution(nums):
    setnum=list(set(nums))
    if len(setnum) >= len(nums)/2 :
        return len(nums)/2
    else :
        return len(setnum)
print(solution(nums))
