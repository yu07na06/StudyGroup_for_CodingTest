#include <string>
#include <vector>
using namespace std;
int order[7] = {6, 6, 5, 4, 3, 2, 1};
vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int zero_cnt = 0, same_cnt = 0;

    for(auto l : lottos) {
        if(!l) zero_cnt++;
        
        for(auto w : win_nums) {
            if(l==w) same_cnt++;
        }
    }
    
    return {order[same_cnt+zero_cnt], order[same_cnt]};
}
