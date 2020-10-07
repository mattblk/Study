numbers = [0,0]

def solution(numbers):

    # 두개의 수 합 array
    arr_sum=[]

    # 두개의 수 합을 구하는 함수 추가
    def add_sum(nums):
        # 배열 backward
        num_foward = nums[0]
        arr_backward=nums[1:len(nums)]

        for i in arr_backward :
            arr_sum.append(num_foward + i)

        if len(arr_backward) >= 2 :
            add_sum(arr_backward)

    add_sum(numbers)

    answer = list(set(arr_sum))
    answer.sort()
    return answer

print(solution(numbers))
