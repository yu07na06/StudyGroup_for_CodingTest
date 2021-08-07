"""
words
["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries
["fro??", "????o", "fr???", "fro???", "pro?"]

result
[3, 2, 4, 1, 0]
"""

import re


def solution(words, queries):
    answer = []
    queries = [i.replace('?', '\w') for i in queries]
    for i, v in enumerate(queries):
        queries[i] = '(?<!\w)' + v + '(?!\w)'
    # print(queries)
    for i in queries:
        answer.append(len(re.findall(i, ' '.join(words))))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
solution(words, queries)
