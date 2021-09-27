#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)
#define INF 0x3f3f3f3f

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int n, m, ans = INF;    // 맵사이즈50, 바이러스갯수10 // 10C3 = 120
int board[50][50];      // 0빈칸 1벽 2비활성,3활성바이러스
int cpy_board[50][50];  // 원본
int check[50][50];      // 도달시간
vector<pii> vPos;       // 바이러스 좌표1
vector<int> perm;

// 모든칸에 바이러스있는 최소시간, 다 못퍼트리면 -1
int main() {
    FASTIO;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 2) vPos.push_back({i, j});
        }
    }
    memcpy(cpy_board, board, sizeof(board));
    // 1. 활성바이러스 선택해서 배치
    // 2. 전파
    // 3. 시간 카운트
    // ** 비활성 바이러스로 끝나는 위치 예외처리

    for (int i = 0; i < vPos.size() - m; ++i) {
        perm.push_back(0);
    }
    for (int i = 0; i < m; ++i) {
        perm.push_back(1);
    }

    do {
        memcpy(board, cpy_board, sizeof(board));
        memset(check, -1, sizeof(check));

        queue<pii> q;  // 좌표r,c,도달시간 // 1. 활성바이러스 위치 선택해서 배치
        for (int i = 0; i < vPos.size(); ++i) {
            if (perm[i] == 1) {
                const auto& [r, c] = vPos[i];
                q.push({r, c});
                board[r][c] = 3;
                check[r][c] = 0;
            }
        }

        while (!q.empty()) {  // 2. 전파
            const auto& [r, c] = q.front();
            q.pop();

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (0 > nr || 0 > nc || n <= nr || n <= nc) continue;     // 맵범위 체크
                if (check[nr][nc] != -1 || board[nr][nc] == 1) continue;  // 방문여부,벽 체크

                if (board[nr][nc] != 2) board[nr][nc] = 3;  // 비활성 바이러스 예외처리
                check[nr][nc] = check[r][c] + 1;
                q.push({nr, nc});
            }
        }

        // 3. 모든 빈 칸에 전파됬는지 확인하고 전파시간이 가장 긴 칸 체크
        bool noBlank = true;
        int maxTime = -1;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 0) {
                    noBlank = false;
                    goto exit;
                }
                if (board[i][j] != 2 && maxTime < check[i][j]) maxTime = check[i][j];
            }
        }
    exit:

        if (!noBlank) continue;
        if (ans > maxTime) ans = maxTime;

    } while (next_permutation(perm.begin(), perm.end()));

    if (ans == INF)
        cout << -1;
    else
        cout << ans;
    return 0;
}
