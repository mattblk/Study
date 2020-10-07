skill='CBD'
skill_trees =['BACDE', 'CBADF', 'AECB', 'BDA']

def solution(skill, skill_trees):
    answer = 0
    for usr in skill_trees :
        is_err=0
        index_arr=[]
        for i in skill:
            if i in usr :
                index_arr.append(usr.index(i))
            else :
                index_arr.append(99)
        for i in range(len(index_arr)-1) :
            if index_arr[i]>index_arr[i+1]:
                is_err+=1
                break
        if is_err == 0 :
            answer+=1
    return answer

print(solution(skill,skill_trees))

#5점 46분소요
