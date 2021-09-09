#include <cstring>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

bool checkDist(vector<string>& map, int sr, int sc) {
    int d[5][5];
    memset(d, -1, sizeof(d));

    queue<tuple<int, int, int>> q;  // r, c, dist;
    d[sr][sc] = 0;
    q.push({sr, sc, 0});

    while (!q.empty()) {
        const auto& [r, c, dist] = q.front();
        q.pop();

        if (dist > 2) continue;
        if (dist != 0 && map[r][c] == 'P') return false;

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            int nDist = dist + 1;
            if (0 > nr || 0 > nc || 5 <= nr || 5 <= nc) continue;
            if (d[nr][nc] != -1 || map[nr][nc] == 'X') continue;

            d[nr][nc] = nDist;
            q.push({nr, nc, nDist});
        }
    }

    return true;
}

bool check(vector<string>& map) {
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (map[i][j] == 'P') {
                if (!checkDist(map, i, j))
                    return false;
            }
        }
    }

    return true;
}

vector<int> solution(vector<vector<string>> places) {
    int N = places.size();
    vector<int> answer(5, 0);

    for (int i = 0; i < N; ++i) {
        if (check(places[i])) answer[i] = 1;
    }

    return answer;
}
