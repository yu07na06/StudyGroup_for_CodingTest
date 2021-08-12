#include <algorithm>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

unordered_map<string, int> umap = {
    {"-", 0},
    {"cpp", 1},
    {"java", 2},
    {"python", 3},
    {"backend", 1},
    {"frontend", 2},
    {"junior", 1},
    {"senior", 2},
    {"chicken", 1},
    {"pizza", 2}};
vector<int> parsedInfo[4][3][3][3];

vector<int> solution(vector<string> info, vector<string> query) {
    for (string& s : info) {
        stringstream ss(s);
        string lang, pos, exp, food;
        int point;
        ss >> lang >> pos >> exp >> food >> point;
        int arr[4] = {umap[lang], umap[pos], umap[exp], umap[food]};

        for (int i = 0; i < (1 << 4); ++i) {
            vector<int> idx(4);
            for (int j = 0; j < 4; ++j) {
                if (i & (1 << j)) {
                    idx[j] = arr[j];
                }
            }
            auto& target = parsedInfo[idx[0]][idx[1]][idx[2]][idx[3]];
            target.push_back(point);
        }
    }

    for (int lang = 0; lang < 4; ++lang) {
        for (int pos = 0; pos < 3; ++pos) {
            for (int exp = 0; exp < 3; ++exp) {
                for (int food = 0; food < 3; ++food) {
                    auto& target = parsedInfo[lang][pos][exp][food];
                    sort(target.begin(), target.end());
                }
            }
        }
    }

    vector<int> answer;
    for (string& q : query) {
        stringstream ss(q);
        string lang, pos, exp, food, etc;
        int point;
        ss >> lang >> etc >> pos >> etc >> exp >> etc >> food >> point;

        auto target = parsedInfo[umap[lang]][umap[pos]][umap[exp]][umap[food]];
        auto it = lower_bound(target.begin(), target.end(), point);  // point와 같거나 큰 index
        answer.push_back(target.end() - it);
    }

    return answer;
}
