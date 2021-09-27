import numpy

def solution(table, languages, preference):
    result=[0]*len(table)
    job=[]
    for i, tb in enumerate(table):
        tbList = list(reversed(tb.split())) # 리스트 꺼꾸로 뒤집기 (좌우반전)
        job.append(tbList[-1]) # 직업은 따로 빼두기

        for lang, pre in zip(languages, preference): # 선호언어랑 선호점수
            if lang in tbList: # 리스트안에 선호 언어가 있을 경우만,
                idx = tbList.index(lang) # 해당 선호 언어의 위치 받아오기
                result[i] += (idx+1)*pre # (위치+1) 과 선호 점수를 곱해서 결과창에 대입

    maxValue = max(result) # 큰 값 가져오기
    if result.count(maxValue)==1: # 큰 값이 유일하게 하나라면,
        maxIdx =  result.index(maxValue) # 큰 값 인덱스 들고오기
        return job[maxIdx] # 해당 인덱스에 위치한 직업 출력
    else:
        job_cp=[] # 중복되는 직업만 담을 리스트
        temp=numpy.array(result) # numpy로 만들기
        sameIdx=numpy.where(temp==maxValue)[0] # 중복되는 큰 값 인덱스 담기
        for s in sameIdx:
            job_cp.append(job[s]) # 중복되는 큰 값의 인덱스에 해당하는 직업 담기
        job_cp.sort() # 직업 정렬
        print(job_cp[0]) # 가장 첫번째꺼 출력
