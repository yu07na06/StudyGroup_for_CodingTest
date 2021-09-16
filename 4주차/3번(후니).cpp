#include <iostream>
#include <queue>
#include <vector>
#include <memory.h>
int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	//1벽, 2바이러스
	int n, m, result;
	std::cin >> n >> m;
	int map[8][8], visited[8][8];
	std::vector<std::pair<int, int>> v, empty;

	for (int y = 0; y < n; y++) {
		for (int x = 0; x < m; x++) {
			std::cin >> map[y][x];
			if (map[y][x] == 2) v.push_back({ y,x });
			else if (map[y][x] == 0) empty.push_back({ y,x });
		}
	}

	int dy[] = { -1,0,1,0 };
	int dx[] = { 0,1,0,-1 };
	int pollution = 0, minPollution = n*m;

	int emptySize = empty.size();
	for (int i = 0; i < emptySize -2; i++){
		for (int j = i+1; j < emptySize -1; j++){
			for (int k = j+1; k < emptySize; k++){
				map[empty[i].first][empty[i].second] = 1;
				map[empty[j].first][empty[j].second] = 1;
				map[empty[k].first][empty[k].second] = 1;

				pollution = 0;
				memset(visited, 0, sizeof(visited));

				//bfs
				int size = v.size();
				for (int s = 0; s < size; s++) {
					
					if (visited[v.at(s).first][v.at(s).second]) continue;


					std::queue<std::pair<int, int>> q;
					q.push({ v.at(s).first , v.at(s).second });
					visited[v.at(s).first][v.at(s).second] = 1;
					
					while (!q.empty()) {
						int ty = q.front().first;
						int tx = q.front().second;
						q.pop();

						for (int a = 0; a < 4; a++) {
							int ny = dy[a] + ty;
							int nx = dx[a] + tx;
							if (ny < 0 || nx < 0 || ny >= n || nx >= m || visited[ny][nx] || map[ny][nx] == 1) continue;

							visited[ny][nx] = ++pollution;
							if (map[ny][nx] == 2) pollution--;
							q.push({ ny,nx });

						}

					}

					if (minPollution < pollution) break;

				}

				if (minPollution > pollution) {
					minPollution = pollution;
				}
				
				map[empty[i].first][empty[i].second] = 0;
				map[empty[j].first][empty[j].second] = 0;
				map[empty[k].first][empty[k].second] = 0;
			}
		}
	}

	result = empty.size() - minPollution - 3;
	std::cout << result;
}
