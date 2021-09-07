from collections import deque


def find_all_p(l):
    p_list = []
    for i, v1 in enumerate(l):
        for j, v2 in enumerate(v1):
            if v2 == 'P':
                p_list.append((i, j, 0))

    return p_list


def bfs(l, graph):
    dq = deque([l])
    visited = [[False] * 5 for _ in range(5)]

    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]  # 상하좌우

    while dq:
        y, x, dist = dq.popleft()
        visited[y][x] = True

        if 1 <= dist <= 2 and graph[y][x] == 'P':
            return 0

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if 0 <= new_x <= 4 and 0 <= new_y <= 4 and not visited[new_y][new_x]:
                if graph[new_y][new_x] != 'X' and dist < 2:
                    dq.append((new_y, new_x, dist+1))

    return 1


def solution(places):
    answer = []
    for i in places:
        if not find_all_p(i):
            answer.append(1)
        else:
            for j in find_all_p(i):
                tmp = bfs(j, i)
                if tmp == 0:
                    break
            answer.append(tmp)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# places = [["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]]
print(solution(places))
result = [1, 0, 1, 1, 1]