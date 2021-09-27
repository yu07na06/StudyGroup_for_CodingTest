""" 미완성 """
D, N = map(int, input().split()) # 오픈의 깊이(D), 피자 반죽의 개수(N)
D_list = list(map(int, input().split()))
N_list = list(map(int, input().split()))

ZERO=0; TWO=2
def binary(start, end, L, n):
    half=int((end-start)/TWO) # 반으로 쪼개기
    if (end-start)==ZERO: # 하나인 경우,
        if D_list[start]==n: # 해당 값이 찾는 값과 같다면,
            arr.append(start) # 리스트에 해당 인덱스를 추가한다.
        return
    if half==ZERO: # 반으로 쪼갠 인덱스가 0이라면, 두개이므로
        binary(start, start, D_list[start], n) # 하나씩
        binary(end, end, D_list[end], n) # 하나씩
    else:
        binary(start, start+half-1, D_list[start:start+half], n) # 반으로 나눈거 기준으로 왼쪽
        binary(start+half, end, D_list[start+half:end+1], n) # 반으로 나눈거 기준으로 오른쪽

num=[]
for i, n in enumerate(N_list):
    arr=[] # 초기화하기
    binary(0, D-1, D_list, n) # 특정값 찾기
    num.append(arr) # 2차원 배열로 추가하기
print(num)
