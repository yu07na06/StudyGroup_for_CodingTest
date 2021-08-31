'''
5 5 6
1 1
3 2
2 3
5 1
5 4
out: 3

첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.
가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.
가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가한다. 세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.
입력으로 주어지는 가로선이 서로 연속하는 경우는 없다.
'''

import sys


def examine():                      # 사다리 결과 검수 함수
    for i in range(N):
        tmp = i
        for j in range(H):
            if ladder[j][tmp]:      # 현 위치에 연결로 있으면 우측이동
                tmp += 1
            elif ladder[j][tmp-1]:    # 이전 위치에 연결로 있으면 좌측이동
                tmp -= 1
        if tmp != i:
            return False            # 시작지점에서 끝나지 않으면 False 리턴
    return True                     # 모든 세로선이 같은 지점에서 끝나므로 True 리턴


def dfs(start, cnt):
    global res
    if cnt == min_cnt:              # min_cnt가 0, 1, 2, 3 일때 각각 처리하다가 examine함수가 True 리턴시 res를 현재 cnt 값을 넣어주고 빠져나오기
        if examine():
            res = cnt
        return
    for i in range(start, H):       # 시간 단축을위해 재귀함수들어갈때 지난 세로선은 처리 안하게 하기
        for j in range(N-1):
            if not ladder[i][j] | ladder[i][j-1] | ladder[i][j+1]:      # 세로선이 연결되면 안되므로 현재, 왼쪽, 우측에 사다리가 없을경우에만 추가하기
                ladder[i][j] = True                                     # 사다리 추가
                dfs(i, cnt+1)
                ladder[i][j] = False                                    # 백트레킹을 위해 재귀가 끝나면 처리된 사다리 제거


if __name__ == '__main__':
    # 입력값들 받기
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    ladder = [[False]*N for _ in range(H)]
    for i in range(M):
        a, b = map(int, input().split())
        ladder[a-1][b-1] = True

    res = 10000
    for min_cnt in range(4):        # cnt가 0~3의 경우를 체크
        dfs(0, 0)
        if res != 10000:            # examine함수가 True 반환시 res값이 cnt값으로 변환되어 빠져나와서 res를 프린트하고 루프 종료
            print(res)
            break
    else:
        print(-1)                   # 0~3 범위내에 답이 없을시 -1반환(사다리를 넣어 답을 구할수 없는경우, cnt가 3이 초과하는 경우)
