#include <bits/stdc++.h>
using namespace std;

int N, K;
int W[101], V[101];
int DP[101][100001];

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> K;
  for(int i = 1; i <= N; ++i) cin >> W[i] >> V[i];

  for(int i = 1; i <= N; ++i)
    for(int j = 1; j <= K; ++j)
      DP[i][j] = (j >= W[i]) ? max(DP[i - 1][j], DP[i- 1][j - W[i]] + V[i]) : DP[i - 1][j];

  cout << DP[N][K];
}
