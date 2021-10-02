#include <string>
#include <vector>
#include <iostream>

using namespace std;
 
int solution(string s) {
    int ans = s.size();
    
    if(s.size() == 1) return 1;
    
    for(int len = 1 ; len <= s.size() / 2 ; ++len) {
        vector<string> v;
        int idx = 0;
        while(idx < s.size()) v.push_back(s.substr(idx, len)), idx += len;
        
        int prev_found = 1;
        string tmp_ans = "", prev = v[0];
        
        for(int i = 1 ; i < v.size(); ++i) {
            
            if(prev == v[i]) {
                
                if(i == v.size() - 1)   tmp_ans += to_string(prev_found) + v[i];
                
                prev_found++;
                
            } else if (prev != v[i]) {

                if(i == v.size() - 1) {
                    if(prev_found > 1)  tmp_ans += to_string(prev_found) + prev + v[i];
                    else                tmp_ans += prev + v[i];
                }
                else {
                    if(prev_found > 1)  tmp_ans += to_string(prev_found) + prev;
                    else                tmp_ans += prev;
                }
                prev_found = 1;
            }
            prev = v[i];
        }
        if(tmp_ans != "") ans = min(ans, (int) tmp_ans.size());
    }

    return ans;
}

/*
int solution(string s) {
    int ans = s.size();
    
    if(s.size() == 1) return 1;
    
    for(int len = 1 ; len <= s.size() / 2 ; ++len) {
        vector<string> v;
        int idx = 0;
        while(idx < s.size()) {
            v.push_back(s.substr(idx, len)), idx += len;
        }
        
        int prev_found = 1;
        string tmp_ans = "", prev = v[0];
        
        //cout << "LEN : " << len << '\n';
        for(int i = 1 ; i < v.size(); ++i) {
            //cout << "\t" + prev << ", " << v[i] << " : ";
            
            if(prev == v[i]) {
                //cout << "SAME, ";
                
                // 마지막 비교
                if(i == v.size() - 1) {
                    //cout << "LAST, ";
                    tmp_ans += to_string(prev_found) + v[i];
                }
                // 마지막 비교가 아니면
                else {
                    //cout << "NOT LAST ";
                }
                
                prev_found++;
                
            } else if (prev != v[i]) {
                //cout << "DIFF, ";
                
                // 마지막 비교
                if(i == v.size() - 1) {
                     //cout << "LAST, ";

                    // 이전에 압축 했으면
                    if(prev_found > 1) {
                        //cout << "FOUND, ";
                        tmp_ans += to_string(prev_found) + prev + v[i];
                    }
                    // 이전에 압축 못했으면
                    else {
                        //cout << "NO FOUND, ";
                        tmp_ans += prev + v[i];
                    }
                }
                // 마지막 비교가 아니면
                else {
                    //cout << "NOT LAST ";
                    
                    // 이전에 압축 했으면
                    if(prev_found > 1) {
                        //cout << "FOUND, ";
                        tmp_ans += to_string(prev_found) + prev;
                    }
                    // 이전에 압축 못했으면
                    else {
                        //cout << "NO FOUND, ";
                        tmp_ans += prev;
                    }
                }
                
                prev_found = 1;
            }
            //cout << " , " << temp_ans << '\n';
            prev = v[i];
        }
        if(tmp_ans != "") ans = min(ans, (int) tmp_ans.size());
    }

    return ans;
}
*/