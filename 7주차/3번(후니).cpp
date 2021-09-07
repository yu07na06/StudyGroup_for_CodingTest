#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
set<int> foo;
vector<int> trash;
string c;
int num;
string solution(int n, int k, vector<string> cmd) {
    for(int i=0; i<n; ++i) foo.insert(i);
    auto idx = foo.find(k);
    
    for(string s : cmd) {
        stringstream ss(s);
        ss >> c >> num;
        // cout << s << '\n';
        
        if(c == "D") {
            while(num--) idx++;
        } else if(c == "U") {
            while(num--) idx--;
        } else if(c == "C") {
            trash.push_back(*idx);
            idx = foo.erase(idx);
            if(idx == foo.end()) idx--;
        } else if(c == "Z") {
            foo.insert(trash.back());
            trash.pop_back();
        }
        // for(int i : foo) cout << i << ' '; cout << '\n';
        // cout<<*idx<<"\n\n";
    }
    string ans(n, 'X');
    for(int i : foo) ans[i] = 'O';
    return ans;
}

/*
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
struct P { int idx, num; };
vector<int> foo;
vector<P> trash;
string c;
int num;

string solution(int n, int k, vector<string> cmd) {
    for(int i=0; i<n; ++i) foo.push_back(i);
    auto idx = foo.begin() + k;
    
    for(string s : cmd) {
        stringstream ss(s);
        ss >> c >> num;
        
        if(c == "D") {
            idx += num;
        } 
        else if(c == "U") {
            idx -= num;
        } 
        else if(c == "C") {
            int cur_idx = lower_bound(foo.begin(), foo.end(), *idx) - foo.begin();
            // cout << "\tcur_idx : " << cur_idx << '\n';
            trash.push_back({cur_idx, *idx});
            
            if(*(idx+1) == trash.back().num){
                foo.erase(idx);
                idx--;
            } 
            else foo.erase(idx);
            
            
            // cout <<"\ttrash.size() : " << trash.size() << '\n';
        } 
        else if(c == "Z") {
            // cout << "\tretreive : " << trash.back().num << '\n';
            foo.insert(foo.begin() + trash.back().idx - 1, trash.back().num );
            if(trash.back().num < *idx) idx++;
                
            trash.pop_back();
            // cout <<"\ttrash.size() : " << trash.size() << '\n';
        }
        // cout << *idx << '\n';
    }
    
    string ans(n, 'X');
    for(int i=0; i<foo.size(); ++i) ans[foo[i]] = 'O';
    
    return ans;
}
*/
