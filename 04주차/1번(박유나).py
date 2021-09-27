from collections import defaultdict

""" 0. 입력 받기 및 초기화 """
N=int(input()) #20개 > 20*20=400개 400*20*20*4*4b = 2,560,000

student_list=[] #학생 리스트
student_dic = defaultdict(list)
for _ in range(N**2):
    student, *s_like = map(int,input().split())
    student_dic[student] = s_like #각각의 학생들이 좋아하는 학생들을 사전형식으로
    student_list.append(student)

seat=[[0]*N for _ in range(N)] #확정지은 자리
seat[1][1]=student_list[0] #맨 처음 학생 자리 고정(2,2)


""" 1. 자리 정하기 """
dx=[-1, 0, 0, 1]; dy=[0, -1, 1, 0] #상, 좌, 우, 하
for cnt in range(1, N*N): #학생 수만큼
    check=[[0]*N for _ in range(N)] #확정지은 자리
    m_num=-1
    for i in range(N):
        for j in range(N):
            if seat[i][j]: continue #비어있는 자리가 아니라면, 탐색하지 않음
            for x, y in zip(dx, dy): #비어있는 자리만 탐색
                nx, ny = i+x, j+y
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if seat[nx][ny]==0: check[i][j]+=1 #빈 자리라면, 가치 1 추가
                if seat[nx][ny]!=0: #자리가 있다면,
                    for count in range(1, N+2): #그 자리가 해당 학생이 좋아하는 학생이라면, 가치 10 추가
                        if seat[nx][ny] in student_dic[student_list[cnt]]:
                            check[i][j]+=10

                """ 가치가 가장 큰 자리의 위치 저장 """
                if m_num<check[i][j]: #가치가 가장 큰 값
                    m_num=check[i][j]
                    px, py=i, j #처음으로 가치가 가장 큰 값의 위치 저장

    """ 자리 확정 """
    seat[px][py]=student_list[cnt] #자리 확정


""" 2. 학생 만족도 계산하기 """
total=0
for i in range(N):
    for j in range(N):
        number=0
        for x, y in zip(dx, dy):
            nx, ny = i+x, j+y
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if seat[nx][ny] in student_dic[seat[i][j]]: number+=1 #좋아하는 학생과 앉았다면, 카운팅
        if number!=0: #만족도가 0이 아니라면,
            total+=10**(number-1)

print(total) #최종 학생 만족도 출력
