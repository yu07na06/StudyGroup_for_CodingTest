#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int n, m, ans = -1;
int a[8][8];      // 0빈칸 1벽 2바이러스
int cpy_a[8][8];  // 원본저장용
bool check[8][8];
vector<pii> pos0;
vector<int> permu;

int bfs() {
    for (int i = 0; i < permu.size(); ++i) {
        if (permu[i] == 1) {
            const auto& [r, c] = pos0[i];
            a[r][c] = 1;
        }
    }

    queue<pii> q;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 2) {
                q.push({i, j});
                check[i][j] = true;
            }
        }
    }

    while (!q.empty()) {
        const auto& [r, c] = q.front();
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (0 > nr || 0 > nc || n <= nr || m <= nc) continue;
            if (a[nr][nc] != 0 || check[nr][nc]) continue;
            if (a[nr][nc] == 0) {
                a[nr][nc] = 2;
                check[nr][nc] = true;
                q.push({nr, nc});
            }
        }
    }

    int ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 0) ++ret;
        }
    }

    return ret;
}

int main() {
    FASTIO;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
            if (a[i][j] == 0) pos0.push_back({i, j});
        }
    }
    memcpy(cpy_a, a, sizeof(a));

    for (int i = 0; i < pos0.size() - 3; ++i) {
        permu.push_back(0);
    }
    for (int i = 0; i < 3; ++i) {
        permu.push_back(1);
    }

    do {
        memcpy(a, cpy_a, sizeof(a));
        memset(check, false, sizeof(check));
        ans = max(ans, bfs());
    } while (next_permutation(permu.begin(), permu.end()));

    cout << ans;
    return 0;
}
