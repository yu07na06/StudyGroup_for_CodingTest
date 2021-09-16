from itertools import permutations #순열
import copy

def solution(expression):

    """ 1. 입력받은 연산식 숫자와 연산 구분하여 나누기 """
    word=""; list_ex=[]; 
    for e in expression:
        if 48<=ord(e)<=57: #숫자라면,
            word+=e #숫자 문자를 차례로 차곡차곡 쌓는다.
        else: #연산 기호라면,
            list_ex.append(int(word)) #차곡차곡쌓은 숫자 문자를 리스트에 넣기
            list_ex.append(e) #연산 기호도 리스트에 넣기
            word="" #차곡차곡 쌓을 변수 초기화
    list_ex.append(word) #마지막 숫자 문자도 리스트에 넣기


    """ 2. 숫자와 연산식의 모든 경우의 수를 정하기 """
    oper_all=list(permutations(["+", "-", "*"]))
    

    """ 3. 우선순위대로 계산하기"""
    m_num=-1 #최대값 찾기
    for ope in oper_all: # 총 6번 : [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
        result=copy.deepcopy(list_ex) #계속 복사하면서, 사용(왜냐하면, 밑에서 리스트를 변경시키기 때문에)
        for op in ope: #튜플안에 있는 연사자들을 하나씩 분리해서 사용
            while True: #중복되는 연산자가 있을 수 있으므로, 계속 반복
                if op in result: #튜플안에 있는 연산자가 있다면,
                    index=result.index(op) #해당 연산자가 있는 인덱스를 찾기
                    #연산자 인덱스 좌, 우에 있는 값을 연산한다
                    if op == "+": value=int(result[index-1])+int(result[index+1])
                    elif op == "-": value=int(result[index-1])-int(result[index+1])
                    else: value=int(result[index-1])*int(result[index+1])
                    for _ in range(3): del result[index-1] #연산이 끝난 숫자와 연산자를 전부 지움
                    result.insert(index-1, value) #해당 인덱스에 연산한 값을 집어넣음
                else: break #튜플안에 있는 연산자가 없다면, 튜플안에 다음 연산자로 이동하기 위해 while문을 나감
        result=abs(int(result[0])) #최종적으로 데이터가 하나 남아 있으며, 혹시 빼기 연산이 결과이면 절대값을 씌어줌
        if result>m_num: #최대값 찾기
            m_num=result
    return m_num
