import re

TWO_STR = re.compile('[a-z]{2}')

def str_list(st):
    st = st.lower()
    lists = []
    for i in range(0, len(st)-1):
        if TWO_STR.match(st[i] + st[i+1]):
            lists.append(st[i] + st[i+1])
    return lists

def intersection(st1, st2):
    st_list = []
    for i in st1:
        if i in st2:
            st_list.append(i)
            st2.pop(st2.index(i))
    return st_list


def solution(str1, str2):
    answer = 0
    str1 = str_list(str1)
    str2 = str_list(str2)

    if len(str1) == 0 and len(str2) == 0:
        return 65536
    else:
        n = len(intersection(str1, str2))
        u = len(str1) + len(str2)
        return int(n / u * 65536)
