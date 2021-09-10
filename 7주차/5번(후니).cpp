//20210909 1050-1110
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

int solution(string s) {
    // 숫자를 1 늘려줘서 zero가 0이 되지않게 만듬
    unordered_map<string, int> umap = {{"zero",1},{"one",2},{"two",3},{"three",4},{"four",5},{"five",6},{"six",7},{"seven",8},{"eight",9},{"nine",10}};
    string ans = "", tmp = "";
    
    for(int i=0; i<s.size(); ++i) {
        tmp += s[i];
        
        if(isdigit(s[i])){
            ans += s[i];
            tmp = "";
        }
        else if(umap[tmp]) {
            ans += to_string(umap[tmp]-1);
            tmp = "";
        }         
    }
    return stoi(ans);
}
