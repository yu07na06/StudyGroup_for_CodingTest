"""
words
["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries
["fro??", "????o", "fr???", "fro???", "pro?"]

result
[3, 2, 4, 1, 0]
"""

# import re
# from bisect import bisect_left, bisect_right
#
#
# def solution(words, queries):
#     new_queries = []
#     for i in queries:
#         new_queries.append('(?<!\w)' + i.replace('?', '\w') + '(?!\w)')
#     # print(new_queries)
#
#     words.sort(key=lambda x: len(x))
#     answer = []
#     for i in range(len(queries)):
#         L = bisect_left(list(map(len, words)), len(queries[i]))
#         R = bisect_right(list(map(len, words)), len(queries[i]))
#         answer.append(len(re.findall(new_queries[i], ' '.join(words[L:R]))))
#
#     return answer


import re


def solution(words, queries):
    for i, v in enumerate(queries):
        queries[i] = '(?<!\w)' + v.replace('?', '\w') + '(?!\w)'
    return [len(re.findall(i, ' '.join(words))) for i in queries]


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
