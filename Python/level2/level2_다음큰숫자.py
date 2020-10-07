n=78 #83

def solution(n):
    str_n = bin(n)[2:]
    print(str_n)

    rrz=0
    for i in range(-1,-len(str_n)-1,-1):
        if str_n[i] == '0' : rrz+=1
        else: break

    n_str_n = list(str_n[:len(str_n)-rrz])
    if len(n_str_n) == 1 : return int(str_n+'0',2)

    for i in range(-1,-len(n_str_n)-1,-1):
        if n_str_n[i] == '0':
            n_str_n[i] ='1'
            n_str_n[i+1]='0'
            n_str_n.insert(i+1,'0'*rrz)
            break
        if i==-len(n_str_n) :
            n_str_n=['1']+n_str_n
            n_str_n[1] = '0'
            n_str_n.insert(1,'0'*rrz)
            break

    return int("".join(n_str_n),2)


print(solution(n))

#1점 1시간 40분 까쳐먹음??
