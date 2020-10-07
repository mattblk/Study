numbers = [8,3,5,7,3,4]

def solution(numbers) :
    tree = [[0]*pow(2,i+1) for i in range(len(numbers))]
    return tree

print(solution(numbers))
