# 상, 하, 좌, 우, 위, 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def bfs(z, x, y):
    global visited, temp, bfscount

    visited[z][x][y] = True
    for k, i, j in zip(dz, dx, dy):
        nz, nx, ny = z+k, x+i, y+j
        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H: continue # 범위 아웃
        if visited[nz][nx][ny] : continue # 방문했다면,
        if arr[nz][nx][ny] == -1 or arr[nz][nx][ny] == 1: continue # 익지 않은 토마토만 거르기 위해
        visited[nz][nx][ny] = True
        arr[nz][nx][ny]=1
        temp.append((nz, nx, ny)) # 임시 리스트에 넣어줌
        bfscount+=1 # 익지 않은 토마토 카운팅

M, N, H = map(int, input().split()) # M : 가로, N : 세로, H : 높이
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 3차원 행렬
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토 없음

visited = [[[False]*M for _ in range(N)] for _ in range(H)]

tomato=[]
count1=0; count0=0; count_1=0 # 각각의 토마토 카운팅
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                tomato.append((h, n, m)) # 초기 익은 토마토 위치 찾기
                count1 += 1
            elif arr[h][n][m] == 0: count0 += 1
            else: count_1 += 1

if count1+count_1 == M*N*H: # 모든 토마토가 익어있다면,
    print(0)
    exit(0) # 멈춰!!!!

cnt=0; bfscount=0
while len(tomato): # 익은 토마토의 위치가 계속 갱신(갱신이 끝나면, 상자안에는 전부 익었거나 못익을 위치에 토마토가 존재한다는 말)
    temp=[] # 초기화, 깨끗한 마음가짐으로
    for t in tomato: # 익은 토마토의 위치를 탐색
        z, x, y = t
        bfs(z, x, y) # 딱, 익은 토마토의 주변 토마토만 탐색
    tomato=temp # 임시로 저장한 익은 토마토의 위치를 넘겨줌
    cnt+=1 # 하루하루 카운팅

if bfscount == count0: # 익지 않은 토마토를 탐색한 카운팅과 처음에 세었던 익지 않은 토마토의 개수가 같다면,
    print(cnt-1) # 익은 토마토를 전부 익도록 했으므로
else : print(-1) # 익을 수 없는 위치에 토마토가 있으므로
