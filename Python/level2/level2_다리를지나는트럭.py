bridge_length = 4
weight = 100
truck_weights = [10]

def solution(bridge_length, weight, truck_weights):
    on_br=[0]*bridge_length
    truck_weights.reverse()
    time=0

    def time_lapse(list):
        _num_zero =0
        for i in range(len(list)-1,-1,-1) :
            if list[i]==0: _num_zero+=1
            else : break
        list = [0]*_num_zero + list[:-_num_zero]
        return (list,_num_zero)


    while True :
        for i in range(bridge_length-1,0,-1):
            on_br[i]= on_br[i-1]
        on_br[0] = 0
        time+=1
        if len(truck_weights) !=0 :
            if sum(on_br)+truck_weights[-1] <= weight :
                on_br[0] = truck_weights.pop()
            else:
                if on_br[-1] == 0:
                    on_br, dr_time = time_lapse(on_br)
                    time+=dr_time
                else :
                    on_br[0] = 0
        else :
            if on_br[-1] == 0 and sum(on_br)!=0:
                on_br, dr_time = time_lapse(on_br)
                time+=dr_time
            else :
                on_br[0] = 0
        if sum(on_br) == 0: return time

    return answer

print(solution(bridge_length,weight,truck_weights))


#6점 
