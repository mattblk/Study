dic = {0:1}

def DP(result, level, array, target):
    if level<9:
        if result in dic :
            if dic[result] > level:
                dic[result] = level
                if result == target:
                    return level
                for i in range(0,8):
                    DP(result-array[i], level +i+1, array,target)
                    DP(result//array[i], level +i+1, array,target)
                    DP(result*array[i], level +i+1, array,target)
                    DP(result+array[i], level +i+1, array,target)
        else:
            dic[result] = level
            if result == target:
                return level
            for i in range(0,8):
                DP(result-array[i], level +i+1, array,target)
                DP(result//array[i], level +i+1, array,target)
                DP(result*array[i], level +i+1, array,target)
                DP(result+array[i], level +i+1, array,target)



def solution(N, number):
    answer = 0
    array = []
    your_dict = {0:1}
    num = N
    for i in range(0,8):
        array.append(num)
        num = num*10 + N
    DP(0, 0, array, number)
    if(number in dic):
        answer = dic[number]
    else: answer = -1
    return answer
