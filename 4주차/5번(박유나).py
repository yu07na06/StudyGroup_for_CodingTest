"""
N, K = map(int, input().split()) # N:물품 수, K:버틸 무게
arr=[]; temp=[]

for i in range(N):
  W, V = map(int, input().split()) # W:물건 무게, V:물건 가치
  if W>K: continue #버틸 무게보다 물건 무게가 클 경우, 고려하지 않음
  for arr_W, arr_V in temp: #무게, 가치
    if W+arr_W <= K: #가치가 현재 물건 가치보다 작으면,
      arr.append((arr_W+W, arr_V+V)) #배열에 넣기
  temp.append((W, V)) #물건 무게, 물건 가치
  temp=temp+arr #임시 배열에 추가하기
  arr=[] #넣을 배열 초기화

answer=-1
for i, j in temp:
  if answer<j: #가치 최대값 출력
    answer=j
if answer==-1: #하나도 없다면,
  answer=0 #없다고 반환
print(answer)
"""

#참고 사이트 : https://suri78.tistory.com/2

N, K = map(int, input().split()) # N:물품 수, K:버틸 무게
arr = [[0]*N for _ in range(K+1)]
arr_list=[]

for i in range(N):
  W, V = map(int, input().split()) # W:물건 무게, V:물건 가치
  if W>K: continue
  arr[W][i]=V #물건 무게 인덱스에 물건 가치 대입
  for arr_W, j in arr_list:
    if W+arr_W <= K:
      arr[W+arr_W][j]=arr[arr_W][j]+arr[W][i]
      arr_list.append((W+arr_W, j))
  arr_list.append((W,i))

answer=-1
for i in arr:
  if answer<max(i):
    answer=max(i)

print(answer)
