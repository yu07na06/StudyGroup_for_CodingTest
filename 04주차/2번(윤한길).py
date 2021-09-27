from itertools import permutations
from bisect import bisect_right


def solution(n, weak, dist):
    answer = []
    new_weak = weak + [i + n for i in weak]
    pers = permutations(dist, len(dist))
    # print(new_weak)

    for per in pers:
        for i in range(len(weak)):
            start = i
            length = 0
            for j in range(len(dist)):
                idx = bisect_right(new_weak, new_weak[start]+per[j])
                length += idx - start
                start = idx
                if length >= len(weak):
                    answer.append(j+1)
                    break
                if j == len(dist)-1 and length < len(weak):
                    answer.append(9)
    # print(answer)
    return -1 if min(answer) == 9 else min(answer)



# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# result = 2
# print(solution(n, weak, dist))
#
# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# result = 1
# print(solution(n, weak, dist))

# 반례
# N = 200
# weak = [0, 10, 50, 80, 120, 160]
# dist = [1, 10, 5, 40, 30]
# result = 3
# print(solution(N, weak, dist))

# N = 50
# weak = [1, 10, 20, 40]
# dist = [1, 2, 1]
# result = -1
# print(solution(N, weak, dist))
