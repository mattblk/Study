llist=[12345,2345,5456]

#### 나의풀이
def solution(phone_book) :
    phone_book.sort()
    i=0
    for item in phone_book :
        if i<len(phone_book) :
            for j in range(i+1,len(phone_book)) :
                if str(item) == str(phone_book[j][0:len(str(item))])
                    return False
        i=i+1
    return True
