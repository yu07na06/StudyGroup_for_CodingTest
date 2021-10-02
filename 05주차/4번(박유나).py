""" 시간 초과... """

from itertools import permutations
from collections import deque
import copy
import math

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 상,하,좌,우
def bfs(pos):
    global N, M, visited, cnt
    q=deque()
    visi=copy.deepcopy(visited) # 계속 복사해서 사용
    
    for i in pos:
        q.append(i) # 활성 바이러스 위치 추가하기
        x, y = i
        visi[x][y]=-1 # 비활성 바이러스를 활성 바이러스로 만들어준다.

    count=0
    answer=-1
    while q: # queue가 비워질때까지
        X, Y = q.popleft() # 맨 앞에꺼 꺼냄
        for i, j in zip(dx, dy): #상,하,좌,우로 탐색
            nx, ny = i+X, j+Y
            if nx<0 or nx>=N or ny<0 or ny>=N: continue # 범위를 벗어난다면,
            if visi[nx][ny]=='*' or visi[nx][ny]=='-' or visi[nx][ny]==-1 or visi[nx][ny]!=0: continue # 벽과 비활성 바이러스는 고려하지 않는다.
            q.append((nx, ny)) # 해당 위치좌표 queue에 저장
            count+=1 #빈칸 들린 횟수 카운팅
            if visi[X][Y]==-1: visi[nx][ny]=1 # 바이러스에서 주변 방문 시, 방문 표기
            else: visi[nx][ny]=visi[X][Y]+1 # 바이러스 아닌 곳에서 주변 방문 시, 방문 표기
            answer=max(answer, visi[nx][ny]) # 최대값 찾기
    return answer if cnt==count else -1 # 빈칸 카운팅 횟수가 빈칸의 개수와 같다면, answer 반환 / 다르다면, 바이러스를 퍼트려도 빈칸이 있는 거니까 -1 반환

N, M = map(int, input().split())

""" 1. 바이러스 위치 저장  """
EMPTY=0; WALL=1; VIRUS=2; position=[]; cnt=0
visited=[[0]*N for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]==VIRUS: # 바이러스라면
            position.append((i, j)) # 바이러스 위치좌표 (x, y) 저장
            visited[i][j]='*' # 일단 전부 바이러스 비활성화 시킴
        elif temp[j]==WALL: visited[i][j]='-' # 벽은 -로 만듦
        else: cnt+=1 # 빈칸이라면, 카운팅
if cnt==0: # 빈칸이 하나도 없다면, 바이러스를 퍼트릴 필요 없기에 종료
    print(0) # 바이러스 전부 퍼져있으므로 끝
    exit()

""" 2. M개 선택한 바이러스 위치의 모든 경우의 수 확인  """
positions=list(permutations(position, M)) # 사용할 수 있는 바이러스 갯수(M) 만큼 가능한 경우의 수를 바이러스 위치 좌표로 표기

""" 3. 모든 경우의 수로 바이러스 퍼트려서 최소 시간 구하기 """
answer=math.inf # 최소값을 찾기 위해
for pos in positions:
    if bfs(pos)!=-1: answer=min(answer, bfs(pos)) # 모든 경우의 수에 대해 bfs를 사용하기

print(-1 if answer==(2**31)-1 else answer) # answer이 초기값 그대로라면, 옮길 수 있는게 없으므로 -1 반환 / 아니라면 최소값 반환
