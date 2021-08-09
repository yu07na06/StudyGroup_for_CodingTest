
arr__ = []
for _ in range(0, int(input())):
    sum__ = []
    for __ in range(0, int(input())):
        sum__.append(sum(map(int, input().split())))
    sum__.sort()
    arr__.append(0)
    for __ in sum__:
        if abs(int(sum__[0])-int(__)) < 2:
            arr__[_]+=1

print(arr__)
