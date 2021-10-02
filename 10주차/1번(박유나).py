def find_gep(*data):
    list_data=[]
    for d in data:
        if d <= 0:
            list_data.append(d)
    return max(list_data)

def changeLR(L, R, v1):
    global left, right

    if L + v1 == left or R + v1 == right: # left 값이다.
        if left < L:
            left=L
        if right < R:
            right=R
        return
    if L + v1 == right or R + v1 == left: # right 값이다.
        if left < R:
            left=R
        if right < L:
            right=L
        return

    

MAXV=99999999

def solution(sizes):
    global left, right, g_left, g_right

    left, right = sizes[0][0], sizes[0][1] # 기준이 되는 값 첫번째 인덱스로 설정
    del sizes[0] # 첫번째 인덱스 삭제
    g_left, g_right = MAXV, MAXV
    
    for s in sizes: # 남은 배열만큼 반복
        t1, t2 = left-s[0], right-s[1] # 60-30, 50-70
        c1, c2 = left-s[1], right-s[0] # 60-70, 50-30
        min_value = min(t1, t2, c1, c2) # 가장 작은 값 선택

        # 모두 양수
        if min_value > 0 : continue
        
        # 한 쌍이 양수라면,
        if t1*t2 > 0 and t1 > 0 : continue
        if c1*c2 > 0 and c1 > 0: continue

        # 두 쌍다 전부 음수가 있다면,
        max_value = find_gep(t1, t2, c1, c2) # 음수 중에서 가장 큰 값

        # 기준 변경
        changeLR(s[0], s[1], max_value)
    
    return left*right
