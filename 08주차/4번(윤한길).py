import sys


input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
left = 0
right = N-1
min_answer = float('inf')
answer = []

while left != right:
    if min_answer > abs(nums[left] + nums[right]):
        min_answer = abs(nums[left] + nums[right])
        answer = [nums[left], nums[right]]

    if nums[left] + nums[right] > 0:
        right -= 1
    elif nums[left] + nums[right] < 0:
        left += 1
    else:
        break

print(*answer)