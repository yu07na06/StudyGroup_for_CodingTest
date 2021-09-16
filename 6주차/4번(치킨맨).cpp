#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int n;
vector<int> a;

int main() {
    FASTIO;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int b;
        cin >> b;

        auto it = lower_bound(a.begin(), a.end(), b);
        if (it != a.end()) {  // 발견되면 그 위치 값 수정
            *it = b;
        } else {  // 발견 안되면 끝에 추가
            a.push_back(b);
        }
    }

    cout << a.size();
    return 0;
}
