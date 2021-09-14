"""
price	money	count	result
3	    20	    4	    10
"""

"""
def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1, count+1):
        total += i * price
    if total <= money:
        return 0
    else:
        return total - money
"""


def solution(price, money, count):
    # 등차수열 공식 : S_n = n(a+l)/2
    n = count  # n항
    a = price  # 첫번째 항
    l = price * count  # 마지막 항

    return max(0, n*(a+l)//2-money)


if __name__ == '__main__':
    price, money, count = 3, 20, 4
    print(solution(price, money, count))