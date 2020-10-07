scoville =[1, 1,7]
K=7

# 8점 베낀 풀이 heap 구조 이해했으!!
import heapq
def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt

print(solution(scoville,K))

#
# 정확성 통과 했으나 효율성 부족 ---- 15분소요
# def solution(scoville, K):
#     time = 0
#     while True :
#
#         if min(scoville) < K :
#             min1 = min(scoville)
#             scoville.remove(min1)
#             min2 = min(scoville)
#             scoville.remove(min2)
#             scoville.append(min1+min2*2)
#             time += 1
#         else : return time
#
#         if len(scoville) <= 1 and min(scoville)<K : return -1
