numbers=[8,3,5,7,3,4]


#dfs 방식이 아니라 이거 뭐냐 dp로 해결
def solution1(numb):
	visit= [[0]*pow(2,i+1) for i in range(len(numb))]
	visit[0][0], visit[0][1] = numb[0], -numb[0]
	for i in range(1,len(numb)):
		for j in range(len(visit[i])):
			if j%2 ==0:
				visit[i][j]=visit[i-1][j//2]+ numb[i]
			else:
				visit[i][j]=visit[i-1][j//2]-numb[i]
	
	return visit[len(numb)-1].count(0)
	
print(solution1(numbers))

def solution2(numb):
	visit= [[0]*pow(2,i+1) for i in range(len(numb))]
	visit[0][0], visit[0][1] = numb[0], -numb[0]
	for i in range(1,len(numb)):
		for j in range(len(visit[i])):
			if j%2 ==0:
				visit[i][j]=visit[i-1][j//2]+ numb[i]
			else:
				visit[i][j]=visit[i-1][j//2]-numb[i]
	
	return visit[len(numb)-1].count(0)

	
