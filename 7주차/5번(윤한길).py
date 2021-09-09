# def solution(s):
#     answer = s.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', "4").replace('five', '5').replace('six', '6')\
#         .replace('seven', '7').replace('eight', '8').replace('nine', "9").replace('zero', '0')
#     return answer

import re


replacements = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ('zero', '0'),
]


def solution(s):
    for before, after in replacements:
        s = re.sub(before, after, s)
    return int(s)


if __name__ == '__main__':
    s = "one4seveneight"
    print(solution(s))

    s = "23four5six7"
    print(solution(s))

    s = "2three45sixseven"
    print(solution(s))

    s = "123"
    print(solution(s))

"""
숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
"""