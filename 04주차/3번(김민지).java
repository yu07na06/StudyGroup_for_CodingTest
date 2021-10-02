import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q14502 {
    //연구소
    private static int N, M, maxSafe;
    private static int[][] map;
    private static final int[] dx = {-1, 0, 1, 0}; //좌 하 우 상
    private static final int[] dy = {0, 1, 0, -1};

    private static class virus {
        int x, y;

        public virus(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //세로
        M = Integer.parseInt(st.nextToken()); //가로
        map = new int[N][M]; //연구소 0빈칸, 1벽, 2바이러스
        maxSafe = 0; //안전영역 최대크기

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        setWall(0); //벽세우면서 바이러스
        System.out.println(maxSafe);
    }

    //벽 세우기
    private static void setWall(int depth) {
        if (depth == 3) {
            spreadVirus();
            return;
        }

        //빈칸이면 벽세우기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 1;
                    setWall(depth + 1);
                    map[i][j] = 0;
                }
            }
        }
    }

    private static void spreadVirus() {
        int[][] virusMap = new int[N][M];
        Queue<virus> virusQueue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                virusMap[i][j] = map[i][j];
            }
        }

        //바이러스 큐에 넣기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (virusMap[i][j] == 2) {
                    virusQueue.add(new virus(i, j));
                }
            }
        }

        while (!virusQueue.isEmpty()) {
            virus v = virusQueue.remove();
            for (int i = 0; i < 4; i++) {
                int nx = v.x + dx[i];
                int ny = v.y + dy[i];

                //범위 확인
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (virusMap[nx][ny] == 0) { //빈칸이면 바이러스 넣기
                        virusMap[nx][ny] = 2;
                        virusQueue.add(new virus(nx, ny));
                    }
                }
            }
        }
        countSafeArea(virusMap);
    }

    private static void countSafeArea(int[][] virusMap) {
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (virusMap[i][j] == 0) {
                    cnt++;
                }
            }
            maxSafe = Math.max(cnt, maxSafe);
        }
    }
}
