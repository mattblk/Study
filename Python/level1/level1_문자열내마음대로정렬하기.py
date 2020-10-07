strings=["abce", "abcd", "cdx"]
n=2
def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda k :k[n])
    return answer
print(solution(strings,n))

#8점
