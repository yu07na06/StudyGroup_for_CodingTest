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


# import re
#
#
# def solution(words, queries):
#     for i, v in enumerate(queries):
#         queries[i] = '(?<!\w)' + v.replace('?', '\w') + '(?!\w)'
#     return [len(re.findall(i, ' '.join(words))) for i in queries]


from bisect import bisect_left, bisect_right


def solution(words, queries):
    ascending = [[] for _ in range(10001)]
    descending = [[] for _ in range(10001)]

    for word in words:
        # 단어 있는 그대로
        ascending[len(word)].append(word)
        # 단어 reverse
        descending[len(word)].append(word[::-1])
    for i in range(10001):
        ascending[i].sort()
        descending[i].sort()

    answer = []
    for query in queries:
        #  prefix cases : ???~~~
        if query[0] == '?':
            L = bisect_left(descending[len(query)], query[::-1].replace('?', 'a'))
            R = bisect_right(descending[len(query)], query[::-1].replace('?', 'z'))
            answer.append(R - L)
        # suffix cases : ~~~???
        else:
            L = bisect_left(ascending[len(query)], query.replace('?', 'a'))
            R = bisect_right(ascending[len(query)], query.replace('?', 'z'))
            answer.append(R - L)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
