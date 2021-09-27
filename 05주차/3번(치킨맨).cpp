#include <iostream>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)
#define INF 0x3f3f3f3f

// 마지막 피자 반죽의 위치 출력(1~d), 다 안들어가면 0
int d, n;  // 깊이30만, 반죽갯수30만
int oven[300001];
int dough[300001];

int main() {
    FASTIO;
    cin >> d >> n;
    for (int i = 1; i <= d; ++i) {
        cin >> oven[i];
    }
    oven[0] = INF;

    // 30만^2로 못푸므로 ON^2 미만으로 풀어야됨
    // 이분탐색으로 풀려면 오븐 지름이 정렬되어 있어야됨.
    for (int i = 2; i <= d; ++i) {
        if (oven[i - 1] < oven[i]) {
            oven[i] = oven[i - 1];
        }
    }

    for (int i = 1; i <= n; ++i) {
        cin >> dough[i];
    }

    // oven 내림차순 정렬되어있음
    int floor = d + 1;
    for (int i = 1; i <= n; ++i) {
        if (floor == 0) break;           // 1. n층~1층까지 다 고려하면 종료
        if (dough[i] <= dough[i - 1]) {  // 2. 지금 도우 <= 이전에 넣은 도우
            --floor;
        } else {  // 3. 지금 도우너비 <= 오븐너비
            int l = 0, r = floor - 1;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (dough[i] <= oven[mid]) {  // 3. 오븐너비 이분탐색. 도우 사이즈 <= 오븐사이즈 여야 들어감
                    floor = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
    }

    cout << floor;
    return 0;
}
