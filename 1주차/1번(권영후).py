'''
-> 완전탐색 구현을 제대로 못함
    => copy and paste...
-> 압축된 문자열 표기한 수의 길이에 대한 처리 생각 못함
    => 100a -> length=4
참조 
-> https://youtu.be/SQP6JT4AoAE
'''

def solution(s):
    answer = len(s)
    for i in range(1, int(len(s)/2) + 1):
        pos = 0
        length = len(s)

        while pos + i <= len(s):
            unit = s[pos:pos+i]
            pos += i

            cnt = 0
            while pos + i <= len(s):
                if unit == s[pos:pos+i]:
                    cnt += 1
                    pos += i
                else:
                    break

            if cnt > 0:
                length -= i * cnt

                if cnt < 9:
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4
        answer = min(answer, length)

    return answer
