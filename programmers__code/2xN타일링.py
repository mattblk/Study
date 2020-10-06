def solution(n):
	fibo=list()
	fibo.append(1)
	fibo.append(2)
	if n>=3:
		for i in range(2,n):
			fibo.append(fibo[i-1]+fibo[i-2])
	return fibo[n-1]%1000000007

print(solution(7))