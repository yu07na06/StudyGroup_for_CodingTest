#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

// 가로 x, 세로 y
// 첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
// a,x 가로선 (점선), b,y 세로선과 b+1 세로선
int n, m, h, a, b, ans, done, ori_map[31][31];

void print(int map[][31]) {
    for(int x=0; x<h; ++x){
        for(int y=0; y<n; ++y){
            cout << map[x][y] << " ";
        }cout << '\n';
    }cout << '\n';
}

bool check(int map[][31]) {
    for(int y=0; y<n; ++y){
        int ty = y;
        for(int x=0; x<h; ++x){
            if(map[x][ty] == 0) continue;
            
            if(map[x][ty] % 2 == 1) ++ty;
            else if(map[x][ty] % 2 == 0) --ty;
        }
        if(y != ty) return false;
    }
    return true;
}

void dfs(int map[][31], int cnt, int max_cnt) {
    if(cnt == max_cnt) {
        if(check(map)) {
            ans = max_cnt;
            done = true;
            return; 
        }
        else return;
    }

    // 모든 세로선 방문 후 사다리 가로선 추가하기
    for(int y=0; y<n-1; ++y){
        for(int x=0; x<h; ++x){
            if(map[x][y] || map[x][y+1] || done) continue;
            
            map[x][y] = 3;
            map[x][y+1] = 4;
            
            dfs(map, cnt+1, max_cnt);
            
            map[x][y] = 0;
            map[x][y+1] = 0;
        }
    }
}

int main() {
    cin>>n>>m>>h;
    if(m == 0) {
        cout << 0;
        return 0;
    }
    for(int i=0; i<m; ++i){
        cin>>a>>b; a--, b--;
        ori_map[a][b] = 1;
        ori_map[a][b+1] = 2;
    }

    if(check(ori_map)){
        cout << 0;
        return 0;
    }
    // print(ori_map);

    for(int max_cnt=1; max_cnt<=3; ++max_cnt) {
        
        dfs(ori_map, 0, max_cnt);
        if(done) {
            cout << ans;
            return 0;
        }
    }

    cout << -1;
    return 0;
}
