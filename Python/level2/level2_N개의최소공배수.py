numbers = [2,6,8,14]

def solution(numbers):

    def prime(num):
        list_prime = list()
        for i in range(2,num+1):
            while num%i == 0 :
                num = int(num/i)
                list_prime.append(int(i))
        return list_prime

    def lcm(num1,num2):
        for i in num1 :
            try : num2.remove(i)
            except: pass
        return num1+num2


    prime_list=list()
    for i in range(len(numbers)):
        prime_list = lcm(prime_list,prime(numbers[i]))

    answer=1
    for i in prime_list:
        answer *= i
    return answer

print(solution(numbers))
