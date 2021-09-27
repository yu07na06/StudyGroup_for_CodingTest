N, H = map(int, input().split()) # 동굴 길이, 동굴 높이

# 석순과 종유석 배열에 담기
down=[0]*(H+1); up=[0]*(H+1)
for i in range(N):
    data=int(input())
    if i%2==0: down[data]+=1 # 석순 높이별 카운팅 ( 높이 3짜리가 5개라면, down[3]=5 )
    else : up[data]+=1 # 종유석 높이별 카운팅 ( 높이 2짜리가 3개라면, up[2]=3 )
downSum=sum(down) # 석순만 카운팅 전체 합을 구함 ( down=[1,2,3]이라면, downSum=6 )

# 여기서 H=5라면,
result=[0]*(H+1) # 구간별 파괴해야하는 개수를 담을 배열
upAdd=up[H]; downAdd=down[1] # 연산 시 필요한 변수
result[1]=(downSum+upAdd) # 첫번째 구간일 경우, 석순 높이가 1 이상인 값 전부와 종유석 높이가 5인 개수가 파괴해야할 개수이므로

# 여기서 H=5로 잡는다면,
for i in range(2, H+1): # 두번째 구간부터 높이 5까지
    upAdd+=up[H-i+1] # 종유석은 뒤에서부터 앞으로 카운팅 값을 계속 더해가기 위해
    result[i]+=(downSum-downAdd)+(upAdd) # i번째 구간일 경우, 석순 높이가 i이상인 값 전부와 종유석 높이가 5-i 이상인 개수가 파괴해야할 개수이므로
    downAdd+=down[i] # 석순은 앞에서부터 최대값을 시작으로 뒤로 갈 수록 계속 빼주기 위해
del result[0] # 사용하지 않는 0번째 인덱스 제거

value=min(result) # 최소값 찾기
print(value, result.count(value)) # 최소값과, 최소값을 카운팅한 값 출력
