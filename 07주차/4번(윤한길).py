d = {
    '1': (0, 0), '2': (1, 0), '3': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '7': (0, 2), '8': (1, 2), '9': (2, 2),
    '*': (0, 3), '0': (1, 3), '#': (2, 3)
}


def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left = str(i)
        elif i in [3, 6, 9]:
            answer += 'R'
            right = str(i)
        else:
            left_dist = abs(d[left][0] - d[str(i)][0]) + abs(d[left][1] - d[str(i)][1])
            right_dist = abs(d[right][0] - d[str(i)][0]) + abs(d[right][1] - d[str(i)][1])
            if left_dist < right_dist:
                answer += 'L'
                left = str(i)
            elif right_dist < left_dist:
                answer += 'R'
                right = str(i)
            else:
                if hand == 'left':
                    answer += 'L'
                    left = str(i)
                else:
                    answer += 'R'
                    right = str(i)

    return answer


if __name__ == '__main__':
    numbers, hand, result = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"
    print(solution(numbers, hand))

"""
numbers	                                hand	    result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	    "right"	    "LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	    "left"	    "LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	        "right"	    "LLRLLRLLRL"
"""