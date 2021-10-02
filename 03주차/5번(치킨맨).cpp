#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

unordered_map<string, int> umap;  // 0은 민호
int parent[10001];
int totalEarn[10001];
vector<int> answer;

void giveFee(int idx, int money) {
    if (parent[idx] == -1) {  // 민호면 돈 다 먹고 종료
        totalEarn[idx] = money;
        return;
    }

    int fee = money / 10;  // 19 * 10% = 1
    totalEarn[idx] += money - fee;

    giveFee(parent[idx], fee);
}

// enroll 1만, seller 10만
vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    int mNum = enroll.size();
    int selNum = seller.size();

    // 1. 트리 만들고
    parent[0] = -1;  // 민호는 부모없음
    for (int i = 0; i < mNum; ++i) {
        string mem = enroll[i];
        string refMem = referral[i];

        umap[mem] = i + 1;
        parent[i + 1] = umap[refMem];
    }

    // 2. 총 번 돈 읽으면서 부모에게 전달
    for (int i = 0; i < seller.size(); ++i) {
        string mem = seller[i];
        int sell = amount[i];

        giveFee(umap[mem], sell * 100);
    }

    // 3. 돈분배 결과 enroll 순서대로 answer배열에 담기
    for (int i = 0; i < mNum; ++i) {
        string mem = enroll[i];
        int earn = totalEarn[umap[mem]];
        answer.push_back(earn);
    }

    return answer;
}
