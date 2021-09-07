from bisect import bisect_left
from collections import deque


def solution(n, k, cmd):
    answer = ''
    init = [i for i in range(n)]
    copied = init[:]
    removed = deque()
    current = k
    for i in cmd:
        if i[0] == 'U':
            current -= int(i[2:])
        elif i[0] == 'D':
            current += int(i[2:])
        elif i[0] == 'C':
            removed.append(copied.pop(current))
            if current > len(copied)-1:
                current -= 1
        elif i[0] == 'Z':
            tmp = removed.pop()
            idx = bisect_left(copied, tmp)
            copied.insert(idx, tmp)
            if idx <= current:
                current += 1

    for i in init:
        if i in copied:
            answer += 'O'
        else:
            answer += 'X'

    return answer


if __name__ == '__main__':
    n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    print(solution(n, k, cmd))

    n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    print(solution(n, k, cmd))


"""
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

n	k	cmd	                                                        result
8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	            "OOOOXOOO"
8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	    "OOXOXOOO"
"""