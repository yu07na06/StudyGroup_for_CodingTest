#include <iostream>
#include <vector>
#include <queue>
#include <math.h>
#define MAX 5001
#define F(i,m,n) for(int i=m;i<n;++i)
using namespace std;

struct P{
    int x,y; double r;
};

double cal_len(P p1, P p2){
    return sqrt(pow(p2.x-p1.x,2)+pow(p2.y-p1.y,2));
}

int main(){
    int t; cin>>t;
    while(t--){
        vector<int> map[MAX];
        vector<P> v; v.clear();
        int ans=0,n,x,y; double r; cin>>n;
        F(i,0,n) {
            cin>>x>>y>>r; v.push_back({x,y,r});
        }

        F(a,0,n-1) F(b,a+1,n){
            //cout << a << " : " << b << ", " << cal_len(v[a], v[b]) << ", " << v[a].r+v[b].r << '\n';
            if(cal_len(v[a], v[b]) <= v[a].r+v[b].r){
                //cout << "connect : " << a << " : " << b << '\n';
                map[a].push_back(b);
                map[b].push_back(a);
            }
        }

        int visit[MAX] {};
        F(i,0,n){
            if(visit[i]) continue;
            ans++;
            //cout << "visit : " << i << '\n';
            queue<int> q; while(!q.empty()) q.pop();
            visit[i]++; q.push(i);

            while(!q.empty()){
                int tq=q.front(); q.pop();

                F(nq,0,map[tq].size()){
                    if(visit[map[tq][nq]]) continue;
                    visit[map[tq][nq]]++; q.push(map[tq][nq]);
                    //cout << "\tpush : " << map[tq][nq]<< '\n';
                }
            }
        }

        cout << ans << '\n';
    }
    return 0;
}
