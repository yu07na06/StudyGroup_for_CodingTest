#include <cmath>
#include <string>
#include <vector>

using namespace std;

// 147 왼쪽 369오른쪽 2580 가까운 손가락 or hand
string solution(vector<int> numbers, string hand) {  // numbers 1000
    string answer = "";

    vector<pair<int, int>> fingerPos(2);  // L, R 위치
    vector<pair<int, int>> board(13);     // 번호별 좌표

    fingerPos[0] = {3, 0}, fingerPos[1] = {3, 2};  // *, #
    board[0] = {3, 1};
    for (int i = 1; i <= 9; ++i) {
        int r = ((i - 1) / 3);
        int c = ((i - 1) % 3);
        board[i] = {r, c};
    }

    for (int n : numbers) {
        if (n == 1 || n == 4 || n == 7) {
            answer += 'L';
            fingerPos[0] = board[n];
        } else if (n == 3 || n == 6 || n == 9) {
            answer += 'R';
            fingerPos[1] = board[n];
        } else {                        // 2,5,8,0
            auto& [tr, tc] = board[n];  // r,c
            auto& [r1, c1] = fingerPos[0];
            auto& [r2, c2] = fingerPos[1];
            int len1 = abs(tr - r1) + abs(tc - c1);
            int len2 = abs(tr - r2) + abs(tc - c2);

            if (len1 < len2) {
                answer += 'L';
                fingerPos[0] = board[n];
            } else if (len1 > len2) {
                answer += 'R';
                fingerPos[1] = board[n];
            } else {  // 같은 경우
                if (hand == "left") {
                    answer += 'L';
                    fingerPos[0] = board[n];
                } else {
                    answer += 'R';
                    fingerPos[1] = board[n];
                }
            }
        }
    }

    return answer;
}
