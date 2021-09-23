// 20210920 1300-1400
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;
int e,l,n;
unordered_set<int> se;

vector<int> solution(vector<int> enter, vector<int> leave) {
    n=enter.size();
    vector<int> ans(n);
    set<int> room[n+1];
    
    while(e!=n+1 && l!=n) {
        // for(int i : se) cout<<i<<", ";cout<<'\n';
        
        if(se.empty()) se.insert(enter[e++]);
        else {
            if(se.find(leave[l]) != se.end()) {

                for(int i : se) {
                    for(int j : se) {
                        if(i==j || room[i].find(j) != room[i].end()) continue;
                        room[i].insert(j);
                    }
                }
                
                // for(auto i=se.begin(); i!=se.end(); ++i) {
                //     for(auto j=i; j!=se.end(); ++j) {
                //         if(*i==*j) continue;
                //         room[*i].insert(*j);
                //         room[*j].insert(*i);
                //     }
                // }
                
                se.erase(leave[l++]);
            }
            else {
                se.insert(enter[e++]);
            }
        }
    }
    
    for(int i=1; i<=n; ++i) ans[i-1] = room[i].size();
    return ans;
}
