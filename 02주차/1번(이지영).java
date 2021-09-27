package test;
public class Solution {

    public static void main(String[] args) {
		int[] arr = solution(new String[][]{{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, 
			{"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"}, {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}});
		System.out.println(arr[0]+""+arr[1]+""+arr[2]+""+arr[3]+""+arr[4]);
    }
    

    public static int[] solution(String[][] places) {
    	int[] arr = {1, 1, 1, 1, 1};
    	int[][] xarr = {{0, 1}, {-1, 3}, {-3, 5}, {-3, 3}, {-1, 1}};
    	for ( int i = 0; i < places.length; i++ ) {
    		for ( int j = 0; j < places[i].length; j++ ) {
    			if ( places[i][j].indexOf("P") < 0 ) continue;
    			int x = places[i][j].indexOf("P");
        		int y = j-2;

    			boolean chk = false;
        		for ( int l = 0; l < 5; l++ ) {	//xarr 의 길이만큼 돌기
        			x += xarr[l][0];
        			for ( int k = 0; k < xarr[l][1]; k++ ) {	//1, 3, 5, 3, 1 회씩 돌기
        				//x, y값이 현재 비교하는 좌표와 동일하면 continue;
        				if ( x == places[i][j].indexOf("P") && y == j ) continue;
        				if ( x >= 5 || y >= 5 ) continue;
            			if ( y < 0 || x < 0 ) {
            				if ( x < 0 ) x++;
            				continue;
            			}

    					if ( places[i][y].charAt(x) == 'P' && (Math.abs(j-y)+Math.abs(places[i][j].indexOf("P")-x) <= 2) ) {
                			char a = places[i][j].charAt(places[i][j].indexOf("P"));
                			char b = places[i][y].charAt(x);
            				int f = places[i][j].indexOf("P");
	        				if ( Math.abs(j-y)+Math.abs(places[i][j].indexOf("P")-x) <= 1 ) {	//안쪽은 p이면 무조건 true
	        					chk = true;
    							arr[i] = 0;
    							places[i][j].replace("P", "O");
                    			System.out.println(places[i][j]+":"+places[i][y]+"//"+k+"//"+j+":"+places[i][j].indexOf("P")+"="+a+y+":"+x+"="+b);
	        					break;
	        				} else {
            					if ( places[i][j].indexOf("P") == x ) {		//좌표상 위 아래
            						if ( places[i][(j+y)/2].charAt(x) == 'O' ) {	//사이값이 테이블이면 true
            							chk = true;
            							arr[i] = 0;
            							places[i][j].replace("P", "O");
            							break;
            						}
            					} else if ( j == y ) {		//좌표상 양옆
            						if ( places[i][y].charAt((x+places[i][j].indexOf("P"))/2) == 'O' ) {	//사이값이 테이블이면 true
            							chk = true;
            							arr[i] = 0;
            							places[i][j].replace("P", "O");
            							break;
            						}
            					} else {		//대각선 측면
            						if ( ( places[i][y].charAt(places[i][j].indexOf("P")) == 'O' ) || ( places[i][j].charAt(x) == 'O' ) ) {	//둘중 하나가 테이블이면 true
            							chk = true;
            							arr[i] = 0;
            							places[i][j].replace("P", "O");
            							break;
            						}
            					}
        					}
        						
        				}
						places[i][j].replace("P", "O");
    					if (chk) break;
    					x++;
        			}
					if (chk) break;
					y++;
        		}
    			if ( arr[i] == 0 ) break;
				if (chk) break;
    		}
    	}
        int[] answer = new int[places.length];
        for ( int i = 0; i < answer.length; i++ ) answer[i] = arr[i];
        return answer;
    }
}