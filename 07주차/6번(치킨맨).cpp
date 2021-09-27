#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#define INF 0x3f3f3f3f
using namespace std;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int d[25][25][4];  // r,c, dir 상하좌우

struct Pos {
    int r, c, dir, w;
    bool operator<(const Pos& other) const {
        return w > other.w;  // minheap
    }
};

int solution(vector<vector<int>> board) {
    int len = board.size();  // 정사각형

    memset(d, INF, sizeof(d));
    for (int i = 0; i < 4; ++i) {
        d[0][0][i] = 0;  // 시작점
    }

    priority_queue<Pos> pq;
    pq.push({0, 0, -1, 0});  // r,c,dir,weight, 0,0 시작은 코너 예외

    while (!pq.empty()) {
        const auto [r, c, dir, w] = pq.top();
        pq.pop();

        for (int i = 0; i < 4; ++i) {  // 0,1,2,3
            int nr = r + dr[i];
            int nc = c + dc[i];
            int nDir = i;
            int nw = w + 100;  // 여기서 +100, 코너이면 +500

            if (0 > nr || 0 > nc || len <= nr || len <= nc) continue;
            if (board[nr][nc] == 1) continue;

            if (dir == 0 || dir == 1) {  // 상하였을 때 좌우면 코너, 좌우일때 상하면 코너
                if (nDir == 2 || nDir == 3) nw += 500;
            }
            if (dir == 2 || dir == 3) {
                if (nDir == 0 || nDir == 1) nw += 500;
            }

            if (nw < d[nr][nc][nDir]) {
                d[nr][nc][nDir] = nw;  // 최소값
                pq.push({nr, nc, nDir, nw});
            }
        }
    }

    int ans = *min_element(d[len - 1][len - 1], d[len - 1][len - 1] + 4);
    return ans;
}
