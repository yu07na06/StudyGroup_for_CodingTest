#include <string>
#include <vector>
using namespace std;

vector<string> words{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int solution(string s) {
    string answer;

    int pos = 0;
    while (pos < s.length()) {
        if (isdigit(s[pos])) {
            answer += s[pos++];
        } else {
            for (int i = 0; i < 10; ++i) {
                if (s.find(words[i], pos) == pos) {
                    answer += '0' + i;
                    pos += words[i].length();
                    break;
                }
            }
        }
    }

    return stoi(answer);
}
