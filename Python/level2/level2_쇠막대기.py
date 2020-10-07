_str="()(((()())(())()))(())"
def solution (arrangement):
     answer = 0
     num_stick = 0
     last = "open"

     for token in arrangement:
         if token == "(":
             num_stick += 1
             last = "open"
         else:
             if last == "open":
                 # laser
                 num_stick -= 1
                 answer += num_stick
                 last = "close"
             else:
                 # end of stick
                 num_stick -= 1
                 answer += 1

     return answer
print(solution(_str))
