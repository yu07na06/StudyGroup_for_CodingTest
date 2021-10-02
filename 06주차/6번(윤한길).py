from copy import deepcopy


def rotate_90(input_list, clockwise_or_counterclockwise):
    if clockwise_or_counterclockwise == 'clockwise':
        rotated = list(map(list, zip(*input_list[::-1])))
    else:  # counterclockwise
        rotated = list(map(list, zip(*[i[::-1] for i in input_list])))

    return rotated


def list_to_binary(l):
    # tmp = [[str(j) for j in i] for i in l]
    tmp = ''
    for i in l:
        for j in i:
            tmp += str(j)

    return int('0b' + tmp, 2)  # 2진수로 바꾸고 -> 10진수로 반환


def small_key(key, lock):
    while len(key) != len(lock):
        key.append([])
    for i in key:
        while len(i) != len(lock):
            i.append(0)

    return key


def move_right(l):
    for i in range(len(l)):
        l[i].insert(0, 0)
        l[i] = l[i][0:len(l)]


def move_down(l):
    length = len(l)
    l.insert(0, [0] * length)
    return l[0:length]


def solution(key, lock):
    answer = False
    check = 2 ** (len(lock) ** 2) - 1  # ex) 1, 11, 111, 1111  xor 처리했을떄 확인하기 위한 변수
    rotate_tmp = small_key(key, lock)
    # print(key)

    for _ in range(4):
        if answer:
            break

        rotate_tmp = rotate_90(rotate_tmp, 'clockwise')

        for i in range(len(lock)):
            copied_tmp = deepcopy(rotate_tmp)
            if i != 0:
                move_right(copied_tmp)
            for j in range(len(lock)):
                if j != 0:
                    copied_tmp = move_down(copied_tmp)
                tmp = list_to_binary(copied_tmp)
                if list_to_binary(lock) ^ tmp == check:
                    answer = True
                    break


    # for i in range(4):
    #     if answer:
    #         break
    #
    #     rotate_tmp = rotate_90(rotate_tmp, 'clockwise')
    #     tmp = list_to_binary(rotate_tmp)
    #     for j in range(len(bin(tmp)) - 2):
    #         if list_to_binary(lock) ^ (tmp >> j) == check:
    #             answer = True
    #             break
    #         if list_to_binary(lock) ^ (tmp << j) == check:
    #             answer = True
    #             break

    return answer


if __name__ == '__main__':
    key = [[0, 1],
           [1, 0]]
    lock = [[1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]]
    print(solution(key, lock))

"""
key	                                    lock	                                result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	    true
"""