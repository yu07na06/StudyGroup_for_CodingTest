# def moveDown(num):
#     global check, cursor
#     count=0
#     while True:
#         cursor+=1
#         if cursor==len(check): 
#             if check[cursor]=='O':
#                 count+=1
#                 if count==int(num): break
#             cursor=0
#         if check[cursor] == 'O': count+=1
#         if count==int(num): break

# def moveUp(num):
#     global check, cursor
#     count=0
#     while True:
#         cursor-=1
#         if cursor==0: 
#             if check[cursor]=='O':
#                 count+=1
#                 if count==int(num): break
#             cursor=len(check)-1
#         if check[cursor] == 'O': count+=1
#         if count==int(num): break

# def solution(n, k, cmd):
#     global check, cursor

#     check=['O']*n
#     delete=[]
#     cursor=k

#     for commend in cmd:
#         C = commend.split()
#         if C[0] == 'D': 
#             moveDown(int(C[1]))
#         elif C[0] == 'U':
#             moveUp(int(C[1]))
#         elif C[0] == 'C':
#             delete.append(cursor)
#             check[cursor]='X'
#             if cursor!=len(check)-1: moveDown(1)
#             else: moveUp(1)
#         else:
#             check[delete[-1]]='O'
#             del delete[-1]

#     print(''.join(check))

def moveDown(num):
    global check, cursor
    count=0
    while True:
        cursor+=1 # 커서 증가
        if cursor==len(check): # 커서가 범위 넘어가면,
            cursor=0 # 커서를 처음 위치로
            if check[cursor]=='O': # 삭제한 것이 아니라면,
                count+=1 # 카운팅
                if count==int(num): break # 카운팅값이 이동할 값과 같다면,
        if check[cursor] == 'O': count+=1 # 삭제한 것이 아니라면, 카운팅
        if count==int(num): break # 카운팅값이 이동한 값과 같다면,

def moveUp(num):
    global check, cursor
    count=0
    while True:
        cursor-=1 # 커서 감소
        if cursor==-1: # 커서가 범위 넘어가면,
            cursor=len(check)-1 # 커서를 맨 뒤로
            if check[cursor]=='O': # 삭제한 것이 아니라면,
                count+=1 # 카운팅
                if count==int(num): break # 카운팅값이 이동할 값과 같다면,
        if check[cursor] == 'O': count+=1 # 삭제한 것이 아니라면, 카운팅
        if count==int(num): break # 카운팅값이 이동한 값과 같다면,

def solution(n, k, cmd):
    global check, cursor

    check=['O']*n # 삭제 표기를 위해
    delete=[] # 삭제할 것들 리스트에 담음
    cursor=k # 커서 위치 초기화

    for commend in cmd:
        C = commend.split()
        if C[0] == 'D': 
            moveDown(int(C[1])) # 아래로
        elif C[0] == 'U':
            moveUp(int(C[1])) # 위로
        elif C[0] == 'C':
            delete.append(cursor) # 삭제할 곳 커서 위치 넣기 (실제로 삭제하지 않음)
            check[cursor]='X' # 삭제 표기
            if cursor!=len(check)-1: moveDown(1) # 커서가 범위 넘지않으면, 아래로
            else: moveUp(1) # 커서가 범위 넘으면, 위로
        elif C[0] == 'Z':
            check[delete[-1]]='O' # 다시 삭제 안했다고 표기
            del delete[-1] # 다시 삭제 안했으니 삭제한 리스트에 담지 않기

    return ''.join(check) # 전부 합쳐서 출력
