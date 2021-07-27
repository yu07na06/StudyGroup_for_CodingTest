public class minji_2 {
    //수들의 합2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] A = new int[N]; //N개로 된 수열
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        //수열의 합이 M이 되는 경우의 수
        int result = 0;
        int index = 0;
        while (true) {
            int sum = 0;
            for (int i = index; i < N; i++) {
                sum += A[i];
                if (sum == M) {
                    result++;
                } else if (sum > M) {
                    break;
                }
            }
            index++;
            if (index >= N) break;
        }
        System.out.println(result);
    }
}
