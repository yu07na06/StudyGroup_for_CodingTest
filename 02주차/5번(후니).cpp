#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define F(i,n) for(int i=0;i<n;++i)
using namespace std;

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> ans;
    
    for(string query : queries) {
        /*
        int tmp_ans=0;
        auto first = query.find("?");
        auto last = query.find_last_of("?");
        for(string word : words) {
            
            //cout << "\tchk : "<<word<<'\n';
            if(word.length() != query.length()) continue;
            
            if(first == 0 && last == query.length()-1) { // ? , ?????
                tmp_ans++;
            
            } else if(last == query.length()-1) { // aa???
                if(word.substr(0, first) == query.substr(0, first))
                    tmp_ans++;
                //cout << "\t\tfront word : " << word.substr(0, first) <<'\n';
                
            } else if(first == 0) { // ???aa
                if(word.substr(last+1) == query.substr(last+1))
                    tmp_ans++;
                //cout << "\t\tback word : " << word.substr(last+1) <<'\n';
            
            }
        }
        */
        
        
        int tmp_ans = 0;
        auto first = lower_bound(query.begin(), query.end(), '?',
                                 [](auto a, auto b) {
                                     return a != '?' && b == '?';
                                 }) - query.begin();
        
        auto last = upper_bound(query.begin(), query.end(), '?',
                                 [](auto a, auto b) {
                                     return a == '?' && b != '?';
                                 }) - query.begin();
        
        //cout << first - query.begin() << ", " << last - query.begin() <<'\n';
        //cout << first << ", " << last <<'\n';
     
        
        for(string word : words) {
            
            //cout << "\tchk : "<<word<<'\n';
            if(word.length() != query.length()) continue;
            
            if(*query.begin() == '?' && *(query.end()-1) == '?') { // ? , ?????
                tmp_ans++;

            } else if(first > 0) { // aa???
                if(word.substr(0, first) == query.substr(0, first))
                    tmp_ans++;
                //cout << "\t\tfront word : " << word.substr(0, first) <<'\n';

            } else if(last > 0) { // ???aa
                if(word.substr(last) == query.substr(last))
                    tmp_ans++;
                //cout << "\t\tback word : " << word.substr(last) <<'\n';

            }
        }
        
        ans.push_back(tmp_ans);
    }
    
    return ans;
}
