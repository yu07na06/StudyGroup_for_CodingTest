#include <bits/stdc++.h>

#define X first
#define Y second

using namespace std;
 
int lab[8][8];
int tempLab[8][8];
int N, M;
int ans = 0;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

void mapCopy(int a[][8], int b[][8]) {
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
      a[i][j] = b[i][j];
}

void doVirus() {
  int spreadLab[8][8];
  mapCopy(spreadLab, tempLab);
  queue<pair<int, int> > q;
  // 바이러스 위치 확인 후 큐에 대입
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
      if (spreadLab[i][j] == 2)
        q.push({i, j});

  // bfs 탐색으로 바이러스 퍼트리기
  while (!q.empty()) {
    int x = q.front().X;
    int y = q.front().Y;
    q.pop();
    for(int i = 0; i < 4; ++i) {
      int a = x + dx[i];
      int b = y + dy[i];
      if(0 <= a && a < N && 0 <= b && b < M) {
        if(spreadLab[a][b] == 0) {
          spreadLab[a][b] = 2;
          q.push({a, b});
        }
      }
    }
  }

  // 바이러스 퍼진 영역 개수 측정
  int area = 0;
  for(int i = 0; i < N; ++i)
    for(int j = 0; j < M; ++j)
      if(spreadLab[i][j] == 0) ++area;
  ans = max(ans, area);
}

void wall(int cnt) {
  // 설치한 벽이 3개일 경우 바이러스 살포
  if(cnt == 3) {
      doVirus();
      return;
  }

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      if(tempLab[i][j] == 0) {
          tempLab[i][j] = 1;
          wall(cnt + 1);
          tempLab[i][j] = 0;
      }
    }
  }
}
 
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;
  for(int i = 0; i < N; ++i)
      for(int j = 0; j < M; ++j)
          cin >> lab[i][j];

  for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        // 빈 칸일경우 벽 설치
        if(lab[i][j] == 0){
            mapCopy(tempLab, lab);
            tempLab[i][j] = 1;
            wall(1);
            tempLab[i][j] = 0;
        }
      }
  }
  cout << ans;
}
