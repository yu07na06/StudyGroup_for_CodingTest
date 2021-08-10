#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

vector<int> solution(vector<string> gems) {  // length 10만. 10만^2 = 100억
    vector<int> ans;

    unordered_set<string> uset;
    for (string& s : gems) {
        uset.insert(s);
    }

    int nType = uset.size();  // 보석 종류갯수
    int s = 0, e = 0, i = 0, range = 100000;
    unordered_map<string, int> umap;
    while (1) {
        for (i = e; i < gems.size(); ++i) {
            ++umap[gems[i]];
            if (umap.size() == nType) {
                e = i;
                break;
            }
        }

        if (i == gems.size()) break;

        for (i = s; i < gems.size(); ++i) {
            if (umap[gems[i]] == 1) {
                s = i;
                break;
            } else {
                --umap[gems[i]];
            }
        }

        if (e - s < range) {
            ans = {s + 1, e + 1};
            range = e - s;
        }

        umap.erase(gems[s]);
        ++s, ++e;
    }

    return ans;
}