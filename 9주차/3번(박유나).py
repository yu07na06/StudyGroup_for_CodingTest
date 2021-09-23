def solution(weights, head2head):
    head = [list(i) for i in head2head] # 2차원 리스트로
    lenHead = len(head2head[0]) # 길이만큼
    result = [[0]*4 for _ in range(len(weights))] # [ 인덱스, 승률, 무거운 복서 이긴 횟수, 자신의 몸무게 ]

    for i, h in enumerate(head): # 인덱스와 각 리스트 행
        winCount=0; loseCount=0 # 이긴 카운팅과 진 카운팅
        result[i][0]=i+1 # 인덱스 삽입
        result[i][3]=weights[i] # 자신의 몸무게 삽입
        for j in range(lenHead):
            if i==j : continue # 자기 자신꺼는 넘어감
            if h[j]=="N" : continue # None 이면, 넘어감
            if h[j]=="W": # 이겼다.
                if weights[j]>weights[i]: # 무거운 상대 이긴 횟수
                    result[i][2]+=1 # 카운팅
                winCount+=1
            else: # 졌다
                loseCount+=1
        result[i][1]= winCount/(winCount+loseCount) if winCount+loseCount!=0 else 0# 승률 계산

    result.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0])) # 우선 순위에 따른 정렬
    return [x[0] for x in result]
