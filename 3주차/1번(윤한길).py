"""
진열대 번호	1	2    3	  4	  5	  6       7	       8
보석 이름	    DIA	RUBY RUBY DIA DIA EMERALD SAPPHIRE DIA

gems	                                                                result
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	    [3, 7]
["AA", "AB", "AC", "AA", "AC"]	                                        [1, 3]
["XYZ", "XYZ", "XYZ"]	                                                [1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	                                [1, 5]
"""

# 첫시도(정확성X, 효율성X)
# def solution(gems):
#     num_category = len(set(gems))
#     R = len(gems)
#     L = 0
#     for left in range(len(gems)):
#         while num_category == len(set(gems[left:R])):
#             R -= 1
#         if num_category != len(set(gems[left:R+1])):
#             L = left
#             break
#     R += 1
#     answer = [L, R]
#     return answer


# 첫시도(정확성O, 효율성X)
# def solution(gems):
#     answer = []
#     num_category = len(set(gems))
#     end = 0
#
#     for start in range(len(gems)):
#         # if end == len(gems)-1 and num_category != len(set(gems[start:end+1])):
#         #     break
#         while num_category != len(set(gems[start:end+1])) and end < len(gems)-1:
#             end += 1
#
#         if num_category == len(set(gems[start:end+1])):
#             if not answer:
#                 answer = [start+1, end+1]
#             else:
#                 if (answer[1] - answer[0]) > ((end+1) - (start+1)):
#                     answer = [start+1, end+1]
#
#     return answer

# (정확성O, 효율성O)
def solution(gems):
    answer = []
    start, end = 0, 0
    num_types = len(set(gems))
    cnt_dict = {}

    while end < len(gems):
        gem = gems[end]
        if gem not in cnt_dict:
            cnt_dict[gem] = 1
        else:
            cnt_dict[gem] += 1

        while start < end:
            gem = gems[start]
            if cnt_dict[gem] >= 2:
                cnt_dict[gem] -= 1
                start += 1
            else:
                break

        if num_types == len(cnt_dict):
            answer.append([start+1, end+1])
        end += 1

    return sorted(answer, key=lambda x: x[1]-x[0])[0]


gems = ["A", "B", "B", "C", "B", "A", "C"]
print(solution(gems))
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
