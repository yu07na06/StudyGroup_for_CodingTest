#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int N, M;
vector<int> graph[10001];
bool vis[10001];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int i = 0; i < M; ++i) {
    int a, b;
    cin >> a >> b;
    graph[b].push_back(a);
  }

  priority_queue<pair<int, int> > pq;
  for (int i = 1; i <= N; ++i) {
    memset(vis, false, sizeof(vis));
    
    int cnt = 0;
    queue<int> q;
    q.push(i);
    vis[i] = true;
    while (!q.empty()) {
      int x = q.front();
      q.pop();
      ++cnt;
      for (int j = 0; j < graph[x].size(); ++j) {
        int a = graph[x][j];
        if (!vis[a]) {
          q.push(a);
          vis[a] = true;
        }
      }
    }
    pq.push({cnt, -i});
  }

  int max = pq.top().first;
  while (!pq.empty()) {
    if (pq.top().first != max) break;
    cout << -pq.top().second << ' ';
    pq.pop();
  }
}
