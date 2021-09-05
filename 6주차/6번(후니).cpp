#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define F(i,n) for(int i=0;i<n;++i)
#define MAX 21
using namespace std;
struct P {int x,y;};
int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

int ans, n, m[MAX][MAX], c_map[MAX][MAX];
void print(int map[][MAX]){
    F(x,n){F(y,n){cout<<map[x][y]<<" ";}cout<<'\n';}cout<<'\n';
}
bool check(int x, int y) {
    return !(x<0||y<0||x>=n||y>=n);
}
void move(int way, int map[][MAX]) {
    //cout<<"MOVE : " << way << '\n';
    //print();

    int tx, ty, nx, ny;
    if(way==0) {
        F(y,n){
            tx=0, nx=1;
            // cout << "\tSTART : " << y << '\n';
            while(check(nx, y)){
                // cout << "\tCHECK : " << nx << '\n';
                if(!map[tx][y]) {           // 0, 2 >> 2, 0
                    if(map[nx][y]){
                        // cout << "\tthis\n";
                        map[tx][y] = map[nx][y];
                        map[nx][y] = 0;
                    }
                }
                else if(map[tx][y]){        // 2, 2 >> 4, 0
                    if(map[tx][y] == map[nx][y]){
                        // cout << "\tthat\n";
                        map[tx][y] += map[nx][y];
                        map[nx][y] = 0;
                    } else {                // 2, 4 >> 2, 4
                        // cout << "\tthose\n";
                        tx++;
                        if(!map[tx][y] && map[nx][y]){           // 2, 0, 4 >> 2, 4, 0
                            // cout << "\tsuper those\n";
                            map[tx][y] = map[nx][y];
                            map[nx][y] = 0;
                        }
                    }
                }
                nx++;
            }
        }
    } else if(way==1) {
        F(x,n){
            ty=n-1, ny=n-2;
            while(check(x, ny)){
                if(!map[x][ty]) {           // 0, 2 >> 2, 0
                    if(map[x][ny]){
                        map[x][ty] = map[x][ny];
                        map[x][ny] = 0;
                    }
                }
                else if(map[x][ty]){        // 2, 2 >> 4, 0
                    if(map[x][ty] == map[x][ny]){
                        map[x][ty] += map[x][ny];
                        map[x][ny] = 0;
                    } else {                // 2, 4 >> 2, 4
                        ty--;
                        if(!map[x][ty] && map[x][ny]){           // 2, 0, 4 >> 2, 4, 0
                            map[x][ty] = map[x][ny];
                            map[x][ny] = 0;
                        }
                    }
                }
                ny--;
            }
        }
    } else if(way==2) {
        F(y,n){
            tx=n-1, nx=n-2;
            while(check(nx, y)){
                if(!map[tx][y]) {           // 0, 2 >> 2, 0
                    if(map[nx][y]){
                        map[tx][y] = map[nx][y];
                        map[nx][y] = 0;
                    }
                }
                else if(map[tx][y]){        // 2, 2 >> 4, 0
                    if(map[tx][y] == map[nx][y]){
                        map[tx][y] += map[nx][y];
                        map[nx][y] = 0;
                    } else {                // 2, 4 >> 2, 4
                        tx--;
                        if(!map[tx][y] && map[nx][y]){           // 2, 0, 4 >> 2, 4, 0
                            map[tx][y] = map[nx][y];
                            map[nx][y] = 0;
                        }
                    }
                }
                nx--;
            }
        }
    } else {
        F(x,n){
            ty=0, ny=1;
            while(check(x, ny)){
                if(!map[x][ty]) {           // 0, 2 >> 2, 0
                    if(map[x][ny]){
                        map[x][ty] = map[x][ny];
                        map[x][ny] = 0;
                    }
                }
                else if(map[x][ty]){        // 2, 2 >> 4, 0
                    if(map[x][ty] == map[x][ny]){
                        map[x][ty] += map[x][ny];
                        map[x][ny] = 0;
                    } else {                // 2, 4 >> 2, 4
                        ty++;
                        if(!map[x][ty] && map[x][ny]){           // 2, 0, 4 >> 2, 4, 0
                            map[x][ty] = map[x][ny];
                            map[x][ny] = 0;
                        }
                    }
                }
                ny++;
            }
        }
    }
    // memset(c_map, 0, sizeof(c_map));
    // memcpy(c_map, map, sizeof(c_map));
}

void dfs(int way, int cnt, int map[][MAX]) {
    if(cnt==5){
        F(x,n)F(y,n) ans=max(ans, map[x][y]);
        // if(ans == 128) {
        // cout << "DONE : " << ans << '\n';
        // print(map);
        // }
        return;
    }
    
    int c_map[MAX][MAX] {};
    memcpy(c_map, map, sizeof(c_map));
    move(way, c_map);

    F(a,4){
        // cout << "\ta, cnt : " << a << ", " << cnt+1 << '\n';
        dfs(a, cnt+1, c_map);
    }
}
int main(){
    cin>>n; F(x,n)F(y,n)cin>>m[x][y];

    F(a,4) {
        dfs(a, 0, m);
    }

    cout<<ans;
    // cout<<'\n';print(m);
    return 0;
}