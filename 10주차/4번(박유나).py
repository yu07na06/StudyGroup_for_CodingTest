from collections import deque

# input
N=int(input()) # 보드 크기
A=int(input()) # 사과 개수
Aposition=[list(map(int, input().split())) for _ in range(A)] # 사과 위치
L=int(input()) # 뱀 방향 변환 횟수
Ldata=list(input().split() for _ in range(L)) # 시간, 방향(L:왼쪽, D:오른쪽)


# setting
board=[[0]*(N+1) for _ in range(N+1)]
board1=[['-']*(N+1) for _ in range(N+1)]
for position in Aposition:
    x, y = position
    board[x][y] = 1 # 사과 위치
rotationL={(0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0), (1,0):(0,1)}
rotationD={(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
snake=deque()

board1[1][1]="*"
head=(1,1); timer=0; vector=(0,1); FLAG = False; i=0
snake.append((1,1))


# run
while(True):
    if i >= L: time = 101
    else : time, rotation = Ldata[i]
    while(timer < int(time)):
        head = tuple(sum(elem) for elem in zip(head, vector))
        x, y = head
        if x<=0 or x>=(N+1) or y<=0 or y>=(N+1): FLAG = True; break # 범위 벗어나면,
        if (x, y) in snake: FLAG = True; break # 몸이랑 부딪히면,

        snake.append((x, y)) # 뱀
        timer+=1

        board1[x][y]='*'
        if board[x][y] == 1:
            board[x][y] = 0
            continue

        snake.popleft() # 뱀
    i+=1
    if FLAG: break
    vector = rotationL[vector] if rotation == 'L' else rotationD[vector] # 방향 전환
print(timer+1)
