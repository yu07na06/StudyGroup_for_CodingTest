import sys

num=int(input())
water=list(map(int, input().split()))

left=0; right=num-1
min_value=sys.maxsize

while(True):
    if left==right:
        break
    value=water[left]+water[right]
    if abs(value)<=min_value: # 작거나 같음
        min_value=abs(value)
        result=[water[left], water[right]]
    if value>0: # 양수
        right-=1 # 왼쪽으로
    elif value<0: # 음수
        left+=1 # 오른쪽으로
    else:
        break
result=sorted(result)
print(*result)
