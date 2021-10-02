#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;
#define F(i, n) for(int i = 0 ; i < n ; ++i)
#define FS(s, i, n) for(int i = s ; i < n ; ++i)

vector<pair<int, string>> sorting[11];

vector<string> solution(vector<string> orders, vector<int> course) {
	vector<string> answer;
	map<string, int> candidate;
	vector<pair<int, string>> vec;

	F(order_num, (int)orders.size()) {

		int menu_size = (int)orders[order_num].size();
		sort(orders[order_num].begin(), orders[order_num].end());

		for (int course_size : course) {
			vector<int> v(menu_size, 1);

			if (course_size > menu_size) continue;

			F(i, course_size) {
				v[i] = 0;
			}

			do {
				string str = "";
				
				F(i, (int)v.size()) {
					if (v[i] == 0) {
						//cout << orders[order_num][i] << ", ";
						str += orders[order_num][i];
					}
				}

				candidate[str]++;

			} while (next_permutation(v.begin(), v.end()));
		}

	}

	//F(i, 11) sorting[i].clear();

	for (auto a : candidate) {
		//cout << a.first << " : " << a.second << '\n';
		
		// 몇글자 글에 {갯수, 어떤 글} 들이 담김
		sorting[(int)a.first.size()].push_back({ a.second, a.first });
	}

	for (int course_size : course) {

		sort(sorting[course_size].begin(), sorting[course_size].end()
			, [](auto a, auto b) {
				return a.first > b.first;
			}
		);

		// cout << "COURSE : " << course_size << "\n";
		// for (auto a : sorting[course_size]) {
		// 	cout << a.second << ", ";
		// }
		// cout << '\n';

		if (sorting[course_size].empty() || sorting[course_size].front().first < 2) continue;

		answer.push_back(sorting[course_size].front().second);

		F(i, (int)sorting[course_size].size() - 1) {

			if (sorting[course_size][i].first == sorting[course_size][i + 1].first)
				answer.push_back(sorting[course_size][i + 1].second);
			else break;
		}
	}
	
	sort(answer.begin(), answer.end());

	// for (string sss : answer)
	// 	cout << sss << ", ";

	return answer;
}
