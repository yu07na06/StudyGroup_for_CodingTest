import sys

input = sys.stdin.readline


def most_cnt(num):
    cnt_like = -1
    cnt_empty = -1

    for i in range(N):
        for j in range(N):
            if sits[i][j] == 0:
                tmp_like = 0
                tmp_empty = 0

                for k in range(4):
                    if 0 <= i + dy[k] < N and 0 <= j + dx[k] < N:
                        if sits[i + dy[k]][j + dx[k]] in D[num]:
                            tmp_like += 1
                        if sits[i + dy[k]][j + dx[k]] == 0:
                            tmp_empty += 1

                if cnt_like == tmp_like:
                    if cnt_empty < tmp_empty:
                        cnt_empty = tmp_empty
                        location = [i, j]

                if cnt_like < tmp_like:
                    cnt_like = tmp_like
                    cnt_empty = tmp_empty
                    location = [i, j]

    return location


def find_cnt(x, y):
    cnt = 0
    for k in range(4):
        if 0 <= y + dy[k] < N and 0 <= x + dx[k] < N:
            if sits[y + dy[k]][x + dx[k]] in D[sits[y][x]]:
                cnt += 1

    if cnt == 0:
        return 0
    else:
        return 10 ** (cnt - 1)


dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
dy = [-1, 1, 0, 0]  # 상, 하, 좌, 우
N = int(input())
D = {i: [] for i in range(N * N + 1)}
sits = [[0 for _ in range(N)] for _ in range(N)]
num_orders = []

for i in range(N * N):
    num, a, b, c, d = map(int, input().split())
    num_orders.append(num)
    D[num].append(a)
    D[num].append(b)
    D[num].append(c)
    D[num].append(d)


for i in range(N*N):
    tmp = most_cnt(num_orders[i])
    # if tmp:
    y, x = tmp[0], tmp[1]
    sits[y][x] = num_orders[i]

answer = 0
for i in range(N):
    for j in range(N):
        answer += find_cnt(i, j)

# print(D)
# print(sits)
print(answer)


"""
반례:

3
1 1 1 1 1
2 1 1 1 1
3 1 1 1 1
4 1 1 1 1
5 1 1 1 1
6 1 1 1 1
7 2 3 2 3
8 2 3 2 3
9 2 3 2 3

답: 6
"""