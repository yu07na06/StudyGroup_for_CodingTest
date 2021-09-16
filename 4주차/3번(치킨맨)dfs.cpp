#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

int n, m, ans = -1;
int a[8][8];  // 0빈칸 1벽 2바이러스
int cpy_a[8][8];
bool check[8][8];
vector<pii> pos0;  // wall 넣을 후보
vector<int> permu;

void dfs(int r, int c) {
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (0 <= nr && nr < n && 0 <= nc && nc < m)
            if (a[nr][nc] == 0) {
                a[nr][nc] = 2;
                dfs(nr, nc);
            }
    }
}

int main() {
    FASTIO;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
            if (a[i][j] == 0)
                pos0.push_back({i, j});
        }
    }

    for (int i = 0; i < pos0.size() - 3; ++i)
        permu.push_back(0);
    for (int i = 0; i < 3; ++i)
        permu.push_back(1);
    memcpy(cpy_a, a, sizeof(a));

    do {
        memcpy(a, cpy_a, sizeof(a));
        memset(check, 0, sizeof(check));
        for (int i = 0; i < permu.size(); ++i) {
            if (permu[i] == 1) {
                auto pos = pos0[i];
                a[pos.first][pos.second] = 1;  // 벽새우기
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == 2)
                    dfs(i, j);
            }
        }

        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == 0) cnt++;
            }
        }
        ans = max(ans, cnt);

    } while (next_permutation(permu.begin(), permu.end()));

    cout << ans;
    return 0;
}
