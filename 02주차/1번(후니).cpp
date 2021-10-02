#include <iostream>
#include <string>
#include <vector>
#include <queue>
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;

int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};
struct P {
    int x, y;
};

bool check(int x, int y) {
    return !(x < 0 || y < 0 || x >= 5 || y >= 5);
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    F(t, places.size()) {
        //cout << "ST : " << t << '\n';
        bool is_virus = false;
        
        F(x, 5) F(y, 5) if(places[t][x][y] == 'P') { 
            //cout << "ART : " << x << ", " << y << '\n';
            int visit[6][6] {};
            queue<P> q;
            
            visit[x][y] = 1;
            q.push({x, y});
            
            while(!q.empty()){
                int tx = q.front().x, ty = q.front().y; q.pop();
                //cout << "\tSEARCH : " << tx << ", " << ty << '\n';
                
                for(int a = 0 ; a < 4 ; ++a) {
                    int nx = tx + dx[a], ny = ty + dy[a];
                    
                    if(!check(nx, ny) || visit[nx][ny]) continue;
                    if(places[t][nx][ny] == 'X') continue;
                    
                    visit[nx][ny] = visit[tx][ty] + 1;
                    
                    if(places[t][nx][ny] == 'P' && 1 < visit[nx][ny] && visit[nx][ny] <= 3)
                        is_virus = true;
                    
                    q.push({nx, ny});
                }                
            }
        }
            
        is_virus == true ? answer.push_back(0) : answer.push_back(1);
    }
    
    return answer;
}

/*
OXXXO
OOOXO
XXXXP
OXPXX
POOPX
*
*PX
*OP
*/
