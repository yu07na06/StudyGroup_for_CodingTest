def rotate_90(input_list, clockwise_or_counterclockwise):
    if clockwise_or_counterclockwise == 'clockwise':
        rotated = list(map(list, zip(*input_list[::-1])))
    else:   # counterclockwise
        rotated = list(map(list, zip(*[i[::-1] for i in input_list])))

    return rotated


def solution(key, lock):
    answer = True

    return answer


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solution(key, lock)


"""
key	                                    lock	                                result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	    true
"""