from math import floor


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    d = {v: i for i, v in enumerate(enroll)}

    for i in range(len(seller)):
        name = seller[i]
        income = amount[i] * 100

        while name != '-':
            answer[d[name]] += income - floor(income * .1)
            name = referral[d[name]]
            income = floor(income * .1)

            # income이 0이 되면 더이상 진행안하므로써 시간 단축
            # 이부분 없이 제출하면 시간초과남(질문하기 사람들 답변에서 힌트얻음)
            if income == 0:
                break

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(enroll, referral, seller, amount))

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
result = [0, 110, 378, 180, 270, 450, 0, 0]
print(solution(enroll, referral, seller, amount))