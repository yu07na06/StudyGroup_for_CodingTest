#include <iostream>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int n, k;  // 물건갯수100, 최대무게10만 // O(N^2)미만으로 풀어야됨
int w[101], v[101];
int d[101][100001];
// d[i][j] = max(i번째 물건까지 고려해서, 넣은 무게 합이 j)
// d[i-1][j] : i 안 넣은경우
// d[i-1][j -w[i]] + v[i] : i 넣은 경우
// -> O(NK)
int main() {
    FASTIO;
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        cin >> w[i] >> v[i];
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            d[i][j] = d[i - 1][j];
            int rest = j - w[i];
            if (rest >= 0) {
                d[i][j] = max(d[i][j], d[i - 1][rest] + v[i]);
            }
        }
    }
    // 각각의 무게에 대해서 넣을 수 있는 가장 큰 가치
    int ans = -1;
    for (int j = 1; j <= k; ++j) {
        ans = max(ans, d[n][j]);
    }
    cout << ans;
    return 0;
}
