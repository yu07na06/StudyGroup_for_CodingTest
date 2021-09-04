#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
#define INF 987654321
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int n, h, a;  // 길이20만, 높이50만, 석순-종유석 번갈아가면서 등장
vector<int> up, down;
int ans = INF;

int main() {
    FASTIO;
    cin >> n >> h;  // 높이 h
    for (int i = 0; i < n; ++i) {
        cin >> a;
        if (i % 2 == 0)
            up.push_back(a);  // 개똥벌레 위치 <= 석순높이이면 장애물
        else
            down.push_back(a);  // 개똥벌레 위치 >= 종유석이면 장애물
    }

    sort(up.begin(), up.end());
    sort(down.begin(), down.end());

    int range;
    for (int i = 1; i <= h; ++i) {
        int upCnt = up.size() - (lower_bound(up.begin(), up.end(), i) - up.begin());                // i 하한 범위 제거
        int downCnt = down.size() - (upper_bound(down.begin(), down.end(), h - i) - down.begin());  // i 상한 범위 제거

        int obs = upCnt + downCnt;
        if (ans == obs)
            ++range;
        else if (ans > obs) {
            ans = obs;
            range = 1;  // 새로운 최소값 구간 카운트
        }
    }

    cout << ans << ' ' << range;
    return 0;
}
