
def solution(n):

    nums = [i for i in range(1,n+1)]

    nums.insert(0,1)

    for i in range(2,n+1):

        j=2

        while i*j<=n:

            nums[i*j]=1

            j+=1

    return len(nums)-nums.count(1)


# 이건 시간초과
#
# def solution(n):
#     num=set(range(2,n+1))
#     for i in range(2,n+1):
#         if i in num :
#             num=num-set(range(2*i,n+1,i))
#     return len(num)
# print(solution(10))
#



#13점
