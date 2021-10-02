def Exit(): # 종료 함수
    print(0)
    exit()

def check1(arr): # 사다리 확인
    count=0
    for n in range(1, N+1):
        newN=n
        for h in range(1, H+1):
            if arr[h][newN]==0 or arr[h][newN]==-1: continue
            newN=arr[h][newN] # 새로운 값 넣기
        if n!= newN: #끝과 끝이 다르다면,
            count+=1 #카운팅
    
    if count==0:
        return True
    return False

def wall(cnt):
    global ans

    if cnt!=0 and check1(arr): # 가로선 개수가 0이 아니고, 사다리 확인 시 true인 경우,
        ans=min(cnt, ans) # 최소값 찾기

    if cnt==3: #가로선 개수가 3개라면, 종료
        return

    for n in range(1, N): # 1 ~ (N-1)
        for h in range(1, H+1): # 1 ~ H
            if (arr[h][n]!=0 or arr[h][n+1]!=0):continue # 0이 아니라면, 돌아감

            arr[h][n]=n+1 # 가로선 설정
            arr[h][n+1]=n # 가로선 설정

            wall(cnt+1) # 가로선 개수 증가

            arr[h][n]=0 # 가로선 해제
            arr[h][n+1]=0 # 가로선 해제

""" 0. 입력받기 """
N, M, H=map(int, input().split()) # 세로선 개수, 가로선 개수, 높이 개수
if M==0: Exit() # 가로선 개수가 0이라면, 종료
arr = [[0]*(N+1) for _ in range(H+1)] # 사다리 표기(0인덱스 사용하지 않음)

""" 1. 기존 사다리 저장 """
for _ in range(M):
    i, j = map(int, input().split()) 
    arr[i][j]=j+1 # j+1 행값 넣음
    arr[i][j+1]=j # j 행값 넣음
    if 1<=(j-1) and arr[i][j-1]==0: arr[i][j-1]=-1 # 가로선이 연장하지 않기 위해 금지 표기
    if (j+2)<=N and arr[i][j+2]==0: arr[i][j+2]=-1 # 가로선이 연장하지 않기 위해 금지 표기
if check1(arr): Exit() # 사다리 확인 후, true라면 종료

""" 2. 사다리 확인 """
ans=4 # 정답이 4이상으로 나올 수 없기 때문에
wall(0) # 가로선 설정 및 해제
if ans==4: # 최소값이 4라면,
    print(-1) # 가로선을 놓아도 답이 될 수 없다고 판단하여 -1 출력
else:
    print(ans) # 가로선을 놓아서 답이 된다면, 놓은 가로선 개수 출력
