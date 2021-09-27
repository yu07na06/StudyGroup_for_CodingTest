#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;
int t,n,ans;
int num[10]={6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
int min_num[9] = {0, 0, 1, 7, 4, 2, 6, 8, 10};
string min_dp[MAX], add_dp[MAX];
int main(){
	// 자릿수 최소화, 자릿수 최대화
	/*
	min_dp[2] = 1, max_dp[2] = 1;
	min_dp[3] = 7, max_dp[3] = 7;
	min_dp[4] = 4, max_dp[4] = 11;
	min_dp[5] = 2, max_dp[5] = 71;
	min_dp[6] = 6, max_dp[6] = 111;  //min_dp[6] = 0;
	min_dp[7] = 8, max_dp[7] = 711;

	min_dp[8] = 1+0, max_dp[8] = 1111;
	min_dp[9] = 1+8, max_dp[9] = 7111;
	min_dp[10] = 2+2, max_dp[10] = 11111;
	min_dp[11] = 2+0;
	min_dp[12] = 2+8;
	min_dp[13] = 6+8;
	min_dp[14] = 8+8;
	
	min_dp[15] = 1+08;
	min_dp[16] = 1+68;
	*/

	min_dp[2] = "1";
	min_dp[3] = "7";
	min_dp[4] = "4";
	min_dp[5] = "2";
	min_dp[6] = "6";  // or 0
	min_dp[7] = "8";
	min_dp[8] = "10";
	
	add_dp[2] = "1";
	add_dp[3] = "7";
	add_dp[4] = "4";
	add_dp[5] = "2";
	add_dp[6] = "0";
	add_dp[7] = "8";
	
	for(int i=9; i < 101; ++i) {
	    min_dp[i]="9999999999999999999999999999999999999999999999999999999999999999999999";
	    for(int j=2; j<=7; ++j) {
	        if(min_dp[i].size() > (min_dp[i-j] + add_dp[j]).size()) {
	            min_dp[i] = min_dp[i-j] + add_dp[j];
	        } else if (min_dp[i].size() == (min_dp[i-j] + add_dp[j]).size()) {
	            min_dp[i] = min(min_dp[i], min_dp[i-j] + add_dp[j]);
	        }
    		
    	   // cout<< i << " : " << min_dp[i] << ", "<< min_dp[i-j] + add_dp[j] <<'\n';
	    }
	}
	
	cin>>t;
	while(t--){
		cin>>n;
		cout << min_dp[n] << ' ';
		
		string max_ans = "";
		
		for(int i=0; i< n/2; ++i) max_ans = "1"+max_ans;
		if(n%2==1) max_ans[0]='7';
		
		cout << max_ans << '\n';
	}
	return 0;
}
