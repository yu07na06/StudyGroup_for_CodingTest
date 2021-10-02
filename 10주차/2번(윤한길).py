def solution(lottos, win_nums):
    num_zeros = lottos.count(0)
    set_lottos = set(lottos) - set([0])
    set_win_nums = set(win_nums)

    intersection_nums = len(set_win_nums & set_lottos)
    answer = [intersection_nums + num_zeros, intersection_nums] # 매치된 갯수(최대, 최소)
    # answer = [1 if i == 6 else 2 if i == 5 else 3 if i == 4 else 4 if i == 3 else 5 if i == 2 else 6 for i in answer]
    answer = [7 - i if 2 <= i <= 6 else 6 for i in answer]

    return answer


if __name__ == '__main__':
    lottos, win_nums, result = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19], [3, 5]
    print(solution(lottos, win_nums))

    lottos, win_nums, result = [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25], [1, 6]
    print(solution(lottos, win_nums))

    lottos, win_nums, result = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35], [1, 1]
    print(solution(lottos, win_nums))