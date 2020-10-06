# a=[1,3,4,56,4,2,23,12,89,9,888,999,331,1000]
a=[3, 30, 34, 5, 9]

def solution(arr):
    def str_arr(arr):
        str_arr=""
        for i in range(0, len(arr)):
            str_arr= str_arr + str(arr[i])
        return str_arr

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot=arr[len(arr)//2]
        lesser_arr, equal_arr, greater_arr = [],[],[]
        for num in arr:
            if int(str(num)+str(pivot)) > int(str(pivot)+str(num)) :
                lesser_arr.append(num)
            elif int(str(num)+str(pivot)) < int(str(pivot)+str(num)) :
                greater_arr.append(num)
            else :
                equal_arr.append(num)
        return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

    if str_arr(quick_sort(arr))[0] == 0 :
        return "0"
    else:
        return str_arr(quick_sort(arr))

print(solution(a))
