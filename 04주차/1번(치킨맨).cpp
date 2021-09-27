#include <iostream>
#include <queue>
#define friend _friend
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)
using namespace std;
// 우선순위큐 이용한 우선순위 구현

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

struct Pos {
    int r, c, blank, friend;
    bool operator<(const Pos& other) const {
        if (friend == other.friend) {
            if (blank == other.blank) {
                if (r == other.r) return c > other.c;
                return r > other.r;
            }
            return blank < other.blank;
        }
        return friend < other.friend;
    }
};

struct Student {
    int sid, prefer[4], r, c;
};

int n;
int board[20][20];
Student student[400];

void arrange() {
    for (int id = 0; id < n * n; ++id) {
        priority_queue<Pos> pq;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j]) continue;

                int blank = 0, friend = 0;
                for (int d = 0; d < 4; ++d) {
                    int nr = i + dr[d];
                    int nc = j + dc[d];
                    if (0 > nr || 0 > nc || n <= nr || n <= nc) continue;
                    if (board[nr][nc] == 0) {
                        ++blank;
                    } else {
                        for (int k = 0; k < 4; ++k) {
                            if (board[nr][nc] == student[id].prefer[k]) {
                                ++friend;
                                break;
                            }
                        }
                    }
                }

                pq.push({i, j, blank, friend});
            }
        }

        int r = pq.top().r;
        int c = pq.top().c;
        board[r][c] = student[id].sid;
        student[id].r = r;
        student[id].c = c;
    }
}

int getScore() {
    int ret = 0;
    for (int id = 0; id < n * n; ++id) {
        int r = student[id].r;
        int c = student[id].c;
        int friend = 0;
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (0 > nr || 0 > nc || n <= nr || n <= nc) continue;
            for (int k = 0; k < 4; ++k) {
                if (board[nr][nc] == student[id].prefer[k]) {
                    ++friend;
                    break;
                }
            }
        }

        if (friend == 1)
            ret += 1;
        else if (friend == 2)
            ret += 10;
        else if (friend == 3)
            ret += 100;
        else if (friend == 4)
            ret += 1000;
    }

    return ret;
}

int main() {
    FASTIO;
    cin >> n;
    for (int i = 0; i < n * n; ++i) {
        cin >> student[i].sid;
        for (int j = 0; j < 4; ++j) {
            cin >> student[i].prefer[j];
        }
    }

    arrange();
    cout << getScore();
    return 0;
}
