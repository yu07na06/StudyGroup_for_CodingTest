"""
s	                            result
"aabbaccc"	                    7
"ababcdcdababcdcd"	            9
"abcabcdede"	                8
"abcabcabcabcdededededede"	    14
"xababcdcdababcdcd"	            17
"""

import re


def solution(s):
    answer = []
    LENGTH = len(s)
    MAX_LENGTH = LENGTH // 2 + 1

    if LENGTH < 2:
        return LENGTH

    for i in range(1, MAX_LENGTH):
        # if LENGTH % i == 0:
        tmp = re.findall('.{%d}|.+' % i, s)
        # print(tmp)

        cnt = 1
        zipped = []
        for j in range(len(tmp)):
            # j < len(tmp)-1를 앞에 둬야 제일 마지막 element를 순회할때
            # tmp[j] == tmp[j + 1]조건을 읽지 않고 j < len(tmp)-1 부분만 읽고 else로 넘어가서 list index out of range가 안뜸
            if j < len(tmp)-1 and tmp[j] == tmp[j + 1]:
                cnt += 1
            else:
                if cnt == 1:
                    zipped.append(tmp[j])
                else:
                    zipped.append(str(cnt) + tmp[j])
                    cnt = 1
        # print(zipped)
        answer.append(len(''.join(zipped)))

    return min(answer)


s = "abcabcabcabcdededededede"
print(solution(s))
