"""
Input                       Output
4 2
1 1 1 1                     3

10 5
1 2 3 4 2 5 3 1 1 2         3
"""
# from collections import deque
#
#
# n, m = map(int, input().split())
# A = list(map(int, input().split()))
#
# dq = deque()
# total = sum(dq)
# cnt = 0
# end = 0
#
# for _ in A:
#     while sum(dq) < m and end < n:
#         dq.append(A[end])
#         end += 1
#     if sum(dq) == m:
#         cnt += 1
#     dq.popleft()
#
# print(cnt)

n, m = map(int, input().split())
A = list(map(int, input().split()))

total = 0
cnt = 0
end = 0

for start in range(len(A)):
    while total < m and end < n:
        total += A[end]
        end += 1
    if total == m:
        cnt += 1
    total -= A[start]

print(cnt)
