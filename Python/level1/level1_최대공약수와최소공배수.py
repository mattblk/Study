def solution(n,m) :
    def gcm(n,m):
        gcm=1
        for i in range(2,min(n,m)+1):
            while n%i == 0 and m%i == 0:
                n=n/i
                m=m/i
                gcm*=i
        return gcm
    answer=[]
    gcm_ = gcm(n,m)
    answer.append(gcm_)
    answer.append(n*m/gcm_)
    return answer

#score 5
