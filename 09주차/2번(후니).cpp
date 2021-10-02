#include <iostream>
#include <queue>
using namespace std;
int t,n;
priority_queue<int> pq;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin>>t;
	while(t--){
		cin>>n;
		if(!n) {
		    if(!pq.size()) cout<<"0\n";
			else { 
			    cout<<-pq.top()<<'\n';
			    pq.pop();
			}
		} else pq.push(-n);
	}
	return 0;
}
