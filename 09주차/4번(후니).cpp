#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#define MAX 101
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;
struct P { int x,y,z; };
int dx[]={-1,0,1,0,0,0};
int dy[]={0,1,0,-1,0,0};
int dz[]={0,0,0,0,1,-1};
int m,n,h,ans,map[MAX][MAX][MAX];
queue<P> q;

bool check(int x, int y, int z) {
    return !(x<0||y<0||z<0||x>=n||y>=m|z>=h);
}
int main(){
    cin>>m>>n>>h;
    F(z,h)F(x,n)F(y,m) {
        cin>>map[x][y][z];
        if(map[x][y][z] == 1) q.push({x,y,z});
    }
    
    while(!q.empty()){
        ++ans;
        int qsize = q.size();
        
        while(qsize--) {
            const auto [tx, ty, tz] = q.front(); q.pop();
            F(a, 6) {
                int nx=tx+dx[a], ny=ty+dy[a], nz=tz+dz[a];
                if(!check(nx,ny,nz) || map[nx][ny][nz] != 0) continue;
                q.push({nx,ny,nz});
                map[nx][ny][nz] = 1;
            }
        }
    }
    
    F(z,h)F(x,n)F(y,m) {
        if(map[x][y][z] == 0) {
            cout<<-1;
            return 0;
        }
    }
    cout<<ans-1;
    return 0;
}
