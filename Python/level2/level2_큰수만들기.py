number ='21211111'
k =6
def solution(number, k):
    del_count = 0
    rear=list(number)
    rear.reverse()
    front=[]
    now=[]
    for i in range(2):
        now.append(rear.pop())

    while True:
        if now[0]<now[1] :
            if len(front) == 0:
                now[0] = now[1]
                if len(rear) == 0 :
                    now.pop()
                    del_count +=1
                    del_remain = k-del_count
                    tmp_str = front + now
                    for i in range(del_remain):
                        tmp_str.pop()
                    return ''.join(tmp_str)
                else:
                    now[1] = rear.pop()
                    del_count +=1
            else :
                now[0] = front.pop()
                del_count +=1
        else :
            front.append(now[0])
            now[0]=now[1]
            if len(rear) == 0 :
                now.pop()
                del_remain = k-del_count
                tmp_str = front + now
                for i in range(del_remain):
                    tmp_str.pop()
                return ''.join(tmp_str)
            else:
                now[1] = rear.pop()
        if del_count >= k:
            rear.reverse()
            return "".join(front)+"".join(now)+"".join(rear)


print(solution(number,k))

#15점!!! 뿌-듯
