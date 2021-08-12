#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#define MAX 100000
using namespace std;
vector<int> ans[MAX], v[MAX];
int max_ans;

int main() {
	int n,m; cin>>n>>m;
	for(int i=0;i<m;++i) {
		int u,e; cin>>u>>e;
		v[e-1].push_back(u-1);
    }
	
	for(int i=0;i<n;++i) {
		int tmp_ans = 0, cnt = 0;
		queue<int> q; int visit[MAX] {};
		q.push(i); visit[i]++; cnt++;

		while(!q.empty()){
			int cur=q.front(); q.pop();

			for(int a=0;a<(int) v[cur].size();++a){
				int nxt=v[cur][a];
				if(visit[nxt]) continue;

				q.push(nxt); visit[nxt]++; cnt++;
				
				if(tmp_ans <= cnt) tmp_ans = cnt;
			}
		}
		ans[tmp_ans].push_back(i);
		max_ans = max(max_ans, tmp_ans);
	}

	for(int t : ans[max_ans]) cout << t+1 << ' ';
	return 0;
}
