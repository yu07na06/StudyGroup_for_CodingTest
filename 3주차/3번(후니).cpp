// ref : https://yabmoons.tistory.com/621
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;

vector<string> split(string input, char delimiter) {
    vector<string> answer;
    stringstream ss(input);
    string temp;
 
    while (getline(ss, temp, delimiter)) {
        answer.push_back(temp);
    }
 
    return answer;
}

vector<int> info_vec[4][3][3][3];
map<string, int> m;

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    
    m["-"]=0;
    m["cpp"]=1, m["java"]=2, m["python"]=3;
    m["backend"]=1, m["frontend"]=2;
    m["junior"]=1, m["senior"]=2;
    m["chicken"]=1, m["pizza"]=2;
    
    for(string inf : info) {
        vector<string> in = split(inf, ' ');    // java, backend, junior, pizza, 150
        info_vec[m[in[0]]][m[in[1]]][m[in[2]]][m[in[3]]].push_back(stoi(in[4]));
        // cout << in[0] << ", " << in[1] << ", " << in[2] << ", " << in[3] << ", " << in[4] << '\n';
        // cout << m[in[0]] << ", " << m[in[1]] << ", " << m[in[2]] << ", " << m[in[3]] << ", " << in[4] << "\n";
        
        info_vec[0][m[in[1]]][m[in[2]]][m[in[3]]].push_back(stoi(in[4]));
        info_vec[m[in[0]]][0][m[in[2]]][m[in[3]]].push_back(stoi(in[4]));
        info_vec[m[in[0]]][m[in[1]]][0][m[in[3]]].push_back(stoi(in[4]));
        info_vec[m[in[0]]][m[in[1]]][m[in[2]]][0].push_back(stoi(in[4]));
        info_vec[0][0][m[in[2]]][m[in[3]]].push_back(stoi(in[4]));
        info_vec[0][m[in[1]]][0][m[in[3]]].push_back(stoi(in[4]));
        info_vec[0][m[in[1]]][m[in[2]]][0].push_back(stoi(in[4]));
        info_vec[m[in[0]]][0][0][m[in[3]]].push_back(stoi(in[4]));
        info_vec[m[in[0]]][0][m[in[2]]][0].push_back(stoi(in[4]));
        info_vec[m[in[0]]][m[in[1]]][0][0].push_back(stoi(in[4]));
        info_vec[0][0][0][m[in[3]]].push_back(stoi(in[4]));
        info_vec[0][0][m[in[2]]][0].push_back(stoi(in[4]));
        info_vec[0][m[in[1]]][0][0].push_back(stoi(in[4]));
        info_vec[m[in[0]]][0][0][0].push_back(stoi(in[4]));
        info_vec[0][0][0][0].push_back(stoi(in[4]));
    }
    
    F(a,4) F(b,3) F(c,3) F(d,3) 
        sort(info_vec[a][b][c][d].begin(), info_vec[a][b][c][d].end());

    
    
    for(string quer : query) {
        vector<string> que = split(quer, ' ');  // -, and, -, and, -, and, -, 150, 
        vector<int> query_vec = info_vec[m[que[0]]][m[que[2]]][m[que[4]]][m[que[6]]];
        
        int min_score_idx = lower_bound(query_vec.begin(), query_vec.end(), stoi(que[7])) - query_vec.begin();
        
        answer.push_back(query_vec.size() - min_score_idx);
    }
    
    return answer;
}
