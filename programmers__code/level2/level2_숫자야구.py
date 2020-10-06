import itertools
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

def solution(baseball):
    local_case = set()

    def case_creator (pitch) :
        local_case=set()
        if pitch[1] == 3 and pitch[2] ==0 :
            local_case.add(pitch[0])
        elif pitch[1] == 0 and pitch[2] ==3 :
            tmp_list=list(itertools.permutations(str(pitch[0])))
            local_case = local_case | set(map(lambda k:int("".join(k)),tmp_list))
        elif pitch[1] == 0 and pitch[2] ==0:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            tmp_string = "".join(list(map(str,tmp_list)))
            tmp_list=list(itertools.permutations(tmp_string,3))
            local_case = local_case | set(map(lambda k:int("".join(k)),tmp_list))
        elif pitch[1] == 2 and pitch[2] ==0:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            for i in tmp_list:
                local_case.add(int(str(pitch[0])[:2]+str(i)))
            for i in tmp_list:
                local_case.add(int(str(i)+str(pitch[0])[1:]))
            for i in tmp_list:
                local_case.add(int(str(pitch[0])[0]+ str(i)+str(pitch[0])[2]))
        elif pitch[1] == 0 and pitch[2] ==2:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            tmp_list_2ball=list(itertools.permutations(str(pitch[0]),2))
            for i in tmp_list_2ball:
                for j in tmp_list:
                    tmp = list(itertools.permutations("".join(list(i))+str(j)))
                    local_case = local_case | set(map(lambda k:int("".join(k)),tmp))
        elif pitch[1] == 1 and pitch[2] ==2:
            local_case.add(int(str(pitch[0])[0]+str(pitch[0])[2]+str(pitch[0])[1]))
            local_case.add(int(str(pitch[0])[2]+str(pitch[0])[1]+str(pitch[0])[0]))
            local_case.add(int(str(pitch[0])[1]+str(pitch[0])[0]+str(pitch[0])[2]))
        elif pitch[1] == 0 and pitch[2] ==1:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            tmp_list = list(itertools.permutations(tmp_list,2))
            for i in tmp_list:
                local_case.add(int(str(i[0])+str(pitch[0])[0]+str(i[1])))
                local_case.add(int(str(i[0])+str(i[1])+str(pitch[0])[0]))
                local_case.add(int(str(pitch[0])[1]+str(i[0])+str(i[1])))
                local_case.add(int(str(i[0])+str(i[1])+str(pitch[0])[1]))
                local_case.add(int(str(pitch[0])[2]+str(i[0])+str(i[1])))
                local_case.add(int(str(i[0])+str(pitch[0])[2]+str(i[1])))
        elif pitch[1] == 1 and pitch[2] ==0:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            tmp_list = list(itertools.permutations(tmp_list,2))
            for i in tmp_list:
                local_case.add(int(str(i[0])+str(pitch[0])[1]+str(i[1])))
                local_case.add(int(str(i[0])+str(i[1])+str(pitch[0])[2]))
                local_case.add(int(str(pitch[0])[0]+str(i[0])+str(i[1])))
        elif pitch[1] == 1 and pitch[2] ==1:
            tmp_list=[1,2,3,4,5,6,7,8,9]
            for i in str(pitch[0]):
                tmp_list.remove(int(i))
            for i in tmp_list:
                local_case.add(int(  str(pitch[0])[0]  +  str(i)  +  str(pitch[0])[1]  ))
                local_case.add(int(  str(pitch[0])[0]  +  str(pitch[0])[2]  +  str(i)  ))
                local_case.add(int(  str(pitch[0])[2]  +  str(pitch[0])[1]  +  str(i)  ))
                local_case.add(int(  str(i)  +  str(pitch[0])[1]  +  str(pitch[0])[0]  ))
                local_case.add(int(  str(pitch[0])[1]  +  str(i)  +  str(pitch[0])[2]  ))
                local_case.add(int(  str(i)  +  str(pitch[0])[0]  +  str(pitch[0])[2]  ))
        return local_case

    for i in range(len(baseball)) :
        if i==0 :
            local_case =local_case | case_creator(baseball[i])
        else:
            local_case = local_case.intersection(case_creator(baseball[i]))
    return len(local_case)



print(solution(baseball))





#4점,,,,,,,,
