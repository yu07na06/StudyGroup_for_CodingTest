#include <cmath>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
#define union _union
#define endl '\n'
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int parent[3001];
tuple<int, int, int> enemy[3001];
int ans;

int find(int n) {
    if (parent[n] == n) return n;
    return parent[n] = find(parent[n]);
}

void union(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;

    --ans;
    if (a < b)
        parent[b] = a;
    else
        parent[a] = b;
}

bool isConnected(int a, int b) {
    const auto& [x1, y1, r1] = enemy[a];
    const auto& [x2, y2, r2] = enemy[b];

    if (pow(r1 + r2, 2) >= pow(x1 - x2, 2) + pow(y1 - y2, 2)) return true;
    return false;
}

int t;
int main() {
    FASTIO;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        ans = n;

        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
        }

        for (int i = 1; i <= n; ++i) {
            int x, y, r;
            cin >> x >> y >> r;
            enemy[i] = {x, y, r};
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (i == j) continue;
                if (isConnected(i, j)) {
                    union(i, j);
                }
            }
        }

        cout << ans << endl;
    }

    return 0;
}
