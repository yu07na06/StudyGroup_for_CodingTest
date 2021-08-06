import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q1107 {
    //리모컨
    private static boolean[] isBroken = new boolean[10]; //0~9 고장난 버튼 true

    private static int check(int n) {
        if (n == 0) {
            if (isBroken[0]) {
                return 0; //고장
            } else {
                return 1;
            }
        }
        int cnt = 0; //숫자 개수
        while (n > 0) {
            if (isBroken[n % 10]) {
                return 0;
            }
            n /= 10;
            cnt += 1;
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); //이동하려는 채널 0~500000
        int M = Integer.parseInt(br.readLine()); //고장난 버튼의 개수 0~10
        if (M > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                int index = Integer.parseInt(st.nextToken());
                isBroken[index] = true;
            }
        }

        int min = Math.abs(N - 100); //+-버튼만 누르면 최대(처음 100)
        for (int i = 0; i < 1000000; i++) {//0~999999(9빼고 다 고장)
            int num = check(i); //숫자 버튼 개수
            if (num > 0) {
                int count = Math.abs(N - i); //+- 누르는 횟수
                min = Math.min(min, num + count);
            }
        }
        System.out.println(min);

    }
}
