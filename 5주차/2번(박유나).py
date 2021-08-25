N,e,w,s,n = map(int, input().split()) #이동거리, 동, 서, 남, 북 분리하기
HR=100
ewsn = [e/HR,w/HR,s/HR,n/HR] #각각의 확률을 100으로 나누기
visited = [[0 for i in range(N*2)] for ii in range(N*2)]
dx, dy = [1,-1,0,0], [0,0,-1,1] #상,하,좌,우

def dfs(count, x, y):
    if count==N: #N만큼 이동했다면, 그만
        return 1
    visited[x][y] = 1 #방문 표시하기
    ret = 0
    for i in range(4):
        X, Y = x+dx[i], y+dy[i] #이동할 상,하,좌,우
        if visited[X][Y]:continue #방문하였다면 무시하고 진행
        ret += dfs(count+1,X,Y)*ewsn[i] #dfs는 카운트 세고, 각각의 확률 곱해주기
    visited[x][y] = 0 #방문 표시 없애기
    return ret #최종 확률 출력

print(dfs(0,0,0))
