# union_find 알고리즘 사용
""" 
참고 사이트
https://www.hyesungoh.xyz/Algorithm/BOJ-10216-Python/
https://deep-learning-study.tistory.com/589
"""

def find(a): #입력받은 노드의 루트노드를 찾아준다.
    global parent
    if parent[a]==a: #부모노드가 자기 자신이라면,(아무랑도 연결이 안되어 있다면,)
        return a #자기 자신 반환

    #부모 노드가 자기 자신이 아니라면,
    p=find(parent[a]) #부모노드의 할머니노드를 찾는다.
    parent[a]=p #자식노드의 부모노드를 알려준다.
    return parent[a] #최종적인 부모노드를 알려준다.

def union(a, b):
    global parent, rank
    a=find(a) #a의 부모노드를 찾는다.
    b=find(b) #b의 부모노드를 찾는다.
    if a==b: #두 노드의 부모노드가 같다면, 연결(?)이 이미 되었음
        return
    
    #두 노드의 부모노드가 다르다면,
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
                if find(i)!=find(j): #두 위치가 겹친다고 이미 했는데, find에서 서로 루트 노드가 다르다면,
                    union(i, j) #union으로 합쳐준다.
                    result-=1 #총 N개에서 두 그룹을 합쳤으니 1을 빼준다.
    print(result)
