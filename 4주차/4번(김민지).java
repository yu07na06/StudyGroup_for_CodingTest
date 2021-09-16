package programmers;

import java.util.ArrayList;

public class MaximizeFormula {
    //수식 최대화
    private char[] operator = {'+', '-', '*'};
    private char[] temp = new char[3];
    private boolean[] isVisited = new boolean[3];
    private ArrayList<Long> nums = new ArrayList<>(); //숫자
    private ArrayList<Character> ops = new ArrayList<>(); //연산자
    private long answer;

    public long solution(String expression) {
        answer = 0;

        StringBuilder num = new StringBuilder();
        for (int i = 0; i < expression.length(); i++) {
            if (Character.isDigit(expression.charAt(i))) {
                num.append(expression.charAt(i));
            } else {
                nums.add(Long.parseLong(num.toString()));
                num = new StringBuilder();
                ops.add(expression.charAt(i));
            }

            /*if (expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
                num += expression.charAt(i);
            } else {
                nums.add(Long.parseLong(num));
                num = "";
                ops.add(expression.charAt(i));
            }*/
        }
        //마지막 숫자 넣기
        nums.add(Long.parseLong(num.toString()));
        dfs(0);
        return answer;
    }

    private void dfs(int curr) {
        if (curr == 3) {
            math();
        } else {
            for (int i = 0; i < 3; i++) {
                if (!isVisited[i]) {
                    isVisited[i] = true;
                    temp[curr] = operator[i];
                    dfs(curr + 1);
                    isVisited[i] = false;
                }
            }
        }
    }

    private void math() {
        ArrayList<Long> copyNums = new ArrayList<>(nums);
        ArrayList<Character> copyOps = new ArrayList<>(ops);

        for (int i = 0; i < temp.length; i++) {
            for (int j = 0; j < copyOps.size(); j++) {
                if (temp[i] == copyOps.get(j)) {
                    Long result = calc(copyNums.remove(j), copyNums.remove(j), temp[i]);
                    copyNums.add(j, result);
                    copyOps.remove(j);
                    j--;
                }
            }
        }
        answer = Math.max(answer, Math.abs(copyNums.get(0)));
    }

    private long calc(Long num1, Long num2, char op) {
        if (op == '+') {
            return num1 + num2;
        } else if (op == '-') {
            return num1 - num2;
        } else {
            return num1 * num2;
        }
    }

    public static void main(String[] args) {
        long result = new MaximizeFormula().solution("100-200*300-500+20");
        System.out.println(result);
    }
}
