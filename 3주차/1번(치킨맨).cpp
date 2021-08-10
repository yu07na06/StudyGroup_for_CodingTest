#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// 최장경로
int n, m;
vector<int> a[10001];        // 그래프
pair<int, int> hack[10001];  // {cnt, idx}
bool check[10001];           // 방문여부

int bfs(int n) {
    queue<int> q;
    int cnt = 1;  // 출발노드
    check[n] = true;
    q.push(n);  // 출발점

    while (!q.empty()) {
        int now = q.front();
        q.pop();

        for (int next : a[now]) {
            if (check[next]) continue;

            q.push(next);
            check[next] = true;
            ++cnt;
        }
    }

    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        hack[i].second = i;
    }
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> v >> u;  // 도착, 출발
        a[u].push_back(v);
    }

    for (int i = 1; i <= n; ++i) {
        memset(check, false, sizeof(check));
        hack[i].first = -bfs(i);
    }

    sort(hack + 1, hack + n + 1);

    cout << hack[1].second << ' ';
    for (int i = 2; i <= n; ++i) {
        if (hack[1].first == hack[i].first) cout << hack[i].second << ' ';
    }

    return 0;
}
