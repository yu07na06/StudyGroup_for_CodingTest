#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

vector<int> solution(vector<string> gems) {
    
    map<string, int> display;
    set<string> s(gems.begin(), gems.end());
    int max_cnt = s.size();
    vector<int> answer = {1, (int) gems.size()};
    
    if(max_cnt == gems.size())
        return answer;
    
    int max_ans_cnt = 0, min_ans_len = 1e9;
    int start = 0, end = 0, cnt = 0;
    
    while (start < gems.size()) {
        // cout << start << ", " << end << '\n';
        
        if (cnt == max_cnt) {
            // cout << "\tcnt == max_cnt" << '\n';
            if (min_ans_len > end - start) {
                answer[0] = start + 1, answer[1] = end;
                min_ans_len = end - start;
            }

            display[gems[start]]--;
            if (!display[gems[start++]]) cnt--;

            if (start == end) end++;
            
            // cout <<"\t\t display[gems[start]], start : " << display[gems[start-1]] << " : " << start << ", " << end << '\n';
        }
        else if (cnt < max_cnt) {
            // cout << "\tcnt < max_cnt" << '\n';
            if (end >= gems.size()) break;

            if (!display[gems[end]]) cnt++;
            display[gems[end++]]++;
            
            // cout <<"\t\t display[gems[end]], end : " << display[gems[end-1]] << " : " << start << ", " << end << '\n';
        }
    }

    return answer;
}
