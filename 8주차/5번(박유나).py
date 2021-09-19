/* 실패~~ */

from collections import deque
import copy

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def rotate(lst):
    n = len(lst)
    ret = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = lst[i][j]
    return ret


def fill_board(puzzle): # 보드 채우기
    global board, count

    count=0
    for p in puzzle: # 배열 하나씩
        p_length=len(p) # 퍼즐 덩어리 길이
        for i, b in enumerate(board):
            if p_length == len(b): # 퍼즐 덩어리 길이와 보드 빈칸 길이가 같다면,
                temp=[]
                bx, by = b[0]
                px, py = p[0]
                x, y = bx-px, by-py # 이동해서 계산...
                for a in p:
                    ppx, ppy = a
                    temp.append((ppx+x, ppy+y))
                if temp == p:
                    del board[i]
                    count+=p_length # 안된다...
                

def find_puzzle(x, y): # 퍼즐 덩어리 찾기
    global puzzle_exis, t_length, puzzle_location

    q=deque()
    q.append((x, y))
    puzzle_exis[x][y]=0 # 퍼즐 존재하지 않는다고 표기
    temp_location=[(x, y)] # 퍼즐 위치 저장

    while q:
        x, y = q.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x+i, y+j
            if nx < 0 or nx >= t_length or ny < 0 or ny >= t_length: continue # 범위 벗어났을때
            if puzzle_exis[nx][ny]==0: continue # 퍼즐이 존재하지 않을때
            q.append((nx, ny))
            temp_location.append((nx, ny))
            puzzle_exis[nx][ny]=0
    puzzle_location.append(temp_location) # 각각의 퍼즐 덩어리 저장



def solution(game_board, table):
    global t_length, puzzle_exis, board_location, board, count, puzzle_location

    g_length=len(game_board); t_length=len(table) # 보드과 테이블의 길이
    board_fill=copy.deepcopy(game_board) # 채운 보드 상태

    temp_queue=deque()
    board_location=[] # 보드 빈칸 덩어리 저장
    # 빈칸 보드 위치 저장
    for i in range(g_length):
        for j in range(g_length):
            if(board_fill[i][j]==1): continue # 채워진 보드 확인
            temp_queue.append((i, j))
            temp_location=[(i, j)]
            board_fill[i][j]=1
            while temp_queue:
                x, y = temp_queue.popleft()
                for i, j in zip(dx, dy):
                    nx, ny = x+i, y+j
                    if nx < 0 or nx >= t_length or ny < 0 or ny >= t_length: continue # 범위 벗어났을때
                    if board_fill[nx][ny]==1: continue # 퍼즐이 존재하지 않을때
                    temp_queue.append((nx, ny))
                    temp_location.append((nx, ny)) # 보드 빈칸 저장
                    board_fill[nx][ny]=1 # 빈칸 보드를 채워졌다고 표기
            board_location.append(temp_location) # 각각의 보드 빈칸들 넣기
    
    max_v=0
    # 회전하는 퍼즐 덩어리 찾기 및 보드 채우기
    for _ in range(4): # 4번 90도로 회전
        puzzle_exis=copy.deepcopy(table) # 퍼즐 유무 상태
        puzzle_exis=rotate(puzzle_exis) # 퍼즐 회전
        board=copy.deepcopy(board_location) # 보드 빈칸 복사
        puzzle_location=[] # 퍼즐 덩어리들 위치

        for i in range(t_length):
            for j in range(t_length):
                if(puzzle_exis[i][j]==0): continue # 퍼즐 유무 여부
                find_puzzle(i, j) # 퍼즐 덩어리 찾기
        fill_board(puzzle_location) # 보드 채우기
        max_v=max(count, max_v) # 채운 칸 수

    print(max_v)


solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
#solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]])
