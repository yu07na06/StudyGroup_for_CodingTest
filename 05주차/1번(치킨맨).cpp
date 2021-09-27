#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int timeline[100 * 3600];  // timeline[i] = 같은 시간대 시청자수

// 누적 재생시간이 많이 나오는 공익광고 시간대 배치했을 때 시작시간, 가장빠른 시작시간
int changeInSeconds(string s) {
    stringstream ss(s);  // 99:99:99
    int hour, min, sec;
    char etc;
    ss >> hour >> etc >> min >> etc >> sec;

    return hour * 3600 + min * 60 + sec;
}

string makeTimeStr(int n) {  // 360000 -> 100:00:00
    char s[9];
    sprintf(s, "%02d:%02d:%02d", n / 3600, n / 60 % 60, n % 60);
    string str = s;
    return str;
}

string solution(string play_time, string adv_time, vector<string> logs) {
    int playTime = changeInSeconds(play_time);  // 전체동영상 재생시간길이
    int advTime = changeInSeconds(adv_time);    // 공익광고 재생시간 길이

    for (string log : logs) {
        int start = changeInSeconds(log.substr(0, 8));  // 99:99:99-99:99:99
        int end = changeInSeconds(log.substr(9, 8));
        for (int i = start; i < end; ++i) {
            ++timeline[i];
        }
    }

    // 360000^2 = 1200억, On^2 미만으로 풀어야
    // advtime = 종료시간 - 시작시간, 시작시간=종료시간-advtime, 종료시간=시작시간+advtime

    long long nowSum = 0;
    int startIdx = 0;
    for (int i = 0; i < advTime; ++i) {  // 범위: 인덱스0 ~ advTime-1까지
        nowSum += timeline[i];
    }
    long long maxSum = nowSum;

    for (int i = advTime; i < playTime; ++i) {  // 끝나는 시간
        nowSum += timeline[i];
        nowSum -= timeline[i - advTime];  // 범위: 인덱스 1~advTime

        if (nowSum > maxSum) {
            maxSum = nowSum;
            startIdx = i - advTime + 1;
        }
    }

    return makeTimeStr(startIdx);
}
