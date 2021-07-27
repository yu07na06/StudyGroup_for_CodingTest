"""
3
4
7
10              4
                8
                14
"""

import sys


input = sys.stdin.readline
T = int(input())
N = [int(input()) for _ in range(T)]

dp = [False for _ in range(10001)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
answer = []
for i in N:
    for j in range(4, i+1):
        if not dp[j]:
            dp[j] = (dp[j-1] + dp[j-2]) - dp[j-3]
            if j % 3 == 0:
                dp[j] += 1
    answer.append(dp[i])
print(*answer, sep='\n')
