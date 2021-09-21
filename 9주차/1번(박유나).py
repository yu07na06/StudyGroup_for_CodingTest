from itertools import product, repeat

dic=[]
def solution(word):
    for i in range(1, 6):
        dic.extend(list(map(''.join, product(['A', 'E', 'I', 'O', 'U'], repeat=i))))
    dic.sort()
    return dic.index(word)+1
