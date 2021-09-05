#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
#define FASTIO cin.tie(nullptr)->sync_with_stdio(false)

int n;
int board[21][21], board_cpy[21][21];

void rotate() {
    int tmp[21][21];
    memcpy(tmp, board_cpy, sizeof(board_cpy));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            board_cpy[i][j] = tmp[n - 1 - j][i];
}

void tilt(int d) {
    while (d--) rotate();

    for (int i = 0; i < n; i++) {
        int tmpArr[21] = {};
        int idx = 0;
        for (int j = 0; j < n; j++) {
            if (!board_cpy[i][j]) continue;
            if (!tmpArr[idx])
                tmpArr[idx] = board_cpy[i][j];
            else if (tmpArr[idx] == board_cpy[i][j]) {
                tmpArr[idx] *= 2;
                ++idx;
            } else {
                ++idx;
                tmpArr[idx] = board_cpy[i][j];
            }
        }
        for (int j = 0; j < n; j++) board_cpy[i][j] = tmpArr[j];
    }
}

int main(void) {
    FASTIO;

    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> board[i][j];

    int ans = 0;
    for (int k = 0; k < 1024; ++k) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board_cpy[i][j] = board[i][j];
        int order = k;
        for (int i = 0; i < 5; i++) {
            int d = order % 4;
            order /= 4;
            tilt(d);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = max(ans, board_cpy[i][j]);
            }
        }
    }

    cout << ans;
    return 0;
}