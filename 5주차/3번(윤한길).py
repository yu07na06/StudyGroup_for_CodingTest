"""
7 3
5 6 4 3 6 2 3
3 2 5
"""

import sys

input = sys.stdin.readline
inf = sys.maxsize

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, D):
    oven[i] = min(oven[i], oven[i - 1])

# print(oven)

idx = 0
for i in range(D-1, -1, -1):
    if oven[i] >= pizza[idx]:
        if idx == len(pizza)-1:
            answer = i+1
            break
        idx += 1


print(answer)
