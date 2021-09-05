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

int n, map[MAX][MAX];
void print(){
    F(x,n){F(y,n){cout<<map[x][y]<<" ";}cout<<'\n';}cout<<'\n';
}
bool check(int x, int y) {
    return !(x<0||y<0||x>=n||y>=n);
}
int[][] move(int way, int map[][MAX]) {
    if(way==0) {
        F(x,n) F(y,n)
    } else if(way==1) {

    } else if(way==2) {
        
    } else {
        
    }
}

void dfs(int way, int cnt, int map[][MAX]) {
    if(cnt==5){
        int max_num=0;
        F(x,n)F(y,n) max_num=max(max_num, map[x][y]);
        return;
    }

    int c_map[MAX][MAX]{};
    move(a, map[x][y]);

    F(a,4){
        dfs(a, cnt+1, map[x][y]);
    }
}
int main(){
    cin>>n; F(x,n)F(y,n)cin>>map[x][y];

    queue<P> q;

    F(a,4){
        dfs(a, 0, map[x][y]);
    }
    return 0;
}