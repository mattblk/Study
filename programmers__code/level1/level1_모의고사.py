def solution(answers):
    def _1st(n):
        if n%5 == 0:
            return 5
        else:
            return n%5
    def _2nd(n):
        if n%2==1:
            return 2
        else :
            if (n/2) %4 == 1: return 1
            elif (n/2) %4 == 2: return 3
            elif (n/2) %4 == 3: return 4
            else : return 5
    def _3rd(n) :
        if n%2==1 :
            tn=int((n+1)/2)
        else :
            tn = int(n/2)
        if tn%5 == 1: return 3
        elif tn%5 ==2 : return 1
        elif tn%5 ==3 : return 2
        elif tn%5 ==4 : return 4
        else : return 5
    score=[0]*3

    for i in range(len(answers)):
        if _1st(i+1) == answers[i] : score[0] = score[0] +1
        if _2nd(i+1) == answers[i] : score[1] = score[1] +1
        if _3rd(i+1) == answers[i] : score[2] = score[2] +1
    def find_max_index(num) :
        max_num=max(num)
        max_index=[]
        for i in range(len(num)):
            if num[i]==max_num:
                max_index.append(i+1)
        return max_index
    return find_max_index(score)
