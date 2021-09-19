/* 시간초과~ */
#         0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# number=[6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
min_number=[6, 7, 5, 4, 3, 2] # 성냥개비 개수
max_number=[2, 4, 5, 3, 7, 6] # 성냥개비 개수
min_dic={6:'0', 2:'1', 5:'2', 4:'4', 3:'7', 7:'8'} # 작은 수 기준 성냥 개수
max_dic={6:'9', 7:'8', 3:'7', 5:'5', 4:'4', 2:'1'} # 큰 수 기준 성냥 개수


def min_f(num):
    if num<=7: # 한자리 수라면, 한자리 수로 출력
        if num==6: print('6', end=''); return
        print(min_dic[num], end=''); return # 한자리 수 라면,
    cnt=0
    arr=[]
    while num:
        for n in min_number:
            if num-n>=0:
                if cnt==0 and n==6: continue
                arr.append(min_dic[n])
                num-=n
                break
        cnt=1
    reArr=reversed(arr)
    temp=''.join(reArr)
    print(temp, end='')

def max_f(num):
    arr=[]
    while num:
        if num-2<2: arr.append(max_dic[num]); break
        for n in max_number:
            if num-n>=0:
                arr.append(max_dic[n])
                num-=n
                break
    reArr=reversed(arr)
    temp=''.join(reArr)
    print(temp)

n =  int(input())
n_list = [int(input()) for _  in range(n)]

for i in n_list:
    min_f(i)
    print(" ", end='')
    max_f(i)
    
