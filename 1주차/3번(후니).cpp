#include <iostream>
#include <vector>
#include <queue>
#define MAX 201
using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int ans = 0;
    int visit[MAX] {};
    
    for(int start = 0 ; start < n ; ++start) {
        if(visit[start]) continue;
        
        //cout << "START : " << start << '\n';
        
        queue<int> q;
        visit[start] = ++ans;
        q.push(start);

        while(!q.empty()) {
            int curr = q.front();
            q.pop();

            //cout << "\tVISIT : " << curr << '\n';
            
            for(int next = 0 ; next < n ; ++next) {
                int num = computers[curr][next];

                if(!num || curr == next || visit[next]) continue;

                visit[next] = visit[curr];
                q.push(next);
            }
        }
    }
    
    return ans;
}
