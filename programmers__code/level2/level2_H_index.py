def solution(c):
    for i,x in enumerate(sorted(c)):
        if x>= len(c)-i:
            return len(c)-i
    return 0


#9점 패스함 그냥 짜증나서
#1시간 20분소요
