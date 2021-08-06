"""
input:
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
output:
4
3
"""

# import sys
#
#
# input = sys.stdin.readline
# T = int(input())
# answer = []
# for _ in range(T):
#     N = int(input())
#     T_list = [tuple(map(int, input().split())) for _ in range(N)]
#     cnt = N
#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 continue
#             if T_list[i][0] > T_list[j][0]:
#                 if T_list[i][1] > T_list[j][1]:
#                     cnt -= 1
#                     break
#     answer.append(cnt)
#
# print(*answer, sep='\n')


import sys


input = sys.stdin.readline
T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    T_list = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    MIN = T_list[0][1]
    cnt = N
    for i in range(1, N):
        if T_list[i][1] > MIN:
            cnt -= 1
        else:
            MIN = T_list[i][1]
    answer.append(cnt)

print(*answer, sep='\n')
