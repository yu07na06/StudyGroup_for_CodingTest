from collections import deque


def solution(board):
    def bfs(start):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        dd = ['상', '하', '좌', '우']

        length = len(board)
        table = [[float('inf') for _ in range(length)] for _ in range(length)]
        table[0][0] = 0

        queue = deque([start])

        while queue:
            y, x, cost, head = queue.popleft()
            for i in range(4):
                new_y, new_x = y + dy[i], x + dx[i]
                new_cost = cost + 600 if dd[i] != head else cost + 100
                if 0 <= new_y < length and 0 <= new_x < length:
                    if board[new_y][new_x] == 0 and new_cost < table[new_y][new_x]:
                        table[new_y][new_x] = new_cost
                        queue.append((new_y, new_x, new_cost, dd[i]))
        return table[-1][-1]

    return min(bfs((0, 0, 0, '우')), bfs((0, 0, 0, '하')))


if __name__ == '__main__':
    board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
    print(solution(board))