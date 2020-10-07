def solution(phone_number):
    answer = '*'*(len(phone_number)-4)
    answer+=str(phone_number)[-4:]
    return answer
#score 1
