s="a B z"
n=4
def solution(s, n):
    string=''
    for i in s:
        if i == ' ': string += ' '
        elif i.isupper() :
            string+=chr(((ord(i)-65+n)%26)+65)
        else :
            string+=chr(((ord(i)-97+n)%26)+97)
    return string
print(solution(s,n))

#score 9
