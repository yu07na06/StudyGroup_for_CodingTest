#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define ll long long

using namespace std;

vector<ll> num;
vector<char> op;
vector<char> opOrder;

ll operation(ll a, ll b, char o) {
    if(o == '*') return a*b;
    else if(o == '+') return a+b;
    else if(o == '-') return a-b;
}

ll solution(string expression) {
    ll answer = 0;
    
    int tmp = 0;
    set<char> opSet;
    for (auto c : expression){
        if ('0' <= c && c <= '9'){
            tmp *= 10;
            tmp += c - '0';
        } else {
            num.push_back(tmp);
            op.push_back(c);
            opSet.insert(c);
            tmp = 0;
        }
    }
    num.push_back(tmp);
    
    for (auto o : opSet) opOrder.push_back(o);
    
    do {
        ll res = 0;
        vector<ll> n(num);
        vector<char> o(op);
        for (int i = 0; i < opOrder.size(); ++i) {
            for (int j = 0; j < o.size(); ++j){
                if (opOrder[i] == o[j]) {
                    n[j+1] = operation(n[j], n[j+1], o[j]);
                    n.erase(n.begin() + j);
                    o.erase(o.begin() + j);
                    --j;
                }
            }
        }
        answer = max(answer, abs(n[0]));
    }while(next_permutation(opOrder.begin(), opOrder.end()));
    
    
    return answer;
}
