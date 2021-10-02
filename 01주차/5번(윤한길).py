"""
orders	                                                course      	result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]    	    [2,3,4]	        ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	    [2,3,5]	        ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                                [2,3,4]	        ["WX", "XY"]
"""

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # max_str = max(orders, key=len)
    for i in course:
        # if i > len(max_str):
        #     continue
        tmp = []
        for j in orders:
            #j sort하는 이유 : case 3 -> wx xw 카운트를 못하기떄문에 미리 sort하고 카운트할수 있게하기
            tmp += combinations(sorted(j), i)
        # case3: 문자열 최대길이는 3인데 course에 4가 돌아가면 tmp가 empty가 됨
        if tmp:
            max_counted = max(Counter(tmp).values())
        if max_counted > 1:
            for k, v in Counter(tmp).items():
                if v == max_counted:
                    answer.append(''.join(k))
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
