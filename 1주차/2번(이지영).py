nm = input()
s = input()

m = int(nm.split(" ")[1])
sarr = s.split(" ")

a = 0
count = 0
idx = 0
i = 0
while i < len(sarr):
    if a == 0:
        idx = i
    a += int(sarr[i])
    if a == m:
        a = 0
        i = idx + 1
        count += 1
        continue
    elif a > m:
        a = 0
        i = idx + 1
        continue
    i += 1

print(count)
