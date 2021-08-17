import copy
from collections import deque

#상, 하, 좌, 우
dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

""" 1. 바이러스 퍼트리기 """
def spreed_virus():
    global out
    count=0; WALL=3
    queue_2_cp=copy.deepcopy(queue_2) #바이러스 위치는 매번 새로 갱신하여 사용
    while queue_2_cp: #바이러스 위치는 계속해서 업데이트
        i, j = queue_2_cp.popleft() #바이러스 위치 꺼내기
        for v, w in zip(dx, dy): #상하좌우 살펴보고, 바이러스 퍼트리기
            new_x, new_y=i+v, j+w #상하좌우
            if new_x<0 or new_x>=N or new_y<0 or new_y>=M: continue #범위 아웃
            if Arr_cp[new_x][new_y]==1 or Arr_cp[new_x][new_y]==2: continue #상하좌우에 벽이나 바이러스가 있는 경우
            Arr_cp[new_x][new_y]=2 #조건 외에는 바이러스 퍼트리기
            queue_2_cp.append((new_x, new_y)) #퍼트린 새로운 바이러스 위치 업데이트
            count+=1 #퍼트린 바이러스 갯수 세기

    if len(position_0)-count-WALL> out: #빈칸의 갯수에서 설치한 3개의 벽과 추가적으로 퍼트린 바이러스의 갯수를 뺀 나머지 빈칸의 갯수
        out=len(position_0)-count-WALL #빈칸의 갯수 최대값 찾기

""" 2. 벽 설치하기 """
def wall(cnt):
    global Arr_cp
    if cnt==3: #벽 3개를 설치했으므로, 바이러스 퍼트리고 종료
        spreed_virus() #바이러스 퍼트리고, 빈칸 세기
        return True #종료

    for i, j in position_0: #벽이 3개가 아니라면, 빈칸 위치만 탐색
        if Arr[i][j]==0: #빈칸일 경우, (재귀 전에 행렬에 벽을 하나 설치했기 때문에 확인하는 과정이 필요)
            Arr[i][j]=1 #빈칸에 벽을 설치
            Arr_cp=copy.deepcopy(Arr)
            wall(cnt+1) #벽 하나 설치했으므로 1증가
            Arr[i][j]=0 #벽 해제
            
def main():
    global Arr, N, M, position_0, queue_2, out
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for i in range(N)]
    
    position_0=[]
    queue_2=deque()
    for i in range(N):
        for j in range(M):
            if Arr[i][j]==0: #빈칸 위치를 저장하면, 사용하기 편리하기 때문
                position_0.append((i, j))
            elif Arr[i][j]==2: #바이러스 위치 저장해서 사용하기 위해서
                queue_2.append((i, j))

    out=0 #빈칸의 갯수 최대값 찾기 위한 비교변수 초기화
    wall(0) #벽 3개 설치하기
    print(out) #최종 빈칸 갯수 출력

if __name__ == "__main__":
    main()
