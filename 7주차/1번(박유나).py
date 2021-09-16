import re

def solution(new_id):
    # 1단계 - 소문자 치환
    answer=new_id.lower()
    # print(answer)

    # 2단계 - 특정 문자외 제외
    answer=re.sub(r'[^a-zA-Z0-9-_.]','',answer)
    # print(answer)

    # 3단계 - 마침표 2개 이상 처리
    while '..' in answer:
        answer=answer.replace('..', '.')
    # print(answer)

    # 4단계 - 처음이나 끝에 마침표 제거
    if answer[0]=='.' and len(answer)>1: answer=answer[1:]
    if answer[-1]=='.': answer=answer[:-1]
    # print(answer)

    # 5단계 - 빈 문자열일경우 a대입
    if answer=="": answer="a"
    # print(answer)

    # 6단계 - 길이 자르기
    if len(answer)>=16: 
        answer=answer[:15]
        if answer[-1]=='.': answer=answer[:-1]
    # print(answer)

    # 7단계 - 길이 늘리기
    if len(answer)<=2:
        while len(answer)!=3:
            answer+=answer[-1]
    # print(answer)
    
    return answer
