"""
from itertools import combinations #조합
from collections import defaultdict #사전
import bisect #이분탐색

def solution(info, query):
    answer = []
    arr = defaultdict(list)
    for i in info:
        #사전 형태로 만들기 위해
        data = i.split() #띄어쓰기 기준으로 배열형태로 분리
        sco = int(data.pop()) #점수만 빼내기
        arr[''.join(data)].append(sco) #사전 형태로 (키,값)=(데이터, 점수)

        for j in range(4): #점수를 제외한 데이터가 4개 이므로 조합 4개를 만듦
            candi = list(combinations(data, j))
            for c in candi:
                arr[''.join(c)].append(sco) #조합 데이터를 키로 값을 점수로
    for i in arr: 
        arr[i].sort() #값을 정렬
    for i in query:
        #배열로 만들기 위해
        query_data = i.split() #띄어쓰기 기준으로 배열형태로 분리
        score = int(query_data.pop()) #점수만 빼내기
        query_data = ''.join(query_data) #점수빼고 데이터 합치기
        query_data = query_data.replace('and', '').replace(' ', '').replace('-', '') #데이터에 쓸모없는거 빼기
        #이진탐색
        answer.append(len(arr[query_data])-bisect.bisect_left(arr[query_data], score))
    
    print(answer)

a=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(a,b)
"""

def solution(info, query):
    answer = []

    arr = [[0,0] for _ in range(len(info))]
    num=0
    for i in info:
        #사전 형태로 만들기 위해
        data = i.split() #띄어쓰기 기준으로 배열형태로 분리
        sco = int(data.pop()) #점수만 빼내기
        arr[num][0]=''.join(data) #사전 형태로 (키,값)=(데이터, 점수)
        arr[num][1]=sco
        num+=1

    arr1 = [[0,0] for _ in range(len(info))]
    num=0
    for i in query:
        #배열로 만들기 위해
        query_data = i.split() #띄어쓰기 기준으로 배열형태로 분리
        score = int(query_data.pop()) #점수만 빼내기
        arr1[num][0]=''.join(query_data) #점수빼고 데이터 합치기
        arr1[num][0]=arr1[num][0].replace('and', '').replace('-','')
        arr1[num][1]=sco
        num+=1

    num=-1
    for a, b in arr: #info
        cnt=0
        num+=1
        for c, d in arr1: #query
            if c in a and d<=b:
                cnt+=1
                answer[num]=cnt
    print(answer)

a=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(a,b)