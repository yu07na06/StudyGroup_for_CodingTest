import re
from itertools import permutations
from copy import copy

def solution(expression):
    answer = []
    expression = re.split('([-+*])', expression)
    pers = permutations(['+', '-', '*'], 3)
    # print(*pers)
    for per in pers:
        exps = copy(expression)
        for p in per:
            # for i, exp in enumerate(exps): ---> for loop 으로하면 '1' '-' '2' '-' '5'와 같이 연달아 같은 연산이 있을시 인덱스 참고 제대로 못함
            while p in exps:
                idx = exps.index(p)
                exps[idx-1] = str(eval(''.join(exps[idx-1:idx+2])))
                del exps[idx:idx+2]
                # print(exps)
        answer.append(abs(int(*exps)))


    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))
"""
expression	            result
"100-200*300-500+20"	60420
"50*6-3*2"	            300
"""