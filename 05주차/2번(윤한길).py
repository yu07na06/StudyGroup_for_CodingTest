"""
input = 2 25 25 25 25
output = 0.75
"""

import sys


input = sys.stdin.readline
n, E, W, S, N = map(int, input().split())
probability = [E/100, W/100, S/100, N/100]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(2*n + 1)] for _ in range(2*n + 1)]
visited[n][n] = True


def dfs(y, x, cnt, p):
    global answer

    if cnt == n:
        answer += p
        return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if not visited[new_y][new_x]:
            visited[new_y][new_x] = True
            dfs(new_y, new_x, cnt+1, p * probability[i])
            visited[new_y][new_x] = False


answer = 0
dfs(n, n, 0, 1)
print(answer)
