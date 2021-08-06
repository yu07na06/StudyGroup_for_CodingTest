#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#define MAX 100001
using namespace std;
int t,n,resume,interview,ans;
pair<int, int> applicant[MAX];

int main(){
	cin>>t;
	while(t--) {
		memset(applicant, 0, sizeof(applicant));
		ans = 1;
		
		cin>>n;
		for(int i=0;i<n;++i) {
			cin>>resume>>interview;
			applicant[i]={resume, interview};
		}
		sort(applicant, applicant+n);
		
		int tmp_min_interview = applicant[0].second;
		for(int i=1;i<n;i++){
			if (applicant[i].second < tmp_min_interview) {
				ans++;
				tmp_min_interview = applicant[i].second;
			}
		}
		
		cout<<ans<<'\n';
	}
	return 0;
}
