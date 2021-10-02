//20210909 1000-
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;
struct P {int x,y;};

string solution(vector<int> numbers, string hand) {
    // int map[4][3] = {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
    string ans = "";
    P l={3,0}, r={3,2};
    
    for(int num : numbers) {
        if(num == 0) num = 11;
        string hand_move;
        int x = (num-1) / 3;
        int y = (num+2) % 3;
        
        //cout << "CURR : " << x << ", " << y << '\n';
        if(y == 1) {  // 2, 5, 8, 0
            int l_len = abs(l.x - x) + abs(l.y - y);
            int r_len = abs(r.x - x) + abs(r.y - y);
            //cout << "\tLEN : " << l_len << " :: " << r_len << '\n';
            if(l_len == r_len){
                if(hand == "left") {
                    hand_move = "L";
                } else {
                    hand_move = "R";
                }
            } else if(l_len < r_len) {
                hand_move = "L";
            } else {
                hand_move = "R";
            }
        } else if(y == 0) { // 1, 4, 7
            hand_move = "L";
        } else if(y == 2) { // 3, 6, 9
            hand_move = "R";
        }
        
        if(hand_move == "R") {
            //cout << "\t\tRR : " << r.x << ", " << r.y << '\n';
            r = {x, y};
        } else {
            //cout << "\t\tLL : " << l.x << ", " << l.y << '\n';
            l = {x, y};
        }
        ans += hand_move;
    }
    return ans;
}
