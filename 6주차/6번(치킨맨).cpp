// 자물쇠와 열쇠
#include <vector>
using namespace std;

int m, n;
vector<vector<int>> Lock, Lock_cpy, Key;

void rotate() {
    vector<vector<int>> tmp(m, vector<int>(m));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            tmp[i][j] = Key[j][m - i - 1];
        }
    }

    Key = tmp;
}

bool unlock(int r, int c) {
    for (int i = r; i < r + m; ++i) {
        for (int j = c; j < c + m; ++j) {
            Lock[i][j] += Key[i - r][j - c];
        }
    }

    for (int i = m; i < m + n; ++i) {
        for (int j = m; j < m + n; ++j) {
            if (Lock[i][j] != 1) {
                return false;
            }
        }
    }

    return true;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    m = key.size(), n = lock.size();
    Lock.resize(2 * m + n, vector<int>(2 * m + n));

    for (int i = m, r = 0; i < m + n; ++i, ++r) {
        for (int j = m, c = 0; j < m + n; ++j, ++c) {
            Lock[i][j] = lock[r][c];
        }
    }
    Lock_cpy = Lock;
    Key = key;

    for (int i = 0; i < m + n; ++i) {
        for (int j = 0; j < m + n; ++j) {
            for (int k = 0; k < 4; ++k) {
                rotate();
                if (unlock(i, j)) {
                    return true;
                }
                Lock = Lock_cpy;
            }
        }
    }

    return false;
}
