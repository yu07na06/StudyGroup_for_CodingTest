# (정확성 O, 효율성 X)

# import re
#
#
# def conv_to_set_int(list_of_list):
#     list_of_list = [[set(i[:-1]) - set('-'), int(i[-1])] for i in list_of_list]
#
#     return list_of_list
#
#
# def check(info, query):
#     answer = []
#     for i in query:
#         cnt = 0
#         for j in info:
#             if i[0].issubset(j[0]) and i[1] <= j[1]:
#                 cnt += 1
#         answer.append(cnt)
#     return answer
#
#
# def solution(info, query):
#     info = [i.split() for i in info]
#     # print(info)
#
#     query = [re.split(' and | ', i) for i in query]
#     # print(query)
#
#     info, query = conv_to_set_int(info), conv_to_set_int(query)
#     print(info)
#     print(query)
#
#     return check(info, query)

# (정확성 O, 효율성 O)
import re
from itertools import combinations
from bisect import bisect_left, bisect_right


def solution(info, query):
    answer = []
    dict = {}
    # info, query 리스트에 각각 키워드 문자열로 저장
    info = [i.split() for i in info]
    query = [re.split(' and | ', i) for i in query]

    # info 딕셔너리에 저장
    for i in info:
        score = int(i.pop())
        for j in range(5):
            for combination in combinations([0, 1, 2, 3], j):
                tmp = ''
                for k in range(4):
                    if k in combination:
                        tmp += '-'
                    else:
                        tmp += i[k]
                if tmp not in dict:
                    dict[tmp] = []
                dict[tmp] += [score]
    # print(dict)

    # 딕셔너리에 저장된 score 값 오르차순 정렬
    for i in dict.values():
        i.sort()
    # print(dict)

    # 쿼리 순회하며 갯수 세기(이진탐색 이용)
    for i in query:
        score = int(i.pop())
        tmp = ''.join(i)
        if tmp in dict:
            left = bisect_left(dict[tmp], score)
            right = len(dict[tmp])
            answer.append(right-left)
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
#result = [1,1,1,1,2,4]
