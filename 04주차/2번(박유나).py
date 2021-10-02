""" 참고 사이트 : https://inspirit941.tistory.com/185 """

from itertools import permutations

#외벽둘레, 취약위치배열, 이동거리배열
def solution(n, weak, dist):
    len_w=len(weak)
    for i in range(len_w): #[1, 5, 6, 10]
        weak.append(weak[i]+n) #[1, 5, 6, 10, 13, 17, 18, 22] 이렇게 늘린다.

    answer=len(dist)+1
    for i in range(len_w):
        start=[weak[j] for j in range(i, i+len_w)] #(1~10, 5~13, 6~17, 10~18)
        candi=permutations(dist, len(dist))
        for order in candi:
            index, count=0,1
            length=start[0]+order[index]

            for s in range(len_w):
                if start[s]>length:
                    count+=1
                    if count>len(order):
                        break
                    index+=1
                    length=order[index]+start[s]
            answer=min(answer, count)
    if answer>len(dist):
        return -1
    return answer
