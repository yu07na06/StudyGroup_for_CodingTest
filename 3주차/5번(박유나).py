def solution(enroll, referral, seller, amount):
    PRICE=100; DIVIDE=10

    dic_e={name:i for i, name in enumerate(enroll)} #인덱스를 사전형식으로 만들어, 탐색이 쉽도록 한다.
    answer=[0]*len(enroll) #결과 담을 리스트 생성

    for s, a in zip(seller, amount): #판매 직원과 그 직원이 판매한 칫솔 수량
        total=a*PRICE #판매한 칫솔값 계산
        index=dic_e[s] #판매한 직원 인덱스 파악
        price10=total//DIVIDE #10%
        price90=total-price10 #90%
        answer[index]+=price90 #칫솔 1개만 팔아도 100원이며, 이를 추천인에게 10% 줄때 10원이므로 1원 미만일 경우가 없어 예외처리하지 않음
        while True:
            seller_upper=referral[index] #추천인 찾기
            if seller_upper=="-": break #추천인이 없으면, while문 종료
            total=price10 #90%는 이미 판매 직원이 가져갔으므로, 나머지 10%가 전체 가격이 된다.
            price10=total//DIVIDE #10%
            price90=total-price10 #90%
            index=dic_e[seller_upper] #추천인 인덱스 파악
            if price10<1: #추천인에게 10% 주는 금액이 1원 미만이면, 안주고 종료
                answer[index]+=total
                break
            answer[index]+=price90

    return answer
