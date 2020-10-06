###11점이고 풀이 베낌 ㅈㅅ


board = [[0]*6 for i in range(6)]
board[0] = [1,1,1,1,1,1]
board[1] = [1,1,1,1,1,1]
board[2] = [1,1,0,1,1,1]
board[3] = [1,1,1,0,1,1]
board[4] = [1,1,1,1,1,1]
board[5] = [1,1,1,1,1,1]

# board =[[1]]
def solution(board):
    sumz =0
    maxz=[]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])) :
            if board[i][j] ==1 :
                board[i][j]=min(board[i-1][j-1], board[i][j-1], board[i-1][j]) +1

    for i in board:
        maxz.append(max(i))

    return pow(max(maxz),2)

print(solution(board))




board=[[0,0,0]]
import math
def solution(board):
    sumz=0
    for i in board:
        # print(i)
        sumz += sum(i)
    if sumz == 0 :
        return 0
    size = min(len(board),len(board[0]))

    def box_sum(size, i, j) :
        for m in board[i:i+size] :
            for n in m[j:j+size]:
                if n ==1 : pass
                else : return False
        return True
    while True :
        for i in range(0,len(board)-size+1):
            for j in range(0,len(board[0])-size+1):
                if board[i][j] == 1:
                    if box_sum(size,i,j) :
                        return size*size
        size-=1
        if size==1: return 1


print(solution(board))
