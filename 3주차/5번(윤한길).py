# (일부만 통과)
from collections import deque
from math import floor


def solution(enroll, referral, seller, amount):
    answer = []
    # d = dict.fromkeys(enroll, []) # 리스트 전체가 하나로 연결되서 수정하면 다 바뀜
    # d = dict(zip(enroll, referral))
    d = {i: [] for i in enroll}
    # print(d)

    # 딕셔너리 방향추가
    for i in range(len(enroll)):
        d[enroll[i]].append(referral[i])
        d[enroll[i]].append(0)
        d[enroll[i]].append(0)
    # print(d)

    # 중복 셀러 하나로 합치기
    # 판매수익 입력
    for i in range(len(seller)):
        d[seller[i]][1] += amount[i] * 100
    # print(d)

    visited = []
    for i in seller:
        if i in visited:
            continue
        visited.append(i)

        initial = 0
        dq = deque([i])

        while dq:
            key = dq.popleft()

            if d[key][0] != '-':
                dq.append(d[key][0])

            if initial == 0:
                initial += 1
                if d[key][1] * .1 < 1:
                    d[key][2] += d[key][1]
                    toss = 0
                else:
                    d[key][2] += d[key][1] - floor(d[key][1] * .1)
                    toss = floor(d[key][1] * .1)
            else:
                if toss * .1 < 1:
                    d[key][2] += toss
                    toss = 0
                else:
                    d[key][2] += toss - floor(toss * .1)
                    toss = floor(toss * .1)


    for i in enroll:
        answer.append(d[i][2])

    return answer




enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(enroll, referral, seller, amount))







"""
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]
"""