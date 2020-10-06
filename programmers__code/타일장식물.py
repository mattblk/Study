def solution(n):
	fibo=[0]*n
	fibo[0]=1
	if n>=2:
		fibo[1]=1
	if n>=3:
		for i in range(2,n):
			fibo[i]=fibo[i-1]+fibo[i-2]
	if n==1:
		return 4
	else:
		print(fibo)
		return fibo[n-1]*4+fibo[n-2]*2

print(solution(5))