def solution(price, money, count):
    #등차수열 합공식
    molecule = 2*price + (count-1)*price # 분자
    result=(molecule*count)//2 # 등차수열 합
    return  result-money if result>money else 0 # 금액이 부족하지 않으면, 0
