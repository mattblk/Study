arr=[1,1,3,3,0,1,1]
def solution(arr):
    _list=[]
    for i in range(len(arr)) :
        if i==0:
            _list.append(arr[i])
        else:
            if _list[-1] != arr[i] :
                _list.append(arr[i])
    return _list
print(solution(arr))


# 첫 번째 타입 ===pop 때문에 효율성 망함
# def solution(arr):
#     i=0
#     while True:
#         if i<len(arr)-1:
#             if arr[i]==arr[i+1]:
#                 arr.pop(i+1)
#             else :
#                 i = i +1
#         else :
#             break
#     answer = arr
#
#
#     return answer
