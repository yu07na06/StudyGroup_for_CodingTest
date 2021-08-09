# import sys
#
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# visited = [False] * (N + 1)
# graph = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     if a not in graph[b]:
#         graph[b].append(a)
#
#
# def DFS(v, cnt):
#     global depth
#     depth = max(depth, cnt)
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             DFS(i, cnt+1)
#             visited[i] = False
#     return depth
#
#
# depth_list = []
# answer = []
# for i in range(0, N+1):
#     depth = 0
#     depth_list.append(DFS(i, 0))
#     visited[i] = False
#
# max_num = max(depth_list)
# if max_num >= 2:
#     for i, v in enumerate(depth_list):
#         if v == max_num:
#             answer.append(i)
#     print(*answer)




import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph[b]:
        graph[b].append(a)
# print(graph)

dq = deque()
def BFS(start):
    visited = [False] * (N + 1)
    visited[start] = True
    dq.append(start)
    cnt = 1

    while dq:
        v = dq.popleft()
        if graph[v]:
            for i in graph[v]:
                if not visited[i]:
                    dq.append(i)
                    visited[i] = True
                    cnt += 1

    return cnt


cnt_list = [BFS(i) for i in range(N + 1)]
# print(cnt_list)
MAX_cnt = max(cnt_list)

answer = []
for i, v in enumerate(cnt_list):
    if MAX_cnt == v:
        answer.append(i)

print(*answer)


"""
5 4
3 1
3 2
4 3
5 3

answer: 1 2
"""