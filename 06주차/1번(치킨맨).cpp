#include <iostream>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

// 모든 i번세로선출발-> i번끝에 도달하게 할때 추가할 가로선 개수의 최솟값
// 도달 가능하면 추가된 선갯수 최소값 출력(0,1,2,3), 불가능 or ans>3이면 -1
// 270 choose 3 = 32만

int r, c, n;       // 가로선 갯수, 세로선 갯수, 그릴수 있는 가로선갯수
int a[31][11];     // r30 c10 a[i][j] = i가로선 j세로선의 가로선, 1왼쪽<->2오른쪽
vector<pii> cand;  // 그릴수 있는 가로선 후보 {r,c}

bool goBottom() {
    for (int j = 1; j <= c; ++j) {
        int nowc = j;
        for (int i = 1; i <= r; ++i) {
            if (a[i][nowc] == 1)
                ++nowc;
            else if (a[i][nowc] == 2)
                --nowc;
        }
        if (nowc != j) return false;
    }
    return true;
}

int main() {
    FASTIO;
    cin >> c >> n >> r;  // 세로선갯수, 그릴수있는 가로선갯수, 가로선갯수
    for (int i = 0; i < n; ++i) {
        int nowr, nowc;
        cin >> nowr >> nowc;
        a[nowr][nowc] = 1;      // 왼쪽
        a[nowr][nowc + 1] = 2;  // 오른쪽
    }
    for (int i = 1; i <= r; ++i) {
        for (int j = 1; j <= c - 1; ++j) {
            if (a[i][j] != 0 | a[i][j + 1] != 0) continue;
            cand.push_back({i, j});
        }
    }
    // cand중에 0개or1개or2개or3개 선택해서 모든 시작점에서 끝까지 도달해야됨
    int ans = -1;
    if (goBottom()) {  // 선택 0개 체크
        cout << 0;
        return 0;
    }

    for (int ch1 = 0; ch1 < cand.size(); ++ch1) {  // 선택1
        const auto& [r1, c1] = cand[ch1];
        a[r1][c1] = 1, a[r1][c1 + 1] = 2;

        if (goBottom()) {
            if (ans == -1 || ans > 1) {
                ans = 1;
            }
        }

        for (int ch2 = ch1 + 1; ch2 < cand.size(); ++ch2) {
            const auto& [r2, c2] = cand[ch2];
            if (a[r2][c2] != 0 || a[r2][c2 + 1] != 0) continue;

            a[r2][c2] = 1, a[r2][c2 + 1] = 2;
            if (goBottom()) {
                if (ans == -1 || ans > 2) {
                    ans = 2;
                }
            }

            for (int ch3 = ch2 + 1; ch3 < cand.size(); ++ch3) {
                const auto& [r3, c3] = cand[ch3];
                if (a[r3][c3] != 0 || a[r3][c3 + 1] != 0) continue;
                a[r3][c3] = 1, a[r3][c3 + 1] = 2;
                if (goBottom()) {
                    if (ans == -1 || ans > 3) {
                        ans = 3;
                    }
                }

                a[r3][c3] = 0, a[r3][c3 + 1] = 0;
            }
            a[r2][c2] = 0, a[r2][c2 + 1] = 0;
        }
        a[r1][c1] = 0, a[r1][c1 + 1] = 0;
    }

    cout << ans;
    return 0;
}
