long long solution(int price, int money, int count) { return money >= (long long) price * (count * (count + 1)) / 2 ? 0 : (long long) price * (count * (count + 1)) / 2  - money; }
