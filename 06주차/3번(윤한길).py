# 정답은 맞지만 시간초과

# import sys
#
#
# input = sys.stdin.readline
# N, H = map(int, input().split())
# obstruction = [int(input()) for _ in range(N)]
# answer = []
# # print(obstruction)
#
# for i in range(1, H+1):
#     cnt = 0
#     for j in range(N):
#         if j % 2 == 1:
#             # 홀수 처리(석순)바닥
#             if obstruction[j] >= i:
#                 cnt += 1
#         else:
#             # 짝수 처리(종유석)천장
#             if obstruction[j] >= abs(i-(H+1)):
#                 cnt += 1
#     answer.append(cnt)
# min_val = min(answer)
#
# print(min_val, answer.count(min_val))


import sys
from bisect import bisect_left


input = sys.stdin.readline
N, H = map(int, input().split())
half_N = N//2
obstructions = [int(input()) for i in range(N)]
even_obstruction = []
odd_obstruction = []

for i in range(len(obstructions)):
    if i % 2 == 0:
        even_obstruction.append(obstructions[i])
    else:
        odd_obstruction.append(obstructions[i])

even_obstruction.sort()
odd_obstruction.sort()
# print(even_obstruction, odd_obstruction)

answer = []
for i in range(1, H+1):
    cnt = 0
    cnt += half_N - bisect_left(even_obstruction, i)
    cnt += half_N - bisect_left(odd_obstruction, abs(i-(H+1)))
    answer.append(cnt)

min_val = min(answer)
print(min_val, answer.count(min_val))
