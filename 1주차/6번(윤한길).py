"""
mirkovC4nizCC44
C4                  mirkovniz

12ab112ab2ab
12ab                FRULA
"""

# import re
# import sys
#
# input = sys.stdin.readline
#
# s = input().strip()
# bomb = input().strip()
#
# while True:
#     if not re.findall(bomb, s):
#         break
#     s = re.sub(bomb, '', s)
#
# if not s:
#     print('FRULA')
# else:
#     print(s)


import sys

input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
length = len(bomb)
stack = []

for i in s:
    stack.append(i)
    if i == bomb[-1]:
        if ''.join(stack[-length:]) == bomb:
            del stack[-length:]

if not stack:
    print('FRULA')
else:
    print(*stack, sep='')
