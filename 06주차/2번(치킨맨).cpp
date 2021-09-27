#include <cstring>
#include <iostream>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int dr[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[] = {0, -1, -1, -1, 0, 1, 1, 1};

struct Fish {
    int r, c, dir;
};

int ans = 0;

// 1. 상어 먹기 2. 물고기 무빙 3. 상어 무빙
void solve(int board[][4], Fish fish[], int sr, int sc, int eat) {
    int cboard[4][4];  // idx
    Fish cfish[16];    // r, c, dir
    memcpy(cboard, board, sizeof(cboard));
    memcpy(cfish, fish, sizeof(cfish));

    // 1. 상어 물고기 먹기
    int fIdx = cboard[sr][sc];
    eat += fIdx + 1;
    if (ans < eat) ans = eat;  // 최대값 갱신

    int sharkDir = cfish[fIdx].dir;
    cfish[fIdx].dir = -1;  // 죽은 물고기
    cboard[sr][sc] = -1;

    // 2. 물고기 무빙
    for (int i = 0; i < 16; ++i) {
        if (cfish[i].dir == -1) continue;

        const auto [r, c, dir] = cfish[i];  // 현재 위치
        int nr = r + dr[dir];
        int nc = c + dc[dir];
        int nDir = dir;

        while (nr < 0 || nc < 0 || 4 <= nr || 4 <= nc || (nr == sr && nc == sc)) {
            nDir = (nDir + 1) % 8;
            nr = r + dr[nDir];
            nc = c + dc[nDir];
        }

        if (cboard[nr][nc] != -1) {  // 물고기 있으면 자리스왑
            int targetIdx = cboard[nr][nc];
            cfish[i] = {nr, nc, nDir};
            cfish[targetIdx] = {r, c, cfish[targetIdx].dir};

            cboard[nr][nc] = i;
            cboard[r][c] = targetIdx;
        } else {  // 없으면 그냥 이동
            cfish[i] = {nr, nc, nDir};

            cboard[nr][nc] = i;
            cboard[r][c] = -1;
        }
    }
    // 3. 상어 무빙
    for (int i = 1; i <= 3; ++i) {  // 1,2,3칸 이동
        int nr = sr + dr[sharkDir] * i;
        int nc = sc + dc[sharkDir] * i;
        if (0 > nr || 0 > nc || 4 <= nr || 4 <= nc) break;
        if (cboard[nr][nc] != -1) {
            solve(cboard, cfish, nr, nc, eat);
        }
    }
}

int main() {
    FASTIO;
    Fish fish[16];
    int board[4][4];

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int idx, dir;
            cin >> idx >> dir;
            --idx, --dir;
            board[i][j] = idx;
            fish[idx] = {i, j, dir};
        }
    }
    solve(board, fish, 0, 0, 0);
    cout << ans;
    return 0;
}
