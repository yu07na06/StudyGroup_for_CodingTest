
# https://mungto.tistory.com/158


def dfs(idx, ans):
    global answer
    visited[idx] = 0
    ans += 1
    if answer < ans:
        answer = ans
    if answer < 5:
        for i in graph[idx]:
            if visited[i]:
                dfs(i, ans)
    visited[idx] = 1


N, M = map(int, input().split())
visited = [1 for _ in range(N+1)]
temp = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
answer = 0
for a, b, in temp:
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    dfs(i, 0)

if answer >= 5:
    print(1)
else:
    print(0)
