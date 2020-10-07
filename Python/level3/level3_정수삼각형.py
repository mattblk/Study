#3점짜리 한 10분 걸렸나 에러없이 한번에 깔-끔

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(len(triangle)) :
    print(triangle[i])


def solution(triangle) :
    max_sum = [[-1]*(i+1) for i in range(len(triangle))]
    max_sum[0][0]=triangle[0][0]

    for i in range(1, len(triangle)) :
        for j in range(0, len(triangle[i])):
            if j==0:
                max_sum[i][j]=max_sum[i-1][0]+triangle[i][j]
            elif j==len(triangle[i])-1:
                max_sum[i][j]=max_sum[i-1][-1]+triangle[i][j]
            else :
                max_sum[i][j] = max(max_sum[i-1][j-1],max_sum[i-1][j])+triangle[i][j]

    # for i in range(len(max_sum)):
    #     print(max_sum[i])


    return max(max_sum[-1])




print(solution(triangle))
