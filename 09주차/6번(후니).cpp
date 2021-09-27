#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#define MIN_VOWEL 1
#define MIN_CONSONANT 2
using namespace std;
int l,c;
string s[16];
vector<string> ans;
int main(){
    cin>>l>>c;
    for(int i=0;i<c;++i) cin>>s[i];
    sort(s, s+c);
    
    vector<int> v(c);
    for(int i=0;i<c-l;++i) v[v.size()-1 - i] = 1;
    
    do {
        int cnt_vowel = 0, cnt_consonant = 0;
        string docs = "";
        for(int i=0; i<v.size(); ++i) if(v[i]==0) {
            docs += s[i];
            
            if(s[i] == "a" || s[i] == "e" || s[i] == "i" || s[i] == "o" || s[i] == "u")
                cnt_vowel++;
            else
                cnt_consonant++;
        }
        
        if(cnt_vowel >= MIN_VOWEL && cnt_consonant >= MIN_CONSONANT)
            cout << docs << '\n';
        
    } while(next_permutation(v.begin(), v.end()));
    
    return 0;
}
