// 20210915 0015 - 0100
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <map>
using namespace std;

string solution(vector<string> table, vector<string> languages, vector<int> preference) {
    vector<string> tabl;
    unordered_map<string, int> um;
    vector<unordered_map<int, int>> v;
    
    string answer = "";
    
    string a;
    int score = 1;
    for(auto t : table) {
        unordered_map<int, int> m;
        stringstream ss(t);
        ss>>a;
        tabl.push_back(a);
        
        for(int i=5; i>=1; --i){
            ss>>a;
            if(!um[a]) um[a] = score++;
            m[um[a]]=i;
        }
        
        v.push_back(m);
    }
    
    int max_score = -1;
    int idx = 0;
    for(auto m : v) {
        score = 0;
        for(int i=0; i<languages.size(); ++i) {
            score += m[um[languages[i]]] * preference[i];
        }
        
        if(max_score < score) {
            max_score = score;
            answer = tabl[idx];
            
        } else if(max_score == score) {
            answer = min(answer, tabl[idx]);
        }
        
        idx++;
    }
        
    return answer;
}
