#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

vector<char> order{'+', '-', '*'};  // 연산자 순열
vector<long long> nums, cpy_nums;   // 원본 저장용cpy
vector<char> op, cpy_op;

long long calc() {
    for (int i = 0; i < 3; ++i) {  // 연산자 순서대로
        for (int j = 0; j < op.size(); ++j) {
            if (op[j] == order[i]) {
                if (op[j] == '+') {
                    nums[j] += nums[j + 1];
                } else if (op[j] == '-') {
                    nums[j] -= nums[j + 1];
                } else {
                    nums[j] *= nums[j + 1];
                }

                nums.erase(nums.begin() + j + 1);
                op.erase(op.begin() + j);
                --j;
            }
        }
    }

    return abs(nums[0]);
}

long long solution(string expression) {
    long long ans = 0;

    char exp[100];
    strcpy(exp, expression.c_str());

    char* p = strtok(exp, "+-*");
    while (p != NULL) {
        nums.push_back(stoll(p));
        p = strtok(NULL, "+-*");
    }

    for (char ch : expression) {
        if (ch == '+' || ch == '-' || ch == '*')
            op.push_back(ch);
    }

    cpy_nums = nums;
    cpy_op = op;

    sort(order.begin(), order.end());
    do {
        nums = cpy_nums;
        op = cpy_op;
        ans = max(ans, calc());
    } while (next_permutation(order.begin(), order.end()));

    return ans;
}
