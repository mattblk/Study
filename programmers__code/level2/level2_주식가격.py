prices =[1, 2, 3, 2, 3]
# ret = [4, 3, 1, 1, 0]

def solution(prices):
    prices.reverse()
    ret =[]
    while True:
        tmp = prices.pop()
        if len(prices) != 0 :
            for i in range(len(prices)-1, -1, -1) :
                if prices[i]< tmp :
                    ret.append(len(prices)-i)
                    break
                if i == 0 :
                    ret.append(len(prices))
                    break
        else :
            ret.append(0)
            return ret

print(solution(prices))


#5점 15분 소요
