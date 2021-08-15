# union_find 알고리즘 사용
""" 
참고 사이트
https://www.hyesungoh.xyz/Algorithm/BOJ-10216-Python/
https://deep-learning-study.tistory.com/589
"""

def find(a):
    global parent
    if parent[a]==a:
        return a
    p=find(parent[a])
    parent[a]=p
    return parent[a]

def union(a, b):
    global parent, rank
    a=find(a)
    b=find(b)
    if a==b:
        return
    if rank[a]>rank[b]:
        parent[b]=a
    else:
        parent[a]=b
        if rank[a]==rank[b]:
            rank[b]+=1

T=int(input()) #테스트 케이스 수
for _ in range(T):
    N=int(input()) #적군 진영의 숫자
    parent=[0]; rank=[0]; x_pos=[]; y_pos=[]; radius=[] #각 위치를 담을 리스트
    for i in range(N):
        x, y, r = map(int, input().split())
        x_pos.append(x)
        y_pos.append(y)
        radius.append(r)
        parent.append(i+1) #union_find에서 부모가 필요하다고 해서
        rank.append(0)

    result=N
    for i in range(N):
        for j in range(i+1, N):
            x_gap=x_pos[i]-x_pos[j]
            y_gap=y_pos[i]-y_pos[j]
            r_=radius[i]+radius[j]

            if (y_gap*y_gap + x_gap*x_gap) <= (r_*r_): #두 원의 위치관계 방정식 이용(피타고라스)
                if find(i)!=find(j):
                    union(i, j)
                    result-=1
    print(result)
