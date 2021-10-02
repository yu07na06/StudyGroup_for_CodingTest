package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q12865 {
    //평범한 배낭 : DP 배낭채우기문제(0-1 Knapsack Problem)
    //짐을 쪼갤 수 있는 배낭문제 Fraction Knapsack Problem : 탐욕 알고리즘(Greedy)
    //짐을 쪼갤 수 없는 배낭문제 0/1 Knapsack Problem : DP(메모이제이션)

    /*
    //Top-Down 탑다운: 재귀호출 (300ms)
    private static int[] W;
    private static int[] V;
    private static Integer[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); //물품의 수
        int K = Integer.parseInt(st.nextToken()); //버틸 수 있는 무게
        W = new int[N];
        V = new int[N];
        dp = new Integer[N][K + 1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(knapsack(N - 1, K));
    }

    private static int knapsack(int i, int k) {
        if (i < 0) {
            return 0;
        }

        if (dp[i][k] == null) { //탐색하지 않았으면
            if (W[i] > k) { //넘으면 이전 i값 탐색
                dp[i][k] = knapsack(i - 1, k);
            } else { //현재 물건(i)을 담을 수 있는 경우
                //이전 i값 VS 이전 i값에 대한 k-W[i]값 + 현재 가치
                dp[i][k] = Math.max(knapsack(i - 1, k), knapsack(i - 1, k - W[i]) + V[i]);
            }
        }
        return dp[i][k];
    }
    */

    //Bottom-up 바텀업: 반복문
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); //물품의 수
        int K = Integer.parseInt(st.nextToken()); //버틸 수 있는 무게
        int[] W = new int[N + 1];
        int[] V = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        //Bottom-up 1 (200ms)
        int[][] dp = new int[N + 1][K + 1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                if (W[i] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i]);
                }
            }
        }
        System.out.println(dp[N][K]);


        /*
        
        //Bottom-up 2 : 성능개선 (156ms)

        int[] dp = new int[K + 1];

        //K부터 탐색해서 담을 수 있는 무게까지 반복
        for (int i = 1; i <= N; i++) {
            for (int j = K; j - W[i] >= 0; j--) {
                dp[j] = Math.max(dp[j], dp[j - W[i]] + V[i]);
            }
        }
        System.out.println(dp[K]);

        */



    }
}
