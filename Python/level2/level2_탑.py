def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)) :
        if i ==0: answer[i] =0
        else :
            for j in range(i-1,-1,-1):
                if heights[j]>heights[i] :
                    answer[i]=j+1
                    break
                if j==0 :
                    answer[i]=0
                    break
    return answer

#2점 13분소요
