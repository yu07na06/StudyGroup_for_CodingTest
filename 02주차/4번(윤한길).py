num_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
N = str(input())
M = int(input())

if M == 0:
    broken = set()
else:
    broken = set(map(str, input().split()))

num_set = (num_set - broken)
ascending = descending = int(N)

flag = True
while not (set(str(ascending)).issubset(num_set) or set(str(descending)).issubset(num_set)):
    if M == 10:
        flag = False
        break
    ascending += 1
    descending -= 1

if set(str(ascending)).issubset(num_set):
    answer1 = ascending - int(N) + len(str(ascending))
if set(str(descending)).issubset(num_set):
    answer1 = int(N) - descending + len(str(descending))
answer2 = abs(100-int(N))

if not flag:
    print(answer2)
else:
    print(min(answer1, answer2))


"""
1555
8
0 1 3 4 5 6 7 9
답:670

99999
1
9
답:7
"""