stock = 10
dates = [4,10,15]
supplies = [20,5,10]
k = 11
#result 2


#다른사람풀이
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    idx=0
    h=[]
    while(stock<k):
        for i in range(idx,len(dates)):
            if dates[i]<=stock:
                heapq.heappush(h,(-supplies[i],supplies[i]))
                idx=i+1
            else:
                break
        stock+=heapq.heappop(h)[1]
        answer+=1
    return answer






#2단시간초과
import heapq
def solution2(stock, dates, supplies, k):
    day = 0
    answer = 0
    date_index=0
    heap=[]
    while True :
        day+=1
        stock-=1
        try:
            if dates[date_index] == day :
                heapq.heappush(heap,(-supplies[date_index],dates[date_index]))
                date_index +=1
        except IndexError: pass
        if stock == 0 :
            stock -= heapq.heappop(heap)[0]
            answer+=1
        if k-day == 1 :
            return answer


#3단시간초과
import heapq
def solution(stock, dates, supplies, k):
    day = 0
    answer = 0
    date_index=0
    heap=[]
    while True :
        day+=stock
        stock = 0

        if k-day <= 0 :
            return answer

        _fdidx = date_index
        for i,date in enumerate(dates[_fdidx:]):
            if date<= day :
                heapq.heappush(heap,(-supplies[_fdidx:][i],date))
                date_index +=1

        stock -= heapq.heappop(heap)[0]
        answer+=1
#

print(solution(stock, dates, supplies, k))
