import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
# 기본 입력값 받기
N, M = map(int, input().split())    # N = 세로, M = 가로
graph = [list(map(int, input().split())) for _ in range(N)]
# empty space 위치 저장
empty = [[y, x] for y in range(N) for x in range(M) if graph[y][x] == 0]
# print(empty)


def bfs(new_graph, i, j):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    dq = deque([[i, j]])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while dq:
        y, x = dq.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            # graph 범위내에있고 상하좌우가 빈공간(0)이고 방문안한 곳이라면...
            if (0 <= new_y <= N-1 and 0 <= new_x <= M-1) and new_graph[new_y][new_x] == 0 and not visited[new_y][new_x]:
                new_graph[new_y][new_x] = 2
                visited[new_y][new_x] = True
                dq.append([new_y, new_x])


# 안전영역 카운트 함수
def count_empty_space(new_graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 0:
                cnt += 1
    return cnt


answer = []
for com in combinations(empty, 3):
    new_graph = deepcopy(graph)
    for v in com:
        new_graph[v[0]][v[1]] = 1
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] == 2:
                bfs(new_graph, i, j)
    answer.append(count_empty_space(new_graph))

print(max(answer))

# for i in g:
#     print(*i)
