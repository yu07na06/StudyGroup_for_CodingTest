"""
5 4
0 1
1 2
2 3
3 4         1

8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7         1

6 5
0 1
0 2
0 3
0 4
0 5         0

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# global
satisfied = False
def dfs(vertex, depth):
    # print('here:%d, depth:%d is called' % (vertex, depth))
    global satisfied
    visited[vertex] = True
    if depth >= 4:
        satisfied = True
        return
    for i in graph[vertex]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False
            # print('here:%d, depth:%d, i:%d is closed' % (vertex, depth, i))


for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if satisfied:
        break

if satisfied:
    print(1)
else:
    print(0)
