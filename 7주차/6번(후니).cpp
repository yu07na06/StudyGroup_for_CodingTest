#include <string>
#include <vector>
#include <queue>
#include <iostream>
#define MAX 26
#define F(i,n) for(int i=0;i<n;++i)
struct P { int x,y,w; };
using namespace std;
int n,ans;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0}; 

void print(int v[MAX][MAX][4]){
    F(x,n){F(y,n){cout<<v[x][y][0]/100<<' ';}cout<<'\n';}cout<<'\n';
    F(x,n){F(y,n){cout<<v[x][y][1]/100<<' ';}cout<<'\n';}cout<<'\n';
    // F(x,n){F(y,n){cout<<v[x][y][2]/100<<' ';}cout<<'\n';}cout<<'\n';
    // F(x,n){F(y,n){cout<<v[x][y][3]/100<<' ';}cout<<'\n';}cout<<'\n';
}
bool check(int x, int y) {
    return !(x<0||y<0||x>=n||y>=n);
}
int solution(vector<vector<int>> board) {
    n = board.size();
    ans = 1e9;
    
    queue<P> q; int visit[MAX][MAX][4] = {};
    q.push({0,0,0}); q.push({0,0,1}); visit[0][0][0] = 0; visit[0][0][1] = 0;
    
    while(!q.empty()) {
        int tx=q.front().x, ty=q.front().y, tw=q.front().w; q.pop();
        //cout << tx << ", " << ty << ", " << tw << ", " << " :: " << visit[tx][ty][tw]<<'\n'; 
        
        F(a,4) {
            int nx=tx+dx[a], ny=ty+dy[a], nw = a, np = visit[tx][ty][tw] + 100;
            if(tw != nw) np += 500;
            
            if(!check(nx,ny) || board[nx][ny] || (visit[nx][ny][nw] && np > visit[nx][ny][nw])) continue;
            if(nx == n-1 && ny == n-1) {
                ans = min(ans, np);
                continue;
            }
            
            //cout << "\t" << nx << ", " << ny << ", " << nw << ", " << np << " :: " << visit[nx][ny]<<'\n'; 
            q.push({nx, ny, nw}); visit[nx][ny][nw] = np;
            //print(visit);
        }
    }
    return ans;
}
