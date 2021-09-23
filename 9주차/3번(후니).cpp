#include <string>
#include <algorithm>
#include <vector>
using namespace std;
struct B { double win_rate, heavier_win; int w, idx; };
int n;

vector<int> solution(vector<int> weights, vector<string> head2head) {
    n = weights.size();
    
    vector<double> win_rate(n), heavier_win(n);
    double cnt, win_cnt, heavier_win_cnt;
    
    for(int head = 0; head < n; ++head) {
        cnt = 0, win_cnt = 0, heavier_win_cnt = 0;
        
        for(int i = 0 ; i < n; ++i) {
            if(head2head[head][i]=='N') continue;
            cnt++;
        
            if(head2head[head][i]=='W') {
                win_cnt++;
                
                if(weights[head] < weights[i]) {
                    heavier_win_cnt++;
                }
            }
        }
        
        if(cnt) {
            win_rate[head]=win_cnt/cnt;
            heavier_win[head]=heavier_win_cnt;
        }
    }
    
    vector<B> v;
    for(int i = 0 ; i < n; ++i) {
        v.push_back({win_rate[i], heavier_win[i], weights[i], i+1});
    }

    sort(v.begin(), v.end(), 
        [](B a, B b) {
            if(a.win_rate == b.win_rate && a.heavier_win == b.heavier_win && a.w == b.w) {
                return a.idx < b.idx;
            } else if(a.win_rate == b.win_rate && a.heavier_win == b.heavier_win) {
                return a.w > b.w;
            } else if(a.win_rate == b.win_rate) {
                return a.heavier_win > b.heavier_win;
            } else {
                return a.win_rate > b.win_rate;
            }
        }
    );

    vector<int> answer;
    for(int i = 0 ; i < n; ++i) {
        answer.push_back(v[i].idx);
    }
    
    // for(int i = 0 ; i < n; ++i) {
    //     cout<<v[i].win_rate<<", "<<v[i].heavier_wine<<", "<<v[i].w<<", "<<v[i].idx<<'\n';;
    // }cout<<'\n';
    
    return answer;
}
