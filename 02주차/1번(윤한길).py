"""
places	                                                result
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	        [1, 0, 1, 1, 1]
"""

from collections import deque


def solution(places):
    def bfs(place, y, x):
        # 동, 서, 남, 북
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[False for _ in range(5)] for _ in range(5)]

        visited[y][x] = True
        dq = deque()
        dq.append([y, x, 0])

        while(dq):
            y, x, dist = dq.popleft()
            if dist > 2:
                return True
            if place[y][x] == 'P' and 0 < dist <= 2:
                return False

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                new_dist = dist + 1
                if 0 <= new_x < 5 and 0 <= new_y < 5:
                    if not visited[new_y][new_x] and place[new_y][new_x] != 'X':
                        dq.append([new_y, new_x, new_dist])
                        visited[new_y][new_x] = True

        return True

    answer = []
    for place in places:
        check = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        check = False
                        break
            if not check:
                break
        if not check:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution((places)))