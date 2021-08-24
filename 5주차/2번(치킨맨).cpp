#include <iostream>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)
// 브루트포스, 백트레킹

int dr[] = {0, 0, 1, -1};  // 동서남북
int dc[] = {1, -1, 0, 0};

int n;               // 선택 길이 14, 4^14= 2억
double a[4];         // 0.25 0.25 0.25 0.25
bool check[29][29];  // -14, 0, 14 -> 0, 14, 28

double go(int len, int r, int c) {
    if (len == n) {
        return 1;
    }
    double possible = 0;

    check[r][c] = true;
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (check[nr][nc]) continue;
        possible += go(len + 1, nr, nc) * a[i];
    }
    check[r][c] = false;

    return possible;
}

// 이동경로가 안 겹칠 확률
int main() {
    FASTIO;

    cin >> n;
    for (int i = 0; i < 4; ++i) {
        float p;
        cin >> p;
        a[i] = p / 100.0;
    }

    cout.precision(9);
    cout << go(0, 14, 14);
    return 0;
}
