import heapq
import sys

n=int(input())

heap = []
for _ in range(n): # n번 반복
    number=int(sys.stdin.readline()) # 입력받기
    if number!=0: # 0이 아니라면,
        heapq.heappush(heap, number) # 0이 아니라면, 힙에 삽입
    else:
        try:
            print(heapq.heappop(heap)) # 최소값 출력
        except:
            print(0) # 힙이 비어있다면, 0 출력
