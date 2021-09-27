from itertools import combinations
import sys


input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    x_list = [0] * N
    y_list = [0] * N
    r_list = [0] * N
    parent = [i for i in range(N)]
    combination_list = [i for i in range(N)]

    for i in range(N):
        x, y, r = map(int, input().split())
        x_list[i] = x
        y_list[i] = y
        r_list[i] = r

    for com in combinations(combination_list, 2):
        if ((x_list[com[0]] - x_list[com[1]])**2 + (y_list[com[0]] - y_list[com[1]])**2) <= ((r_list[com[0]] + r_list[com[1]])**2):
            if find_parent(parent, com[0]) != find_parent(parent, com[1]):
                union_parent(parent, com[0], com[1])
                # print(parent)
    # 모든 노드 find 해줘서 부모노드 변경하기
    for i in range(len(parent)):
        find_parent(parent, i)

    answer.append(len(set(parent)))

print(*answer, sep='\n')

"""
반례

1
4
0 0 1
0 4 1
0 1 1
0 3 1

answer : 1
"""