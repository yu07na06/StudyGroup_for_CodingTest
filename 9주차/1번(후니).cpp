// 20210920 1200-1215
#include <iostream>
#include <string>
using namespace std;
int ans, done;
string alphabet[5]={"A","E","I","O","U"};
void dfs(string str, string word) {
    // cout<< ans << " : " << str<< '\n';
    if(str == word) {
        done++;
        return;
    }
    if(str.size() == 5) return;
    
    for(int i=0; i<5; ++i) {
        if(done) return;
        ans++;
        dfs(str+alphabet[i], word);
    }
    
}
int solution(string word) {
    dfs("", word);
    return ans;
}
