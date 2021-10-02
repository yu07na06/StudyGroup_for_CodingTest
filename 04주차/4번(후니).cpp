#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
using ll = long long;
char order[3] = {'*', '+', '-'};
vector<ll> num, num_original;
vector<char> op, op_original;

ll cal(ll n, char c, ll nn) { 
//     if('*' == order[0]) cout << "**************\n";
//     if('+' == order[1]) cout << "++++++++++++++\n";
//     if('-' == order[2]) cout << "--------------\n";
    
//     if(c == order[0]) return n*nn;
//     else if(c == order[1]) return n+nn;
//     else if(c == order[2]) return n-nn;
        
    if(c == '*') return n*nn;
    else if(c == '+') return n+nn;
    else if(c == '-') return n-nn;
}

long long solution(string expression) {
    long long answer = 0;
    
    // parse
    string tmp="";
    int idx = 0;
    for(char s : expression) {
        idx++;
        if('0' <= s && s <= '9'){
            tmp+=s;
            if(idx == expression.size()){
                num_original.push_back(stoi(tmp));
            }
        }
        else {
            num_original.push_back(stoi(tmp));
            op_original.push_back(s);
            
            tmp = "";
        }
    }
    //for(ll s : num_original) cout << s << ", "; cout << '\n';
    //for(char s : op_original) cout << s << ", "; cout << "\n\n";
    
    // combination
    do {
        int num_used[100] {}, op_used[100] {};
        vector<ll> num(num_original);
        vector<char> op(op_original);
        
        ll sum = 0;
        
        // expression 3번 순회
        for(int i = 0 ; i < 3; ++i) {
            
            for(int n = 0; n < num.size()-1 ; ++n) {
                if(op[n] != order[i]) continue;

                num[n+1] = cal(num[n], op[n], num[n+1]);
                
                num.erase(num.begin() + n);
                op.erase(op.begin() + n);
                n--;
            }
        }
        answer = max(answer, abs(num.front()));
    } while(next_permutation(order, order+3));
    
    return answer;
}
