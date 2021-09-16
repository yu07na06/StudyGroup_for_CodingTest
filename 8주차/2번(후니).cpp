#include <string>
#include <vector>
#include <cmath>

using namespace std;
string solution(vector<vector<int>> scores) {
    string ans = "";
    for(int x=0; x<scores.size(); ++x) {
        int max_num = -1, min_num = 1e9;
        int max_cnt = 0, min_cnt = 0;
        int cnt = scores[x].size();
        
        double sum = 0;
        for(int xx=0; xx<scores.size(); ++xx) {
            if(max_num < scores[xx][x])          max_cnt = 1, max_num = scores[xx][x];
            else if (max_num == scores[xx][x])   max_cnt++;
            
            if(min_num > scores[xx][x])          min_cnt = 1, min_num = scores[xx][x];
            else if (min_num == scores[xx][x])   min_cnt++;
            
            sum += scores[xx][x];
        }
        
        if((scores[x][x] == max_num && max_cnt==1) || (scores[x][x] == min_num && min_cnt==1)) {
            sum -= scores[x][x];
            cnt--;
        }
        
        sum = sum / cnt;
        if(!cnt) sum = 0;
        
        if(sum >= 90)       ans += "A";
        else if(sum >= 80)  ans += "B";
        else if(sum >= 70)  ans += "C";
        else if(sum >= 50)  ans += "D";
        else                ans += "F";
    }
    
    return ans;
}
