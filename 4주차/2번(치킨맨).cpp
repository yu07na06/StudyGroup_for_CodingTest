#include <algorithm>
#define INF 987654321
using namespace std;

int solution(int n, vector<int> weak, vector<int> dist) {
    int ans = INF;
    int wLen = weak.size();
    int dLen = dist.size();

    weak.resize(wLen * 2);
    for (int i = wLen; i < 2 * wLen; ++i) {
        weak[i] = n + weak[i - wLen];
    }  // [1,5,6,10, 13,17,18,22] 여기서 4개 점검하면 됨

    sort(dist.begin(), dist.end());
    do {  // dist: 1234, 1243, 1324, 1342...
        for (int i = 0; i < wLen; ++i) {
            int s = weak[i], e = weak[i + wLen - 1];
            int cnt = 0;
            for (int j = 0; j < dLen; ++j) {
                s += dist[j];
                ++cnt;
                if (s >= e) {
                    ans = min(ans, cnt);
                    break;
                }

                // s보다 큰 weak[j] 중에 제일 작은값
                int nIdx = upper_bound(weak.begin(), weak.end(), s) - weak.begin();
                s = weak[nIdx];
            }
        }
    } while (next_permutation(dist.begin(), dist.end()));

    return ans == INF ? -1 : ans;
}
