cnt = 0


def chk_(b, index, plusOrMinus):  # 쓸수 있는 숫자들중에 제일 가까운 숫자 리턴
    global cnt
    cnt += 1
    if cnt > 10:
        return index

    if index > 9:
        index = 0
    elif index < 0:
        index = 9
    if index in b:
        return index
    return chk_(b, index+plusOrMinus, plusOrMinus)
    # for _ in range(0, 100):
    #     if index in b:
    #         return index
    #     else:
    #         index+plusOrMinus
    #         if index > 9:
    #             index = 0
    #         elif index < 0:
    #             index = 9
    # return index


end = input()
bbc = int(input())
a = map(int, input().split())

if int(end) == 100:
    print(0)
else:
    arr = sorted(a)

    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in arr:
        if _ in b:
            b.remove(_)
    chk = False
    for _ in arr:
        if end.find(str(_)) > -1:
            chk = True
            break

    if chk == False:
        print(len(end))
    else:
        min__ = end
        max = end
        for _ in range(0, len(min__)):
            cnt = 0
            if int(min__[_]) in arr:
                if 0 < int(min__[_]) < 9:  # 끝이 아니면
                    min__ = min__[0:_]+str(chk_(b, int(min__[_])-1, -1)) + \
                        str(b[len(b)-1])*(len(min__)-_-1)
                    max = max[0:_]+str(chk_(b, int(max[_])+1, +1)
                                       )+str(b[0])*(len(min__)-_-1)
                elif int(min__[_]) == 0:  # 끝이 0이면 min만 예외
                    min__ = min__[0:_-1] + \
                        str(chk_(b, int(min__[_-1])-1, -1)
                            ) + min__[_:len(min__)]
                    min__ = min__[0:_]+str(b[len(b)-1])*(len(min__)-_)
                    max = max[0:_]+str(chk_(b, int(max[_])+1, +1)
                                       )+str(b[0])*(len(min__)-_-1)
                elif int(min__[_]) == 9:  # 끝이 9이면 max만 예외
                    try:
                        max = max[0:_-1] + \
                            str(chk_(b, int(max[_-1]) +
                                     1, +1)) + max[_:len(max)]
                    except:
                        max = "1"+max
                    max = max[0:_]+str(b[0])*(len(min__)-_)
                    min__ = min__[0:_]+str(chk_(b, int(min__[_])-1, -1)) + \
                        str(b[len(b)-1])*(len(min__)-_-1)
                break

        print(str(min(abs(int(end)-100), min(abs(int(end)-int(min__))+len(min__),
                                             abs(int(end)-int(max))+len(min__)))))
        #print(end, min__, max)
