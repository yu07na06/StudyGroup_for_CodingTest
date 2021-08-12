# (정확성 O, 효율성 X)

import re


def conv_to_set_int(list_of_list):
    list_of_list = [[set(i[:-1]) - set('-'), int(i[-1])] for i in list_of_list]

    return list_of_list


def check(info, query):
    answer = []
    for i in query:
        cnt = 0
        for j in info:
            if i[0].issubset(j[0]) and i[1] <= j[1]:
                cnt += 1
        answer.append(cnt)
    return answer


def solution(info, query):
    answer = []
    info = [i.split() for i in info]

    #query = [re.split('(.*?) and (.*?) and (.*?) and (.*?) ([\d]*)', i) for i in query]
    query = [re.split(' and | ', i) for i in query]
    # print(query)
    # conv = lambda i : None if i == '-' else i
    # query = [list(map(conv, i)) for i in query]


    info, query = conv_to_set_int(info), conv_to_set_int(query)
    # print(info)
    # print(query)

    return check(info, query)


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
#result = [1,1,1,1,2,4]
