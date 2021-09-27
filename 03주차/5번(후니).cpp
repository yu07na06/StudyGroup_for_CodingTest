#include <string>
#include <vector>
#include <math.h>
#include <unordered_map>
#define F(i,n) for(int i=0;i<n;++i)
#define MAX 10001
using namespace std;

unordered_map<string, int> umap;
unordered_map<string, string> up;

void dfs_sell(string seller, int amount) {
    
    if(seller == "-" || amount == 0) return;

    // for(string next : up[seller]) {
    umap[up[seller]] += ceil(amount * 0.9);
    dfs_sell(up[seller], amount - ceil(amount * 0.9));
    // }
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {

    
    F(i, enroll.size()) {
        up[enroll[i]] = referral[i];
        
        umap[enroll[i]] = 0;
    }

    
    
    F(i, seller.size()) {
        amount[i] *= 100;
        umap[seller[i]] += ceil(amount[i] * 0.9);
        dfs_sell(seller[i], amount[i] - ceil(amount[i] * 0.9));
    }
    
    vector<int> answer;
    for(string s : enroll) answer.push_back(umap[s]);
    return answer;
}

/*
enroll      각 판매원의 이름을 담은 배열    
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"] len <= 10,000

referral    판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"] len <= 10,000

seller      판매량 집계 데이터의 판매원 이름을 나열한 배열
["young", "john", "tod", "emily", "mary"]   len <= 100,000

amount      판매량 집계 데이터의 판매 수량을 나열한 배열
[12, 4, 2, 5, 10]   amoun[n] <= 100

result      판매원이 득한 이익금을 나열한 배열
[360, 958, 108, 0, 450, 18, 180, 1080]
*/
