from collections import deque


def rotate_90(l):
    return list(map(list, zip(*l[::-1])))


def bfs(i, j, board, visited, empty, n):
    section = []
    dq = deque([[i, j]])
    length = len(board)

    while dq:
        x, y = dq.popleft()
        if 0 <= x < length and 0 <= y < length:
            if not visited[x][y] and board[x][y] == n:
                visited[x][y] = True
                section.append((x, y))

                dq.append((x - 1, y))
                dq.append((x + 1, y))
                dq.append((x, y - 1))
                dq.append((x, y + 1))

    empty.append(sorted(section))


def solution(game_board, table):
    answer = []
    length = len(game_board)

    visited_board, visited_table = [list(False for _ in range(length)) for _ in range(length)], [
        list(False for _ in range(length)) for _ in range(length)]
    empty_board, empty_table = [], []

    for i in range(length):
        for j in range(length):
            if not visited_board[i][j] and game_board[i][j] == 0:
                bfs(i, j, game_board, visited_board, empty_board, 0)
            if not visited_table[i][j] and table[i][j] == 1:
                bfs(i, j, table, visited_table, empty_table, 1)
    print(empty_board)
    print(empty_table)


if __name__ == '__main__':
    game_board = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0, 0]]
    table = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0]]
    solution(game_board, table)
