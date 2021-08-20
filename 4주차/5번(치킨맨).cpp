#include <algorithm>
#include <iostream>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int n, k;            // 물품100, 무게10만
int w[101], v[101];  // 물건별 무게, 가치
int d[101][100001];  // d[i][j] = max(i개 까지 고려했을 때 j무게로 담을 수 있는 가치)

int go(int i, int totW) {
    if (i > n) return 0;
    if (d[i][totW]) return d[i][totW];

    int ans = 0;
    if (w[i] + totW <= k) {  // w[i] 담을 수 있으면 넣고 계속 탐색
        ans = go(i + 1, w[i] + totW) + v[i];
    }
    ans = max(ans, go(i + 1, totW));

    return d[i][totW] = ans;
}

int main() {
    FASTIO;

    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        cin >> w[i] >> v[i];
    }

    cout << go(1, 0);
    return 0;
}
