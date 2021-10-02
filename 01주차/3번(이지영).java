package test;

public class test01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println(solution(4, new int[][]{{1, 0, 1, 0}, {0, 1, 0, 1}, {1, 0, 1, 0}, {0, 1, 0, 1}}));
	}

	public static int solution(int n, int[][] computers) {
        int sum = n;
        String indexs = "";
        for ( int i = 0; i < computers.length; i++ ) {
            for ( int j = 0; j < computers[i].length; j++ ) {
                if ( computers[i][j] == 1 && indexs.indexOf(i+"") < 0 ) {
                    sum--;
                    indexs += ""+i;
                }
            }
        }
        return sum;
    }
}
