public class minji_1 {
    //문자열 압축
    public int solution(String s) {
        int min = s.length();
        for (int i = 1; i <= s.length() / 2; i++) { //i : 자르는 단위
            int size = s.length();
            int num = 1; //문자열이 반복되는 수
            for (int j = 0; j <= (s.length() - i) / i - 1; j++) {
                if (s.substring(j * i, j * i + i).equals(s.substring((j + 1) * i, (j + 1) * i + i))) {
                    size -= i;
                    num++;
                } else {
                    if (num > 1) {
                        size += (int) (Math.log10(num) + 1);
                        num = 1;
                    }
                }
                if ((j == (s.length() - i) / i - 1) && num > 1) {
                    size += (int) (Math.log10(num) + 1);

                }
            }
            if (min > size)
                min = size;
        }
        return min;
    }

    public static void main(String[] args) {
        int result = new StringCompression().solution("abcabcabcabcdededededede");
        System.out.println(result);
    }
}
