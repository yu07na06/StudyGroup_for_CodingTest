"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""
import sys
from pprint import pprint
from copy import deepcopy


def find_idx(fish_num):     # 입력된 번호의 물고기 위치 i, j(행, 열)로 반환해주는 함수
    for i in range(4):
        try:
            j = list(map(lambda x: x[0], graph[i])).index(fish_num)
            break
        except ValueError:
            if i == 3:
                return False
            else:
                pass
    return i, j


def fish_move():

    for i in range(1, 17):
        # pprint(graph)
        if find_idx(i):
            y, x = find_idx(i)
        elif not find_idx(i):
            continue
        direction = graph[y][x][1] - 1
        new_y, new_x = y + dy[direction], x + dx[direction]

        # 이동가능한지 체크(범위안에 있고, 물고기가 있거나 비어있는경우)
        if (0 <= new_y < 4 and 0 <= new_x < 4) and (graph[new_y][new_x][0] or not graph[new_y][new_x][1]):
            graph[y][x], graph[new_y][new_x] = graph[new_y][new_x], graph[y][x]
        else:
            for _ in range(7):
                direction = (direction + 1) % 8
                new_y, new_x = y + dy[direction], x + dx[direction]

                if (0 <= new_y < 4 and 0 <= new_x < 4) and (graph[new_y][new_x][0] or not graph[new_y][new_x][1]):
                    graph[y][x][1] = direction + 1
                    graph[y][x], graph[new_y][new_x] = graph[new_y][new_x], graph[y][x]
                    break

    return


def shark_move(count):
    global graph
    global cnt
    # print('상어 움직인 후:')
    # pprint(graph)
    fish_move()
    # print('물고기 움직인 후:')
    # pprint(graph)
    cnt = max(count, cnt)
    # print(cnt)
    for i in range(1, 4):
        y, x = find_idx(False)
        direction = graph[y][x][1] - 1
        new_y = y + (dy[direction]) * i
        new_x = x + (dx[direction]) * i

        # if (0 <= new_y < 4 and 0 <= new_x < 4) and graph[new_y][new_x][0] < 17:
        if (0 <= new_y < 4 and 0 <= new_x < 4) and graph[new_y][new_x][0]:
            tmp_cnt = graph[new_y][new_x][0]

            tmp_g = deepcopy(graph)
            # graph[y][x][0], graph[y][x][1], graph[new_y][new_x][0] = 17, False, False
            graph[y][x][0], graph[y][x][1], graph[new_y][new_x][0] = None, False, False
            shark_move(count+tmp_cnt)
            graph = tmp_g
            # print('백트레킹 후:')
            # pprint(graph)
    return


if __name__ == '__main__':
    input = sys.stdin.readline
    # [↑, ↖, ←, ↙, ↓, ↘, →, ↗]
    # [1, 2, 3, 4, 5, 6, 7, 8]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    graph = [[] for _ in range(4)]

    for i in range(4):      # [물고기 번호, 방향] 입력받아서 리스트로 저장하기
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            if j % 2 == 0:
                graph[i].append([tmp[j]])
            else:
                graph[i][j//2].append(tmp[j])

    # pprint(graph)
    # (0,0) 위치에 상어 들어가기
    cnt = 0     # 상어가 먹은 물고기 번호 총합
    cnt += graph[0][0][0]
    graph[0][0][0] = False

    shark_move(cnt)
    print(cnt)
