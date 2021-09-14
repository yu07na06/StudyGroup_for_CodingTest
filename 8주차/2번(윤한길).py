"""
scores	                                                                                    result
[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	"FBABD"
[[50,90],[50,87]]	                                                                        "DA"
[[70,49,90],[68,50,38],[73,31,100]]	                                                        "CFD"
"""
from collections import defaultdict


def solution(scores):
    answer = ''
    d = defaultdict(list)
    length = len(scores)

    for score in scores:
        for i, v in enumerate(score):
            d[i].append(v)

    for i in range(length):
        min_num, max_num = min(d[i]), max(d[i])
        min_cnt, max_cnt = d[i].count(min_num), d[i].count(max_num)

        if (d[i][i] == min_num and min_cnt == 1) or (d[i][i] == max_num and max_cnt == 1):
            del d[i][i]

        avg = sum(d[i]) / len(d[i])  # 평균값
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


if __name__ == '__main__':
    # scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
    # result = "FBABD"
    # print(solution(scores))
    scores = [[90, 90, 90, 90], [70, 70, 70, 70], [90, 90, 90, 90], [70, 70, 70, 70]]
    result = "BBBB"
    print(solution(scores))
