package test;

public class test0101 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println(solutionT("a"));
	}

	public static int solutionT(String s) {
		if ( s.length() < 2 ) return s.length();
		int min = 1000;
		String a = s;
		for ( int i = 1; i < s.length(); i++ ) {		//문자열 전체 도는 for
			a = s;
			String before = "";
			int count = 1;
			String str = "";
			int idx = 0;
			for ( int j = 0; j < s.length()/i; j++) {
				if ((j+1)*i > s.length()) {
					break;
				}
				str = s.substring(j*i, (j+1)*i);
				if ( str.equals(before) ) {
					count++;
				} else {
					if ( !before.equals("") && count != 1 ) {
						a = a.substring(0, idx) + count + before + s.substring(j*i);
						idx = a.indexOf(s.substring(j*i));
					} else if ( !before.equals("") ) {
						idx += i;
					}
					before = str;
					count = 1;
				}
			}
			if ( !before.equals("") && count != 1 ) {
				a = a.substring(0, idx) + count + before + s.substring(s.length()-s.length()%i);
			}
			if ( min > a.length() ) {
				min = a.length();
			}
		}
        int answer = min;
        return answer;
    }

}
