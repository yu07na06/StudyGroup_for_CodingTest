#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>
#define F(i,n) for(int i=0;i<n;++i)
#define MAX 51
using namespace std;
struct P {int x,y;};
int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

int n, m, map[MAX][MAX], vnum[11];
vector<P> can_virus;
vector<int> answers;

void print(int v[][MAX]) { F(x,n){F(y,n){if(v[x][y]>0)cout<<v[x][y]<<' '; else cout<<"- ";}cout<<'\n';}}
bool check(int x, int y) { return !(x<0||y<0||x>=n||y>=n); }

int map_tour(int v[][MAX]){
    int tmp = 0;
    F(x, n) F(y, n) {
        if(v[x][y] == 0 && map[x][y] == 0) return 1e9;
        else {
            if(map[x][y] == 2 && v[x][y] != 1) continue;
            tmp = max(tmp, v[x][y]);
        }
    }
    return tmp - 1;
}

int main(){
    cin>>n>>m;
    F(x,n) F(y,n) {
        cin>>map[x][y];
        if(map[x][y] == 2) can_virus.push_back({x, y});
    }
    F(i,m) vnum[can_virus.size()-1 - i]++;
    
    do {
        int visit[MAX][MAX] {}; queue<P> q;
        F(i, can_virus.size()) {
            if(!vnum[i]) continue;
            q.push({can_virus[i].x, can_virus[i].y});
            visit[can_virus[i].x][can_virus[i].y] = 1;
        }
        
        while(!q.empty()){
            int tx = q.front().x, ty = q.front().y;
            q.pop();
            
            F(a, 4){
                int nx=tx+dx[a], ny=ty+dy[a];
                if(!check(nx,ny) || visit[nx][ny] || map[nx][ny] == 1) continue;
                
                visit[nx][ny] = visit[tx][ty] + 1;
                q.push({nx, ny});
            }
        }
        
        int tmp_ans = map_tour(visit);
        answers.push_back(tmp_ans);
        
        // print(visit);
        // cout << tmp_ans << '\n';
        
    } while(next_permutation(vnum, vnum+can_virus.size()));
    
    sort(answers.begin(), answers.end());
    
    // cout << '\n';
    // for(int a : answers) cout<<a<<" "; cout<<'\n';
    
    answers.front() == 1e9 ? 
        cout << -1 : cout<<answers.front();
	return 0;
}