#include <iostream>
using namespace std;
int dp[10001][4];

int main() {
	
	dp[1][1] = 1, dp[0][2] = 1, dp[0][3] = 1;
	dp[1][1] = 1, dp[1][2] = 1, dp[1][3] = 1;
	/*
	 dp[2][1] = 1+1, 2
	 dp[3][1] = 1+1+1, 2+1, 3
	 dp[4][1] = 1+1+1+1, dp[4][2] = 2+1+1, 2+2, dp[4][3] = 3+1
	*/
	
	for(int i = 2 ; i <= 10000 ; ++i) {
		dp[i][1] = dp[i-1][1];
		dp[i][2] = dp[i-2][1] + dp[i-2][2];
		dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3];
	}
	
	int n, t; cin >> t;
	while(t--) {
		cin >> n;
		cout << dp[n][0] + dp[n][1] + dp[n][2] << '\n';
	}
}
