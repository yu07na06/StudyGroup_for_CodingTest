//20210906 1400
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;
struct P {int x,y;};
int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

int n = 5;

bool check(int x, int y) {
    return !(x<0||y<0||x>=n||y>=n);
}
bool do_something_special(vector<string> place){
    //F(x,n) {F(y,n) {cout <<place[x][y]<<' ';}cout<<'\n';}cout<<'\n';
    F(x,n) F(y,n) if(place[x][y]=='P') {
        int visit[5][5]={};
        queue<P> q;
        q.push({x,y}); visit[x][y]++;

        //cout<<"START: "<<x<<", "<<y<<'\n';
        while(!q.empty()){
            int tx=q.front().x, ty=q.front().y; q.pop();

            //cout<<"\tGO: "<<tx<<", "<<ty<<'\n';
            F(a,4){
                int nx=tx+dx[a], ny=ty+dy[a];
                if(!check(nx,ny) || place[nx][ny]=='X' || visit[nx][ny]>=2) continue;

                // P >> P, OP
                if(visit[tx][ty] == 1) {
                    if(place[nx][ny]=='P') {
                        //cout<<"\t1 FIND: "<<nx<<", "<<ny<<'\n';
                        return false;
                    } else if(place[nx][ny] == 'O') {
                        q.push({nx,ny}); visit[nx][ny]+=visit[tx][ty]+1;
                    }
                } else if(visit[tx][ty] == 2 && visit[nx][ny] != 1) {
                    if(place[nx][ny]=='P') {
                        //cout<<"\t2 FIND: "<<nx<<", "<<ny<<'\n';
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> ans;
    
    for(auto place : places) {
        ans.push_back(do_something_special(place));
    }
    
    return ans;
}
