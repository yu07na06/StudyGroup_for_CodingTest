#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

string solution(int n, int k, vector<string> cmd) {
    string answer = "";
    for (int i = 0; i < n; ++i) {
        answer += 'X';
    }

    stack<int> removed;
    set<int> rowset;
    for (int i = 0; i < n; ++i) {
        rowset.insert(i);
    }

    auto kIt = rowset.find(k);

    for (string& s : cmd) {
        stringstream ss(s);
        char action;
        int x;
        ss >> action >> x;

        if (action == 'U') {
            while (x--) {
                kIt = prev(kIt);
            }
        } else if (action == 'D') {
            while (x--) {
                kIt = next(kIt);
            }
        } else if (action == 'C') {
            removed.push(*kIt);

            kIt = rowset.erase(kIt);
            if (kIt == rowset.end()) {
                kIt = prev(kIt);
            }
        } else if (action == 'Z') {
            rowset.insert(removed.top());
            removed.pop();
        }
    }

    for (int n : rowset) {
        answer[n] = 'O';
    }

    return answer;
}
